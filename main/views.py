import datetime
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from django.http import HttpResponse, JsonResponse
from django.core import serializers

from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required, permission_required
from django.views.decorators.http import require_POST

from main.models import Experience, Skill, Project
from main.forms import ExperienceForm, ProjectForm


def show_main(request):
    last_login = request.COOKIES.get('last_login', 'Belum ada sesi login / Cookie tidak ditemukan')
    context = {
        "name": "Bagas",
        "npm": "2506656551",
        "study_program": "S1 Sistem Informasi, University of Indonesia",
        "bio": (
            "A student of Information Systems at the University of Indonesia "
            "with a strong passion for graphic design and social media. "
            "I am a creative, proactive individual with a high level of adaptability. "
            "My experience as a Creative Division Volunteer at a school art performance event "
            "has trained me in project management, teamwork, and effective communication, "
            "while also honing my skills in using design tools such as Canva, Adobe Photoshop, "
            "Marvelous Designer, Figma, and Procreate. I am enthusiastic about continuing "
            "to learn and make a meaningful contribution within the campus environment."
        ),
        "last_login": last_login,
    }
    return render(request, "index.html", context)


# =========================
# EXPERIENCE
# =========================

def show_experience(request):
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Bagas",
        "title_query": title_query,
        "form": ExperienceForm(),
    }
    return render(request, "experience.html", context)


@login_required(login_url="/login/")
@permission_required("main.add_experience", raise_exception=True)
def create_experience(request):
    form = ExperienceForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Pengalaman baru berhasil ditambahkan!")
        return redirect("main:show_experience")

    context = {
        "name": "Bagas",
        "form": form,
    }
    return render(request, "experience_form.html", context)

def create_experience_ajax(request):
    if request.method != "POST":
        return JsonResponse({"message": "Method not allowed."}, status=405)

    if not request.user.is_authenticated or not request.user.has_perm("main.add_experience"):
        return JsonResponse(
            {"message": "Anda tidak memiliki izin untuk menambahkan experience."},
            status=403,
        )

    form = ExperienceForm(request.POST)
    if form.is_valid():
        form.save()
        return JsonResponse({"message": "Experience berhasil ditambahkan."}, status=200)

    return JsonResponse({"errors": form.errors.get_json_data()}, status=400)

@login_required(login_url="/login/")
@permission_required("main.change_experience", raise_exception=True)
def edit_experience(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)
    form = ExperienceForm(request.POST or None, instance=experience)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Experience berhasil diperbarui!")
        return redirect("main:show_experience")

    context = {
        "name": "Bagas",
        "form": form,
        "experience": experience,
    }
    return render(request, "experience_form.html", context)


@login_required(login_url="/login/")
@permission_required("main.delete_experience", raise_exception=True)
@require_POST
def delete_experience(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)
    experience.delete()
    messages.success(request, "Experience berhasil dihapus!")
    return redirect("main:show_experience")


def get_experience_json(request):
    title_query = request.GET.get("title", "").strip()
    experiences = Experience.objects.all()

    if title_query:
        experiences = experiences.filter(title__icontains=title_query)

    data = []
    for experience in experiences:
        data.append({
            "pk": str(experience.id),
            "fields": {
                "title": experience.title,
                "description": experience.description,
                "category": experience.category,
                "category_display": experience.get_category_display(),
                "thumbnail": experience.thumbnail,
                "is_ongoing": experience.is_ongoing,
            },
        })

    return JsonResponse(data, safe=False)


# =========================
# SKILL
# =========================

def show_skill(request):
    context = {
        "name": "Bagas",
        "skill_list": Skill.objects.all(),
    }
    return render(request, "skill.html", context)


# =========================
# PROJECT
# =========================

def show_project(request):
    # project.html sekarang mengambil data lewat AJAX (get_project_json),
    # jadi di sini cukup kirim data yang dibutuhkan halaman & modal tambah proyek.
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Bagas",
        "title_query": title_query,
        "form": ProjectForm(),
    }
    return render(request, "project.html", context)


@login_required(login_url="/login/")
@permission_required("main.add_project", raise_exception=True)
def create_project(request):
    form = ProjectForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Project baru berhasil ditambahkan!")
        return redirect("main:show_project")

    context = {
        "name": "Bagas",
        "form": form,
    }
    return render(request, "project_form.html", context)

@require_POST
def create_project_ajax(request):
    if request.method != "POST":
        return JsonResponse({"message": "Method not allowed."}, status=405)

    if not request.user.is_authenticated or not request.user.has_perm("main.add_project"):
        return JsonResponse(
            {"message": "Anda tidak memiliki izin untuk menambahkan project."},
            status=403,
        )

    form = ProjectForm(request.POST)
    if form.is_valid():
        form.save()
        return JsonResponse({"message": "Project berhasil ditambahkan."}, status=200)

    return JsonResponse({"errors": form.errors.get_json_data()}, status=400)


@login_required(login_url="/login/")
@permission_required("main.change_project", raise_exception=True)
def edit_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    form = ProjectForm(request.POST or None, instance=project)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Project berhasil diperbarui!")
        return redirect("main:show_project")

    context = {
        "name": "Bagas",
        "form": form,
        "project": project,
    }
    return render(request, "project_form.html", context)


@login_required(login_url="/login/")
@permission_required("main.delete_project", raise_exception=True)
@require_POST
def delete_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    project.delete()
    messages.success(request, "Project berhasil dihapus!")
    return redirect("main:show_project")


def get_project_json(request):
    title_query = request.GET.get("title", "").strip()
    projects = Project.objects.prefetch_related("starred_by").all()

    if title_query:
        projects = projects.filter(title__icontains=title_query)

    # Konstruksi data JSON manual (bukan serializers.serialize) supaya
    # bisa menyisipkan logika Star (is_starred, star_count) per pengguna.
    data = []
    for project in projects:
        starred_users = project.starred_by.all()
        is_starred = (
            request.user in starred_users if request.user.is_authenticated else False
        )
        starred_by_names = ", ".join([u.username for u in starred_users])

        data.append({
            "pk": str(project.id),
            "fields": {
                "title": project.title,
                "description": project.description,
                "category": project.category,
                "project_url": project.project_url,
                "thumbnail": project.thumbnail,
                "star_count": starred_users.count(),
                "is_starred": is_starred,
                "starred_by_names": starred_by_names,
            },
        })

    return JsonResponse(data, safe=False)


@login_required(login_url="/login/")
@require_POST
def toggle_star(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    # Kalau akun ini sudah pernah memberi star, batalkan star-nya.
    # Kalau belum, tambahkan star. (maksimal satu star per pengguna)
    if project.starred_by.filter(pk=request.user.pk).exists():
        project.starred_by.remove(request.user)
    else:
        project.starred_by.add(request.user)

    return redirect("main:show_project")


# =========================
# AUTH
# =========================

def register(request):
    form = UserCreationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Akun berhasil dibuat. Silakan login.")
        return redirect("main:login")

    context = {
        "name": "Bagas",
        "form": form,
    }
    return render(request, "register.html", context)


def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)
        response = redirect("main:show_main")
        response.set_cookie('last_login', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return response

    context = {
        "name": "Bagas",
        "form": form,
    }
    return render(request, "login.html", context)


def logout_user(request):
    logout(request)
    response = redirect("main:show_main")
    response.delete_cookie('last_login')
    return response
