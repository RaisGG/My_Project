![satu](https://github.com/RaisGG/Company_Bankruptcy_Prediction/blob/main/Bnkcrupt.jpg)

## Domain Proyek

Istilah bangkrut atau pailit dinyatakan sebagai ketidakmampuan suatu perusahaan untuk membayar utang-utangnya kepada para krediturnya. Mengetahui kemungkinan kebangkutan perusahaan merupakan hal yang penting bagi pengurus perusahaan, investor perusahaan dan bahkan masyarakat. Oleh karena itu, kita harus dapat melakukan prediksi kemungkinan kebangkrutan suatu perusahaan sebelum perusahaan itu benar-benar bangkrut. Oleh karena itu, harus dapat dikembangkan suatu model yang tepat untuk dapat melakukan prediksi kebangkrutan perusahaan. Dengan ini, saya mencoba untuk mengembangkan model algoritma machine learning yang dapt melakukan prediksi apakah perusahaan tersebut berpotensi bangkrut atau tidak dengan laporan keuangan dan rasio keuangannya.

## Business Understanding

Menjaga stabilitas suatu perusahaan adalah hal yang sangat penting untuk kelangsungan suatu perusahaan. Perusahaan dengan rasio keuangan yang stabil akan menjaga perusahaan tersebut tetap bertahan. Semakin baik laporan keuangan dan rasio keuangan kas sebuah perusahaan, semakin baik pula stabilitas suatu perusahaan. Sehingga menjaga rasio keuangan perusahaan adalah yang yang harus dilakukan. Bahkan banyak sekali perushaan yang harus melakukan utang untuk dapat menjaga eksistensi perusahaan.

Kebangkrutan atau ketidakmampuan suatu perusahaan untuk membayar utang-utangnya kepada para krediturnya, merupakan hal yang paling ditakuti oleh perusahaan. Ketika suatu perusahaan telah dinyatakan bangkrut dan tidak dapat membayar utang-utangnya, akan sangat sulit bagi perusahaan tersebut untuk bangkit Kembali. Sehingga penanggulangan kebangkrutan adalah hal yang mutlak dilakukan oleh perusahaan. Pada penelitian kali ini, kita akan mengunakan machine learning untuk melakukan prediksi kebangkrutan suatu perusahaan, sehingga dapat mengantisinya sedini mungkin.


### Problem Statements
Bagaimana kemungkinan kebangkrutan perushaan dengan dengan laporan keuangan dan rasio keuangannya?  

### Goals

Membuat model machine learning yang dapat memprediksi kebangkrutan perusahaan dengan menggunakan fitur yang disediakan sehingga mendapatkan informasi yang lebih jelas tentang masa depan perusahaan.

### Solution statements

Untuk prediksi ini, 3 algoritma machine learning yang berbeda akan digunakan dalam studi kasus ini. Algoritma yang digunakan adalah sebagai berikut:

1. Logistic regression: Ini adalah metode klasifikasi pembelajaran mesin dan mencoba memprediksi variabel dependen kategoris yang dikodekan sebagai biner (1 – yes, berhasil dll., 0 – no, tidak berhasil, dll.). 

2. Support Vector Machine (SVM): Support Vector Machine (SVM) merupakan salah satu metode dalam supervised learning yang biasanya digunakan untuk klasifikasi (seperti Support Vector Classification) dan regresi (Support Vector Regression). Dalam pemodelan klasifikasi, SVM memiliki konsep yang lebih matang dan lebih jelas secara matematis dibandingkan dengan teknik-teknik klasifikasi lainnya. SVM juga dapat mengatasi masalah klasifikasi dan regresi dengan linear maupun non linear.

3. Random Forest: Random Forest adalah salah satu metode berbasis klasifikasi dan regresi dimana terdapat proses agregasi decision tree. Oleh karena itu, prinsip dasar random forest mirip dengan decision tree. Masing-masing decision tree akan menghasilkan output yang bisa saja berbeda-beda. Nah, random forest ini akan melakukan voting untuk menentukan hasil mayoritas dari semua decision tree. Bedanya, random forest akan memberikan output berupa mayoritas hasil dari semua decision tree. Algoritma ini memberikan akurasi yang bagus dalam klasifikasi, dapat menangani data training yang jumlahnya besar, dan juga efektif untuk mengatasi data yang tidak lengkap.



Source
Deron Liang and Chih-Fong Tsai, deronliang '@' gmail.com; cftsai '@' mgt.ncu.edu.tw, National Central University, Taiwan.
The data was obtained from 
[UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Taiwanese+Bankruptcy+Prediction/)

Relevant Papers
[Liang, D., Lu, C.-C., Tsai, C.-F., and Shih, G.-A. (2016) Financial Ratios and Corporate Governance Indicators in Bankruptcy Prediction: A Comprehensive Study. European Journal of Operational Research, vol. 252, no. 2, pp. 561-572.] (https://www.sciencedirect.com/science/article/pii/S0377221716000412)
