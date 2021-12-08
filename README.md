# Binary Classification Using KNN

Badan Penyelenggara Jaminan Sosial Kesehatan atau BPJS Kesehatan merupakan layanan kesehatan sosial yang berfungsi dalam memberikan jaminan kesehatan. Program ini merupakan program pemerintah yang berada dalam kesatuan bersama dengan JKN dan mulai beroperasi sejak 1 Januari 2014. Namun, terdapat permasalahan dimana pendapatan BPJS Kesehatan mengalami defisit. Salah satu dugaan penyebab terjadinya defisit pendapatan tersebut adalah dikarenakan beberapa peserta  memalsukan status kepesertaannya, seperti adanya masyarakat yang bukan anggota BPJS Kesehatan, menggunakan layanan rumah sakit dengan memanfaatkan kartu orang lain yang merupakan anggota BPJS Kesehatan. Selain itu, terdapat juga dugaan masalah dimana terjadinya manipulasi terhadap klaim dalam pelayanan rumah sakit yang dilakukan oleh anggota BPJS Kesehatan. Dalam mengatasi permasalahan yang dialami oleh BPJS Kesehatan, maka dilakukan prediksi terhadap fraud untuk klaim dalam Rumah Sakit. Analisis dilakukan dengan memanfaatkan algoritma klasifikasi supervised learning, yaitu K-Nearest Neighbors

### Pendekatan yang diajukan
1. Business Understanding

Business Understanding merupakan tahapan yang bertujuan untuk menentukan tujuan dan persyaratan dengan jelas secara keseluruhan, menerjemahkan tujuan tersebut serta menentukan pembatasan dalam perumusan masalah data mining, dan selanjutnya mempersiapkan strategi awal untuk mencapai tujuan tersebut.

2. Data Understanding 

Data Understanding bertujuan untuk memeriksa data yang terdapat dalam dataset yang digunakan. Data set yang digunakan akan divisualisasikan menggunakan histogram dan  heat map.

3. Data Preparation 

Data Preparation bertujan untuk memperbaiki masalah dalam data, kemudian membuat variabel derived. Pada data preparation terdapat beberapa proses yang dilakukan yaitu:
    - **Feature Selection** yaitu melakukan eliminasi terhadap features yang memiliki nilai unique values=1
    - **Transformasi** menggunakan One Hot Encoding, Standarisasin Binning
    - **Split data** yaitu dengan membagikan data kedalam dua bagian yaiu train=80% dan test=20%.

4. Modelling

Pada tahapan ini melakukan pemodelan dengan menggunakan K-Nearest Neighbour, dimana terlebih dahulu melakukan Select K-best yaiut menemukan nilai K optimal untuk mendapatkan yang terbaik.

5. Evaluation

Pada tahap ini melakukan evaluasi terhadap model yang telah dikembangkan dengan menggunakan confusion matrix yang terdiri dari Precision, Recall, dan F-Score.

6. Deployment

Pada tahap ini melakukan deployment terhadap model yang telah dikembangkan, dimana menggunakan flask dalam pengembang web. https://bpjsfrauddetection.herokuapp.com/

![step](https://user-images.githubusercontent.com/60679474/145212565-bcba5f03-e253-4d15-b9c0-3e7a7b7ae980.png)


##### Team & Anggota
Kelompok: 03
Anggota:
1. 12S18005 – Lusiana Ros Romantika Siahaan
2. 12S18042 – Indah Oktavia M. Sibarani
3. 12S18067 – Grace Vidia Rosa Panjaitan
