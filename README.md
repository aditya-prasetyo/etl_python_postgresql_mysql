# Dokumentasi *ETL Development* Menggunakan Python

## Alur Kerja ETL

Langkah-langkah yang dilalui dalam ETL ini, sebagai berikut:

1. Mendefinisikan tabel-tabel di database SOURCE, jika sudah ada maka diabaikan
2. Mengambil semua nama tabel
3. Tiap tabel melakukan Proses sebagai berikut:
    
    3.1. Mengecek max_createdAt dari data yang telah berumur N_
    3