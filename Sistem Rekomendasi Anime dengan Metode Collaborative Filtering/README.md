# Laporan Proyek Machine Learning – Abdul Ghofur Rais Kumar

## Project Overview

Anime adalah animasi dari Jepang yang digambar dengan tangan maupun menggunakan teknologi komputer. Kata anime merupakan singkatan dari "animation" dalam Bahasa Inggris, yang merujuk pada semua jenis animasi.Di luar Jepang, istilah ini digunakan secara spesifik untuk menyebutkan segala animasi yang diproduksi di Jepang. Meskipun demikian, tidak menutup kemungkinan bahwa anime dapat diproduksi di luar Jepang.Beberapa ahli berpendapat bahwa anime merupakan bentuk baru dari orientalisme.

Saat ini, ada banyak sekali platform yang memudahkan kita untuk menonton serial anime. Mulai dari layanan tv rumahan, k=hingga layanan streaming anime online. Hal ini sangat membantu kita untuk dapat mengakses anime. Sehingga kepopuleran anime semakin meningkat seiring dengan perkembangan Tv dan Internet.

Semakin berkembangnya anime sebagai sarana hiburan menimbulkan semakin banyaknya perusahaan animasi yang terjun didalamnya untuk ikut memproduksi anime. Sehingga semakin banyak anime yang beredar di pasaran. Dengan membanjirnya jumlah anime yang diproduksi, konsumen juga akan semakin banyak opsi untuk menonton jenis anime yang mereka sukai.

## Business Understanding

Dengan semakin banyaknya anime yang ada, menyulitkan konsumen untuk dapat menemukan anime yang sesuai dengan keinginan mereka jika harus memilih dari tumpukan judul anime yang tersedia. Sehingga dibutuhkan suatu sistem yang dapat menyarankan pengguna dalam memilih anime yang sesuai dengan keinginan mereka.
Pada kali ini, kita akan membuat suatu sistem rekomendasi dengan metode Collaborative Filtering untuk memudahkan pengguna dalam memilih anime yang mereka suka.

### Problem Statements
Berdasarkan permaslahan diatas, berikut adalah hal yang harus diselesaikan untuk mengatasi persoalan kita sebelumnya.
-	Sistem apa yang tepat untuk diterapkan pada kasus ini?
-	Bagaimana cara membuat sistem rekomendasi anime pada platfrom streaming anime?
### Goals
Berdasarkan permasalahan sebelumnya, berikut adalah tujuan dari projek ini:
-	Membuat sistem rekomendasi anime untuk platfrom streaming anime.
-	Memberikan rekomendasi anime untuk pengguna.
### Solution approach
Berdasarkan permaslaahn kita pada projek ini,  saya akan menggunakan metode Collaborative Filtering untuk membuat sistem rekomendasi anime. 
Collaborative filtering merupakan sistem rekomendasi yang penentuan rekomendasinya, bergantung pada pendapat daftar pengguna. Collaborative filtering dibagi menjadi dua kategori, yaitu: model based (metode berbasis model machine learning) dan memory based (metode berbasis memori). Pada projek ini, akan menggunakan memory based (metode berbasis memori), yang dibagi menjadi.
-	Item-item filtering: dari konten-konten yang disukai dan/atau tidak disukai pengguna, cari K konten lain yang memiliki rating serupa (berkorelasi tinggi)
-	User-user filtering: dari pengguna-pengguna yang memiliki preferensi serupa dan/atau berbanding terbalik dengan pengguna u, cari K konten lain yang disukai dan/atau tidak disukai oleh mereka
## Data Understanding
Dataset ini ini berisi informasi tentang data preferensi pengguna dari 73.516 pengguna di 12.294 anime. Dimana setiap pengguna dapat menambahkan anime ke dalam daftar dan memberikan peringkat dan kumpulan data ini adalah kompilasi dari peringkat tersebut.
Sumber dataset : [Anime Recommendations Database](https://www.kaggle.com/CooperUnion/anime-recommendations-database)
### Isi dataset
Anime.csv
- anime_id : id unik myanimelist.net dari setiap anime.
- name : nama lengkap anime.
- genre : daftar genre anime yang dipisahkan koma.
- type : film, TV, OVA, dll.
- episode : berapa banyak episode dalam acara ini. (1 jika film).
- rating : rating rata-rata dari 10 untuk anime ini.
- members : jumlah anggota komunitas yang ada di anime ini
"kelompok".

Rating.csv
- user_id : ID pengguna yang dibuat secara acak yang tidak dapat diidentifikasi.
- anime_id : anime yang telah dinilai oleh pengguna ini.
- rating : rating dari 10 yang telah ditetapkan pengguna ini (-1 jika pengguna menontonnya tetapi tidak memberikan rating).

## Data Preparation
Dalam melakukan data preparation, kita akan melakukan beberpa proses sebelum data dapat dimodeling sebagai berikut. 
-	Mengatasi Missing Value
Pada dataset, nilai missing value dari rating, diisi dengan nilai -1. Kita akan mengubah setiap rating yang bernilai -1, denan nilai null value, dikarenakan selanjutkan kita akan menghitung rata-rata rating tiap user. Sehingga diharapkan rating tidak terdistrosi.
-	melakukan pivoting tabel
Dalam collaborative filtering, kita perlu membuat tabel pivot 'user_id' pada satu sumbu dan 'name' di sumbu lainnya. Tabel pivot akan membantu kami dalam menentukan kesamaan antara pengguna dan anime untuk memprediksi dengan lebih baik siapa yang akan menyukai apa.
-	Normalisasi values 
Hal ini dilakukan agar rentang nilai pada label numerik hanya antara 0-1 sehingga dapat mempercepat komputasinya. Selain itu standarisasi juga membuat semua label numerik memiliki rentang nilai yang sama. Normalisasi dilakukan dengan menggunakan min-max normalization.


## Modeling
Pada modeling, kita akan menggunakan metode cosine similiarity untuk mendapatkan rekomendasi anime. Kita dapat melakukan metode cosine similiarity dengan cara memanggil fungsi cosine_similarity dengan argumen dataframe sebagai objeknya pada library sklearn.
Berdasarkan cosine similiarity, kita akan mencoba melakukan rekomendasi anime untuk anime yang mirip dengan Gintama dan Naruto sebagai berikut.

Kita akan coba melihat 10 user dengan preferensi yang mirip dengan user no 5 sebagai berikut:

Terakhir, kita dapat melihat rekomendasi anime untuk user no 5berdasarkan preferensi pengguna lain 

kita juga dapat mendapatkan nilai rating potensial antara user no 5 dan anime gintama

## Evaluasi

Berdasarkan perhitungan nilai Mean Squared Error diatas, kita mendapatkan nilai MSE sebesar 12.5. Hal ini tergolong rendah(kita memangkatkan nilai error rata-rata) sehingga sistem rekomendasi dapat kita gunakan. Hasil dari nilai rekomendasi yang dilakukan juga cukup baik. Namun, peningkatan performa sistem masih dapat dilakukan kedepannya dengan algoritma yang lebih baik.

## Referensi
Girsang A.S, Al Faruq B., Herlianto , & Simbolon. S(2020). Collaborative Recommendation System in Users of Anime Films. Journal of Physics: Conference Series.

