# Project Overview

## Latar Belakang:

Saat ini, banyak perusahaan yang hadir dalam bentuk aplikasi mobile. Pada umumnya, perusahaan-perusahaan ini menyediakan produk atau layanan gratis di dalam aplikasi mobile mereka dengan harapan dapat mengubah pelanggan menjadi anggota berbayar. Beberapa contoh produk berbayar tersebut, yang berasal dari versi gratisnya, antara lain YouTube Red, Pandora Premium, Audible Subscription, dan You Need a Budget. Mengingat upaya pemasaran tidaklah gratis, maka perusahaan-perusahaan ini perlu mengetahui dengan pasti kepada siapa mereka harus mengarahkan penawaran dan promosi mereka.

Dalam konteks ini, pasar yang menjadi target adalah para pelanggan yang menggunakan produk gratis dari perusahaan tersebut melalui aplikasi mobile. Produk yang ditawarkan dalam bentuk keanggotaan berbayar umumnya memberikan fitur-fitur tambahan dan penyempurnaan dari produk gratis yang sudah ada, serta menambahkan fitur-fitur baru yang menarik. Sebagai contoh, YouTube Red memungkinkan pengguna untuk tetap mendengarkan video meskipun mereka keluar dari aplikasi.

## Tujuan:

Tujuan dari model ini adalah untuk memprediksi pengguna mana yang kemungkinan besar tidak akan berlangganan keanggotaan berbayar, sehingga perusahaan dapat mengarahkan upaya pemasaran yang lebih besar kepada mereka dalam upaya "mengonversi" mereka menjadi pengguna berbayar. Dengan demikian, perusahaan dapat mengoptimalkan sumber daya dan strategi pemasaran mereka dengan lebih efektif.

## Data Understanding:


Sumber Data: 
**Jumlah Data:** 

Dataset terdiri dari dua file utama, yaitu "data_aplikasi.csv" dan "top_screens.csv.csv". 

**Dataset:**

- user: ID Pengguna
- first_open: Tanggal pengguna pertama kali membuka aplikasi
- dayofweek: Hari dalam bentuk angka (1-7)
- hour: Jam ketika pengguna pertama kali membuka aplikasi
- age: Usia pengguna
- screen_list: Setiap halaman yang dikunjungi oleh pengguna dalam 24 jam pertama
- numscreens: Jumlah halaman dalam kolom screen_list
- minigame: Dalam aplikasi ini, terdapat permainan kecil yang bisa dipilih oleh pengguna
- used_premium_feature:
- enrolled: Fitur target dalam proyek ini
- enrolled_date: Tanggal dan waktu saat pengguna membeli produk berbayar, jika mereka melakukannya
- liked: Aplikasi ini memiliki tombol "suka" di setiap halaman dan pengguna dapat mengkliknya jika mereka menyukai fitur tertentu

## Solution Approach:


Berikut adalah penjelasan singkat tentang masing-masing metode klasifikasi yang digunakan dalam prediksi:

1. **Logistic Regression**:
   - Metode regresi logistik digunakan untuk memprediksi variabel target biner berdasarkan fitur-fitur yang diberikan.
   - Tujuan utama dari regresi logistik adalah untuk menghasilkan probabilitas prediksi yang memisahkan dua kelas.
   - Metode ini menggabungkan fungsi logit dengan pendekatan maksimum likelihood untuk menemukan parameter terbaik yang sesuai dengan data.
   - Dalam projek, menggunakan klasifikasi regresi logistik dengan solver 'liblinear' dan regularisasi L1 (penalty='l1').
2. **Random Forest**:
   - Random Forest adalah metode klasifikasi berbasis ensemble learning yang menggabungkan beberapa pohon keputusan (decision tree) untuk membuat prediksi.
   - Setiap pohon dalam Random Forest dibangun secara independen dan menghasilkan prediksi yang tidak tergantung satu sama lain.
   - Akurasi Random Forest biasanya tinggi karena mengurangi overfitting dan memperkenalkan variasi dengan menggabungkan hasil dari beberapa pohon.
   - Dalam projek, menggunakan metode Random Forest untuk klasifikasi.
3. **Support Vector Machine**:
   - Support Vector Machine (SVM) adalah metode klasifikasi yang membangun sebuah hyperplane atau sekelompok hyperplane dalam ruang fitur untuk memisahkan dua kelas.
   - SVM mencari hyperplane yang memiliki margin terbesar antara kelas-kelas yang berbeda.
   - SVM memiliki fleksibilitas dalam menggunakan fungsi kernel untuk menangani data yang tidak linear secara alami.
   - Dalam projek, menggunakan metode SVM untuk klasifikasi.
4. **Gradient Boosting**:
   - Gradient Boosting adalah metode klasifikasi berbasis ensemble learning yang menggabungkan beberapa model lemah (weak learner) menjadi model yang lebih kuat.
   - Metode ini menggabungkan pohon keputusan secara berurutan, di mana setiap pohon berusaha memperbaiki kesalahan prediksi model sebelumnya.
   - Gradient Boosting bekerja dengan mengoptimalkan fungsi loss menggunakan gradien descent.
   - Dalam projek, menggunakan metode Gradient Boosting untuk klasifikasi.
5. **Neural Networks**:
   - Neural Networks, atau disebut juga Artificial Neural Networks (ANN), adalah model klasifikasi yang terinspirasi oleh struktur dan fungsi jaringan saraf manusia.
   - ANN terdiri dari lapisan-lapisan neuron buatan (node) yang terhubung dengan bobot yang dapat disesuaikan.
   - Proses pembelajaran ANN melibatkan penyesuaian bobot agar dapat menghasilkan prediksi yang akurat.
   - Dalam projek, menggunakan metode Neural Networks untuk klasifikasi.
6. **Naive Bayes**:
   - Naive Bayes adalah metode klasifikasi yang didasarkan pada Teorema Bayes dengan asumsi independensi fitur.
   - Metode ini menghitung probabilitas posterior berdasarkan probabilitas prior dan likelihood fitur.
   - Naive Bayes sering digunakan untuk klasifikasi teks dan memiliki kecepatan komputasi yang cepat.
   - Dalam projekt, menggunakan metode Naive Bayes untuk klasifikasi.

Dalam contoh script tersebut, metode-metode klasifikasi ini diterapkan pada dataset yang sama dan performanya dievaluasi menggunakan metrik-metrik evaluasi umum seperti akurasi, presisi, recall, dan F1-Score.

## Result & Evaluation:

Rekapitulasi performa metode klasifikasi:

| Metode              | Akurasi | Presisi | Recall | F1-Score |
| ------------------- | ------- | ------- | ------ | -------- |
| Logistic Regression | 76.34%  | 0.76    | 0.76   | 0.76     |
| Random Forest       | 77.55%  | 0.78    | 0.76   | 0.77     |
| SVM                 | 73.81%  | 0.71    | 0.80   | 0.75     |
| Gradient Boosting   | 77.61%  | 0.79    | 0.75   | 0.77     |
| Neural Networks     | 76.05%  | 0.77    | 0.74   | 0.75     |
| Naive Bayes         | 76.05%  | 0.77    | 0.74   | 0.75     |

Kesimpulan:
- Dalam hal akurasi, Random Forest dan Gradient Boosting memperoleh performa terbaik dengan akurasi di atas 77%.
- Dalam hal presisi dan recall, SVM memperoleh nilai recall tertinggi, menunjukkan kemampuannya dalam mengklasifikasikan kelas positif dengan baik.
- F1-Score yang menggabungkan presisi dan recall menunjukkan performa seimbang antara presisi dan recall, di mana metode Gradient Boosting memperoleh skor tertinggi.
- Secara keseluruhan, metode Random Forest dan Gradient Boosting menunjukkan kinerja yang baik dalam mengklasifikasikan target variabel pada dataset ini.

