# Portofolio — Bagas Mahendra

Website portofolio pribadi, dibangun dari nol pakai HTML & CSS murni (tanpa framework). Fokusnya sederhana: tampilin siapa aku, latar belakang, dan tools desain yang biasa aku pakai.

---

## Fitur

- **Sticky navbar berbentuk pill** yang nge-highlight menu aktif sesuai section yang sedang dilihat, ini murni pakai CSS selector `:has()` dan `:target`, jadi nggak butuh JavaScript sama sekali buat scroll-spy-nya.
- **Role text yang berganti otomatis** ("Designer", "Computer Science", "Web Developer") pakai CSS `@keyframes`, looping 9 detik dengan 3 fase.
- **Section "About"** dengan bingkai foto ala browser window (dot merah-kuning-hijau) dan info NPM/Program Studi dalam bentuk pill.
- **Skill deck** - kartu skill software desain yang ditumpuk miring kayak kartu remi, dan rapi lagi + sedikit terangkat kalau di-hover.
- **Fully responsive** - di layar sempit, skill deck otomatis berubah jadi vertikal dan kartunya nggak dimiringkan lagi.

## Tech Stack

- HTML5 semantic markup
- CSS3 (custom properties / CSS variables, Grid, Flexbox, keyframe animation)
- Google Fonts — *Space Grotesk*
- Tanpa JavaScript, tanpa build tool, tanpa framework

## Struktur Proyek

├── templates
│   └── index.html
├── static/
│   ├── css/
│   │   └── style.css
│   └── img/
│       ├── Nobackground.png
│       ├── BagasFasilkom.jpeg
│       ├── PhotoshopLogo.png
│       ├── MarvelousDesignerLogo.png
│       ├── ProcreateLogo.png
│       └── FigmaLogo.png
└── README.md

## Cara Menjalankan

Karena ini murni HTML/CSS statis, nggak perlu install dependency apa pun.

1. Clone repo ini
   ```bash
   git clone <url-repo-kamu>
   cd <nama-folder>
   ```
2. Pastikan folder `static/img/` sudah berisi semua asset gambar yang dipakai di `index.html`.
3. Buka `index.html` langsung di browser, **atau** jalankan local server biar path relatif jalan dengan benar, misalnya:
   ```bash
   npx serve .
   # atau
   python3 -m http.server
   ```
4. Akses di `http://localhost:<port>`.

## Progress Pengerjaan

Jujur aja, aku nggak ngerjain ini dicicil rapi tiap minggu, dikerjain dalam 2–3 hari, dengan commit yang cukup sering (tiap beberapa jam sekali, pas ada bagian yang udah kelar/bisa di-checkpoint). Jadi log di bawah ini aku susun per hari & sesi kerja, bukan per minggu, biar lebih mencerminkan proses aslinya.

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

## Pertanyaan Reflektif

> Diisi tiap minggu sepanjang semester, satu blok `### Tugas N` per minggu.

### Tugas 1

1. Iya, aku pakai beberapa elemen semantik HTML5, tapi nggak semuanya. Struktur utamanya pakai `<header>`, `<main>`, tiga buah `<section>` (hero/profile, about, skills), `<nav>` untuk navbar, dan `<footer>`. Aku sengaja pilih `<section>` untuk tiap bagian utama karena masing-masing punya topik sendiri (identitas, tentang aku, skill) dan bisa dirujuk lewat anchor `#profile`, `#about`, `#skills`, jadi selain semantik, ini juga fungsional buat trik scroll-spy CSS yang aku bikin pakai `:target`.

   Yang *nggak* aku pakai adalah `<article>` dan `<aside>`. Aku nggak pakai `<article>` karena nggak ada konten yang sifatnya independen dan bisa berdiri sendiri kalau dipisah dari halaman, kartu skill di section Skills sekilas kelihatan kandidat, tapi isinya cuma nama software + deskripsi singkat, bukan konten "utuh" seperti sebuah post blog atau berita. Aku juga nggak pakai `<aside>` karena nggak ada konten tangensial/pelengkap semacam sidebar atau catatan terkait, semua yang ada di halaman ini memang konten inti portofolio, jadi maksa masukin `<aside>` justru bakal terasa dipaksakan cuma demi "kelihatan semantik", bukan karena benar-benar butuh.

2. Tantangan terbesarnya ada di efek "skill deck", kartu skill yang ditumpuk miring pakai `margin-left: -3rem` dan `transform: rotate(var(--rot))`. Efek ini enak dilihat di layar lebar, tapi begitu viewport mengecil, kartu-kartunya numpuk parah dan rotasinya bikin teks di dalam kartu kepotong/susah dibaca. Ini beda karakter dari masalah responsive pada umumnya (biasanya soal ukuran font atau jumlah kolom), di sini akar masalahnya di transform dan negative margin yang memang didesain untuk layar lebar.

   Cara aku evaluasi: resize browser pelan-pelan dari lebar penuh sampai ukuran HP sambil lihat elemen mana yang "pecah" duluan. Skill deck ternyata patah paling awal, jauh sebelum grid dua kolom di hero/about mulai sempit. Karena itu aku prioritaskan breakpoint eksplisit di `max-width: 700px` khusus untuk `.skill-card` dan `.skill-deck`, rotasi di-reset ke `0deg`, margin negatif dihapus, dan layout diubah jadi satu kolom (`flex-direction: column`).

   Untuk grid di hero dan about section, aku lebih mengandalkan unit fluid seperti `fr` di `grid-template-columns` dan `clamp()` di font-size (misalnya `clamp(3.2rem, 6vw, 4.6rem)` untuk heading), jadi ukuran teks otomatis menyesuaikan lebar layar tanpa breakpoint eksplisit. Ini cukup membantu, tapi belum sempurna aku sadar di layar yang sangat sempit (di bawah kira-kira 480px), `.hero-grid` dan `.about-grid` masih tetap dua kolom karena belum aku pecah jadi satu kolom secara eksplisit. Ini jadi salah satu titik yang masih perlu breakpoint tambahan.

3. Karena ini static web murni tanpa server-side apa pun, batasan paling kerasa ada di dua hal: pertama, kontak cuma bisa lewat link `mailto:`, yang bikin pengunjung harus buka aplikasi email mereka sendiri, nggak ada form kontak beneran yang bisa langsung mengirim pesan dari halaman, karena itu butuh proses di server untuk handle submission-nya. Kedua, semua konten (bio, daftar skill, foto) itu hardcoded langsung di `index.html` — setiap kali mau update sesuatu, aku harus edit HTML dan re-deploy, tidak ada cara mengubah konten tanpa menyentuh kode.

   Untuk iterasi selanjutnya, dua fungsionalitas dinamis yang paling ingin aku siapkan: (1) form kontak fungsional (misalnya lewat layanan seperti Formspree, atau backend kecil sendiri) supaya pengunjung bisa langsung mengirim pesan tanpa pindah aplikasi, dan (2) section proyek yang datanya diambil dari file data terpisah (JSON) atau headless CMS ringan, supaya aku bisa menambah proyek baru tanpa perlu mengubah struktur HTML setiap kali.

## AI Disclosure

Aku pakai AI (ChatGPT/Claude) sebagai *pair programmer*, terutama di tahap drafting awal — bukan buat generate satu website jadi sekali klik.

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

**Keterbatasan AI yang aku sadari selama proses ini:**
AI cenderung ngasih solusi yang "kelihatan benar" tapi nggak selalu tervalidasi cross-browser atau cross-device, misalnya soal dukungan `:has()` dan `mask-image` yang sebenarnya belum universal di semua browser, tapi AI nggak otomatis ngingetin itu kecuali ditanya spesifik. AI juga nggak "melihat" hasil visualnya secara langsung, jadi hal-hal kayak overlap animasi atau spacing yang kelihatan aneh cuma bisa ketauan setelah aku benar-benar buka di browser dan cek manual. Intinya, AI ini alat bantu percepatan, tapi keputusan desain final dan debugging visual tetap kerjaan manusia.

---

© 2026 Bagas Mahendra Sri Kasta - Fakultas Ilmu Komputer, Universitas Indonesia