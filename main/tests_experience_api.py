import uuid

from django.contrib.auth.models import Group, User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from main.models import Experience

PASSWORD = "test-password"


class ExperienceAPITest(APITestCase):
    """Test API Experience (Individual Assignment 6) untuk keempat peran:
    pengunjung, pengguna biasa, Editor, dan pemilik portofolio (superuser)."""

    def setUp(self):
        self.owner = User.objects.create_superuser(
            username="owner", password=PASSWORD, email="owner@example.com",
        )
        self.editor = User.objects.create_user(
            username="editor", password=PASSWORD, email="editor@example.com",
        )
        # get_or_create: tetap aman kalau grup Editor sudah dibuat lewat migration.
        editor_group, _ = Group.objects.get_or_create(name="Editor")
        self.editor.groups.add(editor_group)
        self.visitor = User.objects.create_user(
            username="visitor", password=PASSWORD, email="visitor@example.com",
        )

        self.experience = Experience.objects.create(
            title="Creative Volunteer",
            description="Divisi kreatif acara seni sekolah",
            category="volunteer",
        )
        self.list_url = reverse("api:experience-list")
        self.detail_url = reverse("api:experience-detail", args=[self.experience.id])
        self.star_url = reverse("api:experience-star", args=[self.experience.id])
        self.payload = {
            "title": "Web Intern",
            "description": "Bantu bangun fitur dashboard",
            "category": "internship",
            "thumbnail": None,
            "ended_at": None,
        }

    def assertExperienceUntouched(self):
        """Isi database harus sama persis seperti di setUp, bukan cuma status HTTP-nya."""
        self.assertEqual(Experience.objects.count(), 1)
        self.experience.refresh_from_db()
        self.assertEqual(self.experience.title, "Creative Volunteer")
        self.assertEqual(self.experience.description, "Divisi kreatif acara seni sekolah")
        self.assertEqual(self.experience.category, "volunteer")
        self.assertIsNone(self.experience.ended_at)

    # ---------- baca & cari ----------

    def test_public_list_and_detail(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        item = response.data[0]
        self.assertEqual(item["id"], str(self.experience.id))
        self.assertEqual(item["category_display"], "Volunteer")
        self.assertTrue(item["is_ongoing"])
        self.assertEqual(item["star_count"], 0)
        self.assertFalse(item["is_starred"])
        self.assertEqual(set(item), {
            "id", "title", "description", "category", "category_display",
            "thumbnail", "started_at", "ended_at", "is_ongoing",
            "star_count", "is_starred", "starred_by_names",
        })
        self.assertNotIn("fields", item)

        detail = self.client.get(self.detail_url)
        self.assertEqual(detail.status_code, status.HTTP_200_OK)
        self.assertEqual(detail.data["title"], "Creative Volunteer")

    def test_search_by_title_and_empty_results(self):
        response = self.client.get(self.list_url, {"title": "VOLUN"})
        self.assertEqual([item["id"] for item in response.data], [str(self.experience.id)])
        response = self.client.get(self.list_url, {"title": "tidak-ada"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [])

    def test_missing_experience_returns_404(self):
        url = reverse("api:experience-detail", args=[uuid.uuid4()])
        self.assertEqual(self.client.get(url).status_code, status.HTTP_404_NOT_FOUND)

    def test_list_runs_a_constant_number_of_queries(self):
        for number in range(5):
            experience = Experience.objects.create(
                title=f"Extra {number}", description="x", category="freelance",
            )
            experience.starred_by.add(self.visitor, self.editor)
        # 1 query daftar + 1 query prefetch starred_by, berapa pun jumlah datanya.
        with self.assertNumQueries(2):
            response = self.client.get(self.list_url)
        self.assertEqual(len(response.data), 6)

    # ---------- pengunjung & pengguna biasa ----------

    def test_guest_and_regular_user_cannot_write(self):
        for user in (None, self.visitor):
            with self.subTest(user=getattr(user, "username", "guest")):
                self.client.force_authenticate(user=user)
                self.assertEqual(
                    self.client.post(self.list_url, self.payload, format="json").status_code,
                    status.HTTP_403_FORBIDDEN,
                )
                self.assertEqual(
                    self.client.put(self.detail_url, self.payload, format="json").status_code,
                    status.HTTP_403_FORBIDDEN,
                )
                self.assertEqual(
                    self.client.patch(self.detail_url, {"title": "Dibajak"}, format="json").status_code,
                    status.HTTP_403_FORBIDDEN,
                )
                self.assertEqual(
                    self.client.delete(self.detail_url).status_code,
                    status.HTTP_403_FORBIDDEN,
                )
                self.assertExperienceUntouched()

    def test_denied_response_explains_why(self):
        self.client.force_authenticate(user=self.visitor)
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertIn("izin", response.data["detail"])

    # ---------- Editor ----------

    def test_editor_can_patch_and_put(self):
        self.client.force_authenticate(user=self.editor)

        response = self.client.patch(self.detail_url, {"title": "Creative Lead"}, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.experience.refresh_from_db()
        self.assertEqual(self.experience.title, "Creative Lead")
        self.assertEqual(self.experience.description, "Divisi kreatif acara seni sekolah")

        response = self.client.put(self.detail_url, self.payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.experience.refresh_from_db()
        self.assertEqual(self.experience.title, "Web Intern")
        self.assertEqual(self.experience.category, "internship")

    def test_editor_cannot_create_or_delete(self):
        self.client.force_authenticate(user=self.editor)
        response = self.client.post(self.list_url, self.payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Experience.objects.count(), 1)

        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertExperienceUntouched()

    # ---------- pemilik ----------

    def test_owner_can_create(self):
        self.client.force_authenticate(user=self.owner)
        response = self.client.post(self.list_url, self.payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        created = Experience.objects.get(pk=response.data["id"])
        self.assertEqual(created.title, "Web Intern")
        self.assertEqual(created.category, "internship")
        self.assertEqual(Experience.objects.count(), 2)

    def test_owner_can_update_and_delete(self):
        self.client.force_authenticate(user=self.owner)
        response = self.client.patch(self.detail_url, {"title": "Creative Lead"}, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.experience.refresh_from_db()
        self.assertEqual(self.experience.title, "Creative Lead")

        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(response.content, b"")
        self.assertFalse(Experience.objects.filter(pk=self.experience.pk).exists())

    def test_put_needs_every_required_field(self):
        self.client.force_authenticate(user=self.owner)
        response = self.client.put(self.detail_url, {"title": "Setengah saja"}, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("description", response.data)
        self.assertExperienceUntouched()

    def test_ended_at_controls_is_ongoing(self):
        self.client.force_authenticate(user=self.owner)
        response = self.client.patch(self.detail_url, {"ended_at": "2026-05-01"}, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(response.data["is_ongoing"])
        self.experience.refresh_from_db()
        self.assertIsNotNone(self.experience.ended_at)

        response = self.client.patch(self.detail_url, {"ended_at": None}, format="json")
        self.assertTrue(response.data["is_ongoing"])
        self.experience.refresh_from_db()
        self.assertIsNone(self.experience.ended_at)

    # ---------- validasi input ----------

    def test_invalid_input_is_rejected_with_400(self):
        self.client.force_authenticate(user=self.owner)
        cases = [
            ({"title": "   "}, "title"),
            ({"title": "<b></b>"}, "title"),
            ({"title": "x" * 256}, "title"),
            ({"description": ""}, "description"),
            ({"description": "<script></script>"}, "description"),
            ({"thumbnail": "javascript:alert(1)"}, "thumbnail"),
            ({"category": "astronaut"}, "category"),
            ({"ended_at": "bukan tanggal"}, "ended_at"),
        ]
        for changes, field in cases:
            with self.subTest(changes=changes):
                response = self.client.post(
                    self.list_url, {**self.payload, **changes}, format="json",
                )
                self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
                self.assertIn(field, response.data)
        self.assertExperienceUntouched()

    def test_html_tags_are_stripped_before_saving(self):
        self.client.force_authenticate(user=self.owner)
        response = self.client.post(self.list_url, {
            **self.payload,
            "title": "<b>Web</b> Intern",
            "description": 'Halo <img src=x onerror="alert(1)">dunia',
        }, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        saved = Experience.objects.get(pk=response.data["id"])
        self.assertEqual(saved.title, "Web Intern")
        self.assertEqual(saved.description, "Halo dunia")

    def test_computed_fields_are_read_only(self):
        self.client.force_authenticate(user=self.owner)
        response = self.client.post(self.list_url, {
            **self.payload,
            "star_count": 99, "is_starred": True, "starred_by_names": "forged",
            "starred_by": [self.visitor.id], "is_ongoing": False,
            "category_display": "Hacked", "started_at": "2000-01-01T00:00:00Z",
        }, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["star_count"], 0)
        self.assertFalse(response.data["is_starred"])
        self.assertTrue(response.data["is_ongoing"])
        self.assertEqual(response.data["category_display"], "Internship")
        created = Experience.objects.get(pk=response.data["id"])
        self.assertEqual(created.starred_by.count(), 0)
        self.assertGreater(created.started_at.year, 2000)

    def test_wrong_method_on_list(self):
        self.client.force_authenticate(user=self.owner)
        self.assertEqual(self.client.delete(self.list_url).status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        self.assertEqual(self.client.put(self.list_url, self.payload, format="json").status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    # ---------- star ----------

    def test_guest_cannot_star(self):
        response = self.client.post(self.star_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(self.experience.starred_by.count(), 0)

    def test_star_toggles_for_logged_in_user(self):
        self.client.force_authenticate(user=self.visitor)
        response = self.client.post(self.star_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data["is_starred"])
        self.assertEqual(response.data["star_count"], 1)
        self.assertEqual(list(self.experience.starred_by.all()), [self.visitor])

        response = self.client.post(self.star_url)
        self.assertFalse(response.data["is_starred"])
        self.assertEqual(response.data["star_count"], 0)
        self.assertEqual(self.experience.starred_by.count(), 0)

    def test_star_always_uses_request_user(self):
        self.client.force_authenticate(user=self.visitor)
        response = self.client.post(
            self.star_url, {"user": self.owner.id, "starred_by": [self.owner.id]}, format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(list(self.experience.starred_by.all()), [self.visitor])

    def test_star_data_is_per_user_and_leaks_no_account_details(self):
        self.experience.starred_by.add(self.visitor, self.editor)

        guest = self.client.get(self.list_url)
        self.assertEqual(guest.data[0]["star_count"], 2)
        self.assertFalse(guest.data[0]["is_starred"])
        self.assertEqual(guest.data[0]["starred_by_names"], "editor, visitor")

        self.client.force_authenticate(user=self.visitor)
        as_visitor = self.client.get(self.list_url)
        self.assertTrue(as_visitor.data[0]["is_starred"])
        self.client.force_authenticate(user=self.owner)
        as_owner = self.client.get(self.list_url)
        self.assertFalse(as_owner.data[0]["is_starred"])

        for response in (guest, as_visitor, as_owner):
            body = response.content.decode()
            self.assertNotIn("@example.com", body)
            self.assertNotIn("password", body)

    def test_star_missing_experience_returns_404(self):
        self.client.force_authenticate(user=self.visitor)
        url = reverse("api:experience-star", args=[uuid.uuid4()])
        self.assertEqual(self.client.post(url).status_code, status.HTTP_404_NOT_FOUND)

    def test_star_only_accepts_post(self):
        self.client.force_authenticate(user=self.visitor)
        self.assertEqual(self.client.get(self.star_url).status_code, status.HTTP_405_METHOD_NOT_ALLOWED)


class ExperienceCSRFTest(APITestCase):
    """force_authenticate melewati SessionAuthentication, jadi CSRF tidak ikut
    teruji. Test di sini memakai login() sungguhan dan enforce_csrf_checks=True."""

    def setUp(self):
        self.owner = User.objects.create_superuser(username="owner", password=PASSWORD)
        self.editor = User.objects.create_user(username="editor", password=PASSWORD)
        editor_group, _ = Group.objects.get_or_create(name="Editor")
        self.editor.groups.add(editor_group)
        self.visitor = User.objects.create_user(username="visitor", password=PASSWORD)

        self.experience = Experience.objects.create(
            title="Creative Volunteer", description="Acara seni", category="volunteer",
        )
        self.list_url = reverse("api:experience-list")
        self.detail_url = reverse("api:experience-detail", args=[self.experience.id])
        self.star_url = reverse("api:experience-star", args=[self.experience.id])
        self.payload = {
            "title": "Web Intern", "description": "Dashboard", "category": "internship",
        }

    def logged_in_client(self, username):
        client = APIClient(enforce_csrf_checks=True)
        self.assertTrue(client.login(username=username, password=PASSWORD))
        return client

    def csrf_token(self, client):
        # Halaman Browsable API menyetel cookie csrftoken, sama seperti halaman Experience.
        page = client.get(self.list_url, HTTP_ACCEPT="text/html")
        self.assertEqual(page.status_code, status.HTTP_200_OK)
        return client.cookies["csrftoken"].value

    def test_writes_without_csrf_token_are_rejected(self):
        owner = self.logged_in_client("owner")
        response = owner.post(self.list_url, self.payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertIn("CSRF", response.data["detail"])
        self.assertEqual(Experience.objects.count(), 1)

        response = owner.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertTrue(Experience.objects.filter(pk=self.experience.pk).exists())

        editor = self.logged_in_client("editor")
        response = editor.patch(self.detail_url, {"title": "Dibajak"}, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.experience.refresh_from_db()
        self.assertEqual(self.experience.title, "Creative Volunteer")

        visitor = self.logged_in_client("visitor")
        response = visitor.post(self.star_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(self.experience.starred_by.count(), 0)

    def test_writes_with_csrf_token_succeed(self):
        owner = self.logged_in_client("owner")
        response = owner.post(
            self.list_url, self.payload, format="json",
            HTTP_X_CSRFTOKEN=self.csrf_token(owner),
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        editor = self.logged_in_client("editor")
        response = editor.patch(
            self.detail_url, {"title": "Creative Lead"}, format="json",
            HTTP_X_CSRFTOKEN=self.csrf_token(editor),
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.experience.refresh_from_db()
        self.assertEqual(self.experience.title, "Creative Lead")

        visitor = self.logged_in_client("visitor")
        response = visitor.post(self.star_url, HTTP_X_CSRFTOKEN=self.csrf_token(visitor))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.experience.starred_by.count(), 1)