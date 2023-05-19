# Project Overview: 

## Latar Belakang: 

Dalam industri hiburan anime, jumlah anime yang tersedia sangat banyak dan terus bertambah setiap tahunnya. Hal ini membuat pengguna kesulitan dalam menemukan anime baru yang sesuai dengan minat dan preferensi mereka. Oleh karena itu, dibutuhkan sistem rekomendasi yang dapat memberikan rekomendasi personalisasi kepada pengguna berdasarkan preferensi mereka. Dataset Anime Recommendation Database menyediakan data yang relevan untuk membangun sistem rekomendasi anime yang efektif.

Dengan adanya sistem rekomendasi anime yang handal, pengguna dapat:

- Meningkatkan pengalaman menonton: Pengguna dapat menemukan anime baru yang sesuai dengan minat dan preferensi mereka, sehingga memperkaya pengalaman menonton mereka. 
- Menyederhanakan pencarian: Pengguna tidak perlu menghabiskan waktu dan usaha yang besar untuk mencari anime baru secara manual, karena sistem rekomendasi akan memberikan rekomendasi yang relevan. 
- Menjelajahi genre baru: Sistem rekomendasi dapat membantu pengguna untuk mengeksplorasi genre anime yang belum mereka kenal sebelumnya, sehingga memperluas pengetahuan mereka tentang anime.



# Business Understanding:

## Problem Statements: 

Pengguna kesulitan menemukan anime baru yang sesuai dengan minat dan preferensi mereka dalam jumlah anime yang sangat besar dan keragaman genre. Pencarian manual menjadi tidak efisien dan memakan waktu.

## Goals:

Membangun sistem rekomendasi anime yang dapat memberikan rekomendasi personalisasi kepada pengguna berdasarkan preferensi mereka. Meningkatkan pengalaman menonton anime pengguna dengan menemukan anime baru yang relevan dengan minat dan preferensi mereka. Memperluas pengetahuan pengguna tentang genre anime yang belum mereka kenal sebelumnya.

## Solution Approach: 

Dalam mencapai tujuan tersebut, akan diajukan dua pendekatan solusi: Content-Based Filtering dan Collaborative Filtering.

### Content-Based Filtering: 

Pendekatan ini akan menggunakan informasi atribut anime, seperti genre, sinopsis, rating, dan popularitas, untuk merekomendasikan anime kepada pengguna. Prosesnya melibatkan langkah-langkah berikut: Menggunakan metode pemrosesan teks untuk memahami konten dan genre anime. Membangun model yang menganalisis kemiripan antara anime berdasarkan atribut-atribut tersebut. Ketika pengguna memberikan preferensi mereka, sistem menggunakan atribut yang relevan untuk merekomendasikan anime baru yang cocok dengan minat dan preferensi mereka.

#### Kelebihan:

Tidak memerlukan data perilaku pengguna, hanya menggunakan informasi konten dari anime. Mampu memberikan rekomendasi untuk anime baru yang belum memiliki data rating. Memperhitungkan kesesuaian genre antara anime yang sedang dilihat dan anime yang direkomendasikan. 

#### Kekurangan: 

Tidak mempertimbangkan preferensi pengguna secara langsung, sehingga mungkin menghasilkan rekomendasi yang terlalu mirip atau tidak beragam. 

### Collaborative Filtering: 

Pendekatan ini akan memanfaatkan informasi peringkat anime oleh pengguna untuk merekomendasikan anime kepada pengguna lain yang memiliki minat dan preferensi serupa. Prosesnya melibatkan langkah-langkah berikut: Membangun model kolaboratif yang menganalisis pola peringkat pengguna pada anime. Mengidentifikasi pengguna dengan minat dan preferensi serupa berdasarkan kesamaan pola peringkat. Merekomendasikan anime yang disukai oleh pengguna dengan minat serupa berdasarkan peringkat pengguna lain yang memiliki minat yang sama. Dengan menggunakan kedua pendekatan tersebut, diharapkan dapat memberikan rekomendasi anime yang lebih relevan dan sesuai dengan preferensi pengguna. Hal ini akan membantu pengguna menemukan anime baru yang menarik dan sesuai dengan minat mereka, serta memperluas pengetahuan mereka tentang genre anime yang belum mereka kenal sebelumnya.

#### Kelebihan:

Memanfaatkan informasi perilaku pengguna dalam membuat rekomendasi. Mampu memberikan rekomendasi yang disesuaikan dengan preferensi pengguna. Dapat menangani dataset dengan banyak pengguna dan anime. 

#### Kekurangan: 

Tergantung pada data rating pengguna, sehingga membutuhkan dataset dengan data rating yang cukup lengkap dan akurat. Tidak efektif untuk memberikan rekomendasi pada anime baru yang belum memiliki data rating. Dengan mengimplementasikan kedua solusi rekomendasi di atas, kita dapat menghasilkan rekomendasi top-N untuk anime berdasarkan konten dan perilaku pengguna. Content-based Filtering cocok untuk memberikan rekomendasi yang sesuai dengan genre anime yang sedang dilihat, sedangkan Collaborative Filtering cocok untuk memberikan rekomendasi yang disesuaikan dengan preferensi pengguna.



# Data Understanding:

- Jumlah Data: Dataset Anime Recommendation Database terdiri dari dua file utama, yaitu "anime.csv" dan "rating.csv". File "anime.csv" berisi informasi tentang anime, sedangkan file "rating.csv" berisi informasi peringkat anime oleh pengguna.
- Kondisi Data: Dataset Anime Recommendation Database dapat berisi informasi yang hilang atau tidak lengkap, sehingga perlu dilakukan pemrosesan data untuk membersihkan dan mengisi nilai yang hilang.
- Sumber Data: Dataset Anime Recommendation Database dapat diunduh dari Kaggle melalui tautan berikut: https://www.kaggle.com/CooperUnion/anime-recommendations-database
- Variabel atau Fitur pada Data:
  1. anime.csv:
     - anime_id: ID unik untuk setiap anime.
     - name: Nama anime.
     - genre: Genre anime yang dapat berisi lebih dari satu genre yang dipisahkan oleh koma.
     - type: Tipe anime seperti TV, Movie, OVA, dll.
     - episodes: Jumlah episode anime.
     - rating: Peringkat anime berdasarkan rating yang diberikan oleh pengguna.
     - members: Jumlah anggota yang memiliki anime ini dalam daftar mereka.
  2. rating.csv:
     - user_id: ID unik untuk setiap pengguna.
     - anime_id: ID unik untuk setiap anime.
     - rating: Peringkat yang diberikan oleh pengguna untuk anime tertentu.



Tahapan Data yang Diperlukan:

- Memuat dataset dan melihat beberapa baris pertama untuk memahami struktur data.
- Mengidentifikasi variabel yang memiliki nilai yang hilang atau tidak lengkap.
- Melakukan eksplorasi data dengan teknik visualisasi seperti histogram, scatter plot, atau diagram batang untuk mendapatkan wawasan tentang distribusi peringkat, genre anime, atau jumlah episode anime.
- Menganalisis statistik deskriptif untuk variabel numerik seperti rating dan members.



# Data Preparation:

Pada tahap Data Preparation, kita akan melakukan beberapa teknik untuk mempersiapkan data sebelum digunakan untuk membangun model rekomendasi. Berikut adalah langkah-langkah yang dilakukan:

## Handling Missing Values:

- Mengecek apakah terdapat nilai yang hilang pada dataset.
- Jika terdapat nilai yang hilang, kita perlu memutuskan apakah akan menghapus baris yang memiliki nilai yang hilang atau mengisi nilai yang hilang dengan pendekatan tertentu, seperti menggunakan nilai rata-rata atau modus.
- Untuk memastikan bahwa tidak ada nilai yang hilang atau kosong dalam dataset yang dapat mengganggu analisis dan pemodelan.



## Encoding Categorical Variables:

- Menangani variabel kategorikal seperti tipe anime atau genre anime.
- Jika variabel kategorikal memiliki banyak nilai unik, kita dapat menggunakan teknik seperti One-Hot Encoding atau Label Encoding untuk mengubahnya menjadi bentuk numerik yang dapat digunakan dalam model.
- Model yang digunakan biasanya membutuhkan input berupa angka, bukan kategori. Oleh karena itu, perlu mengubah variabel kategorikal menjadi representasi numerik.



## Scaling Numerical Variables:

- Menyamakan skala variabel numerik, seperti rating dan jumlah episode anime.
- Teknik seperti Min-Max Scaling atau Standard Scaling dapat digunakan untuk mengubah variabel numerik ke rentang yang serupa atau standar.
- Variabel dengan skala yang berbeda dapat mempengaruhi kinerja model. Dengan melakukan scaling, variabel dapat diperlakukan dengan proporsi yang sebanding.



## Data Integration:

- Menggabungkan informasi dari beberapa file jika ada, seperti menggabungkan dataset "anime.csv" dan "rating.csv" berdasarkan anime_id.
- Jika informasi yang diperlukan tersebar di beberapa file, menggabungkan data akan mempermudah proses analisis dan pemodelan.



# Modeling and Result:

Dalam tahap ini, kita akan membuat sistem rekomendasi untuk menyelesaikan permasalahan dan menghasilkan rekomendasi top-N sebagai output. Kita akan menggunakan dua solusi rekomendasi dengan algoritma yang berbeda, yaitu Content-based Filtering dan Collaborative Filtering. Berikut adalah implementasinya:

## Solusi 1: Content-based Filtering 

Content-based Filtering menggunakan informasi konten dari anime untuk membuat rekomendasi. Pada kasus ini, kita akan menggunakan atribut genre dan type anime sebagai fitur konten. 

Implementasi Content-Based Filtering untuk memberikan rekomendasi anime berdasarkan konten genre. Pertama, data anime diambil dari dataset yang telah diproses sebelumnya. Kemudian, dilakukan pemrosesan data untuk mengubah teks genre menjadi representasi vektor menggunakan metode TF-IDF. Setelah itu, dilakukan perhitungan cosine similarity antara vektor-vektor anime menggunakan linear_kernel. Fungsi get_content_based_recommendations() digunakan untuk mendapatkan rekomendasi anime berdasarkan anime yang diinputkan. Dalam fungsi ini, indeks anime yang sesuai dengan judul yang diberikan diambil, dan kemudian skor kesamaan pairwise diurutkan untuk mendapatkan anime dengan skor tertinggi. Rekomendasi yang dihasilkan adalah anime dengan skor kesamaan tertinggi kecuali anime yang diinputkan. Hasil rekomendasi ditampilkan dalam bentuk judul anime dan genre. Dalam contoh di atas, judul anime "Naruto" digunakan untuk mendapatkan rekomendasi berbasis konten. Jika terdapat rekomendasi, maka judul anime dan rekomendasi tersebut akan dicetak.

Output:

```
Content-based Recommendations for Naruto
                                                   name                                              genre
615                                  Naruto: Shippuuden  Action, Comedy, Martial Arts, Shounen, Super P...
841                                              Naruto  Action, Comedy, Martial Arts, Shounen, Super P...
1103  Boruto: Naruto the Movie - Naruto ga Hokage ni...  Action, Comedy, Martial Arts, Shounen, Super P...
1343                                        Naruto x UT  Action, Comedy, Martial Arts, Shounen, Super P...
1472        Naruto: Shippuuden Movie 4 - The Lost Tower  Action, Comedy, Martial Arts, Shounen, Super P...
```



## Solusi 2: Collaborative Filtering 

Collaborative Filtering menggunakan informasi perilaku pengguna untuk membuat rekomendasi. Pada kasus ini, kita akan menggunakan data rating pengguna pada anime sebagai dasar rekomendasi:

Implementasi Collaborative Filtering menggunakan library Surprise dalam Python. Collaborative. Pada studi kasus ini, data anime, pengguna, dan rating diberikan sebagai input untuk membuat dataset menggunakan library Surprise. Selanjutnya, dataset dibagi menjadi train set dan test set. Model Collaborative Filtering KNNBasic digunakan untuk melatih dataset train.

Fungsi get_collaborative_filtering_recommendations() digunakan untuk mendapatkan rekomendasi berdasarkan Collaborative Filtering untuk pengguna tertentu. Di dalam fungsi tersebut, prediksi rating pengguna dibuat untuk setiap anime, dan rekomendasi diurutkan berdasarkan prediksi rating tersebut. Rekomendasi teratas kemudian diambil dan dikembalikan sebagai judul anime.

Pada evaluasi, rekomendasi Collaborative Filtering untuk pengguna dengan user_id 100 dicetak.

Output:

```
Collaborative Filtering Recommendations for User 100 
0                      Kimi no Na wa.
1    Fullmetal Alchemist: Brotherhood
2                            Gintama°
3                         Steins;Gate
4                       Gintama&#039;
Name: name, dtype: object
```

# Evaluation: 

Dalam tahap ini, kita akan melakukan evaluasi terhadap solusi rekomendasi yang telah dibangun menggunakan metrik evaluasi yang sesuai dengan konteks data, permasalahan, dan solusi yang diinginkan. 

## Evaluasi Content-based Filtering

Dalam evaluasi Content-Based Filtering digunakan metrix evaluasi precision. "Precision" mengacu pada salah satu metrik evaluasi yang digunakan untuk mengukur sejauh mana sistem rekomendasi dapat memberikan rekomendasi yang relevan dan tepat kepada pengguna.

Precision dihitung dengan membagi jumlah item yang relevan dan dianggap tepat (misalnya, item yang disukai atau dipilih oleh pengguna) dengan jumlah total item yang direkomendasikan oleh sistem.



**Precision = Jumlah item yang relevan dan dianggap tepat / Jumlah total item yang direkomendasikan**



Precision memberikan gambaran tentang seberapa akurat sistem rekomendasi dalam memberikan rekomendasi yang sesuai dengan preferensi dan minat pengguna. Semakin tinggi nilai precision, semakin baik sistem rekomendasi dalam memberikan rekomendasi yang relevan dan tepat.



Pada studi kasus, dilakukan percobaan dengan menggunakan anime Naruto, dengan Genre Action, Comedy,  Martial Arts, Shounen, Super Power



Output prediksi:

| Judul                                                    | Genre                                               |
| -------------------------------------------------------- | --------------------------------------------------- |
| Naruto: Shippuuden                                       | Action, Comedy,  Martial Arts, Shounen, Super Power |
| Naruto                                                   | Action, Comedy,  Martial Arts, Shounen, Super Power |
| Boruto: Naruto the  Movie - Naruto ga Hokage ni Natta Hi | Action, Comedy,  Martial Arts, Shounen, Super Power |
| Naruto x UT                                              | Action, Comedy,  Martial Arts, Shounen, Super Power |
| Naruto: Shippuuden  Movie 4 - The Lost Tower             | Action, Comedy,  Martial Arts, Shounen, Super Power |



Dengan menggunakan Rumus :

**Precision = Jumlah item yang relevan dan dianggap tepat / Jumlah total item yang direkomendasikan**

Precision = 5/5 = 100%

Maka dapat disimpulkan bahwa model Collaborative Filtering yang digunakan dalam kode tersebut memberikan hasil presisi yang sangat baik. Presisi sebesar 100% menunjukkan bahwa semua rekomendasi yang diberikan oleh model sesuai dengan preferensi pengguna atau rating yang sebenarnya. Namun hal ini dapat dipengaruhi oleh genre yang digunakan, dikarekan anime naruto memiliki genre yang spesifik, disertai dengan jumllah Top-N yang rendah, sehingga menghasilkan presisi yang cukup tinggi. 



## Evaluasi Collaborative Filtering

RMSE (Root Mean Squared Error) adalah metrik evaluasi yang umum digunakan dalam Collaborative Filtering untuk mengukur sejauh mana prediksi model mendekati nilai rating yang sebenarnya.

RMSE menghitung perbedaan antara nilai rating yang diprediksi oleh model dan nilai rating yang sebenarnya dalam dataset. Perbedaan ini kemudian dihitung dengan mengkuadratkan masing-masing selisih, kemudian diambil akar kuadrat dari rata-rata selisih kuadrat tersebut.



**RMSE = sqrt((1/n) * Σ(y_pred - y_actual)^2)**

Di mana:

- RMSE adalah nilai Root Mean Squared Error yang ingin dihitung.
- n adalah jumlah sampel atau data.
- y_pred adalah nilai prediksi yang dihasilkan oleh model.
- y_actual adalah nilai yang sebenarnya atau nilai yang tercatat dalam dataset.



RMSE memberikan gambaran tentang seberapa akurat model Collaborative Filtering dalam memprediksi rating. Semakin rendah nilai RMSE, semakin baik performa model dalam memprediksi rating. Dengan demikian, RMSE digunakan untuk membandingkan kinerja model Collaborative Filtering yang berbeda dan membantu dalam pemilihan model terbaik.



Output RMSE:

```
RMSE for Collaborative Filtering: 3.6229269934681265
```


Berdasarkan nilai RMSE for Collaborative Filtering yang diperoleh sebesar 3.6229269934681265, dapat dijelaskan bahwa rata-rata selisih antara prediksi rating dan nilai rating sebenarnya dalam dataset adalah sekitar 3.62. Semakin rendah nilai RMSE, semakin baik performa model Collaborative Filtering dalam memprediksi rating.

Dalam konteks ini, RMSE yang diperoleh menunjukkan bahwa ada variasi yang signifikan antara prediksi rating oleh model dan nilai rating sebenarnya. Artinya, model Collaborative Filtering yang digunakan masih memiliki tingkat kesalahan yang relatif tinggi dalam memprediksi preferensi pengguna, hal ini dapat terjadi karena terbatasnya jumlah dataset yang digunakan sebagai dataset, dikarenakan keterbatasan hardware.

Untuk meningkatkan kinerja model Collaborative Filtering, beberapa saran yang dapat dipertimbangkan adalah:

1. Memperluas dataset: Dalam kasus Collaborative Filtering, memiliki dataset yang lebih besar dan lebih representatif dapat membantu meningkatkan kinerja model. Hal ini dapat mencakup lebih banyak data pengguna dan lebih banyak rating untuk anime yang ada.
2. Menggunakan teknik pemrosesan data yang lebih canggih: Terdapat beberapa teknik yang dapat diterapkan dalam Collaborative Filtering, seperti normalisasi rating, penanganan missing value, atau penggunaan metode perbaikan data lainnya. Menerapkan teknik-teknik ini dapat membantu mengurangi kesalahan dan meningkatkan akurasi prediksi.
3. Mengeksplorasi metode Collaborative Filtering yang lebih canggih: Ada beberapa variasi dan perbaikan pada metode Collaborative Filtering, seperti metode berbasis model (model-based) seperti Singular Value Decomposition (SVD) atau Factorization Machines (FM). Mengeksplorasi metode ini dapat memberikan solusi yang lebih baik dalam memprediksi preferensi pengguna.
4. Evaluasi dan pemilihan parameter yang tepat: Melakukan evaluasi dan pemilihan parameter yang cermat untuk model Collaborative Filtering juga penting. Hal ini meliputi pemilihan metrik evaluasi yang tepat, tuning parameter, dan menggunakan teknik validasi silang untuk memastikan model memiliki kinerja yang baik.



### Referensi:

1. Dataset Anime Recommendations Database di Kaggle: https://www.kaggle.com/CooperUnion/anime-recommendations-database
2. Hu, Y., Koren, Y., & Volinsky, C. (2008). Collaborative Filtering for Implicit Feedback Datasets. Proceedings of the 2008 Eighth IEEE International Conference on Data Mining.
3. Pazzani, M. J., & Billsus, D. (2007). Content-based Recommendation Systems. The Adaptive Web, 325-341.

