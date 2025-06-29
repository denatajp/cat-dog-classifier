# Cat vs Dog Classifier - Aplikasi Klasifikasi Gambar dengan AI


## 📝 Deskripsi Proyek
Aplikasi web berbasis AI yang dapat mengklasifikasikan gambar antara kucing dan anjing dengan akurasi tinggi. Dibangun menggunakan Flask untuk backend dan TensorFlow untuk model machine learning, dengan UI yang modern dan responsif.

![image](https://github.com/user-attachments/assets/29aa6014-622e-4a47-bdf0-a2e623942e90)

## ✨ Fitur Utama
- Real-time Classification: Membedakan gambar kucing dan anjing dengan cepat
- UI Modern: Desain responsif yang bekerja di semua device
- Visualisasi Hasil: Menampilkan tingkat confidence dengan grafik yang interaktif
- Drag & Drop Upload: Upload gambar mudah dengan drag and drop

## 🛠️ Apa Yang Digunakan?
- Frontend: HTML5, CSS3, JavaScript
- Backend: Python, Flask
- Machine Learning: TensorFlow, Keras
- Libraries: Pillow, NumPy, Werkzeug

## 🚀 Panduan Instalasi

### Requirements
- Python 3.8 atau lebih baru
- pip (Python package manager)
- virtualenv (direkomendasikan)

### Instalasi
- Clone repository
    ``` bash
    git clone https://github.com/denatajp/cat-dog-classifier.git
    cd cat-dog-classifier
    ```

- Buat dan aktifkan virtual environment
    ``` bash
    python -m venv venv
    venv\Scripts\activate
    ```

- Instal dependencies
    ``` bash
    pip install -r requirements.txt
    ```

- Jalankan Aplikasi
    ``` bash
    python app.py
    ```

- Buka di browser http://localhost:5000 atau http://127.0.0.1:5000/


## 📁 Struktur Proyek
``` bash
cat-dog-classifier/
├── static/
│   ├── uploads/                # Folder penyimpanan gambar sementara
│   └── style.css               # Stylesheet utama
├── templates/
│   └── index.html              # Halaman utama
├── model/                      # Folder untuk model ML
│   └── cat_dog_classifier.h5   # File model (harus disediakan)
├── app.py                      # Flask utama
├── requirements.txt            # Dependencies
└── README.md                   # Dokumentasi
```

## 🤖 Cara Menggunakan
1. Upload gambar kucing atau anjing dengan:
    - Klik tombol "Pilih File"
    - Atau drag and drop gambar ke area yang disediakan
4. Klik tombol "Mulai Klasifikasi"
5. Tunggu proses analisis selesai
6. Lihat hasil prediksi (kucing/anjing) juga confidence level
7. Untuk mencoba gambar lain, klik tombol "Coba Gambar Lain"

## 📦 Model
Aplikasi ini menggunakan pre-trained model `cat_dog_classifier.h5` yang berada di folder model/. Model ini sudah dilatih sebelumnya untuk klasifikasi gambar kucing dan anjing.
