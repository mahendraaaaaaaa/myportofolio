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
│       ├── project.html
│       ├── project_form.html
│       ├── skill.html
│       └── components/
│           ├── experience_delete_modal.html
│           └── project_delete_modal.html
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

---

© 2026 Bagas Mahendra Sri Kasta - Fakultas Ilmu Komputer, Universitas Indonesia