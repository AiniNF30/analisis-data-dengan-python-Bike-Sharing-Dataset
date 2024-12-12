# Analisis Proyek Bike Sharing Dataset (2011-2012)
## Statistik Peminjaman Sepeda
- **Casual Customer**: Meski jumlahnya lebih sedikit dibandingkan peminjam terdaftar, ada kebutuhan untuk memperluas pemasaran bisnis untuk menarik perhatian peminjam baru.
- **Registered Customer**: Jumlah peminjam sepeda yang sudah terdaftar jauh lebih banyak dibandingkan peminjam biasa.
  
## Hasil Analisis Kondisi Peminjaman Sepeda
Hasil analisis menunjukkan bahwa situasi dan kondisi dengan total peminjaman sepeda tertinggi dalam dua tahun terakhir adalah sebagai berikut:
- **Musim gugur** mencatat total peminjaman sepeda tertinggi dibandingkan dengan tiga musim lainnya.
- **Hari kerja (Senin hingga Jumat)** memiliki jumlah peminjam lebih tinggi dibandingkan akhir pekan. Namun, pada **hari Sabtu dan Minggu**, peminjaman sepeda cukup ramai antara pukul 12.00 hingga 15.00 siang.  
- **Waktu puncak peminjaman** terjadi pada pukul 08.00 pagi dan pukul 17.00 hingga 18.00 sore.

## Conclusion
Berdasarkan analisis data peminjaman sepeda selama periode 2011-2012, berikut adalah kesimpulan utama yang dapat diambil:  

1. **Pelanggan Terdaftar Mendominasi**  
   Jumlah pelanggan terdaftar jauh lebih banyak dibandingkan pelanggan biasa (casual). Strategi pemasaran yang lebih agresif diperlukan untuk menarik pelanggan baru, khususnya dari kategori casual.

2. **Pengaruh Musim**  
   Musim gugur mencatatkan jumlah peminjaman sepeda tertinggi, menunjukkan bahwa kondisi cuaca dan suhu di musim ini sangat mendukung aktivitas bersepeda. Hal ini dapat dimanfaatkan untuk promosi musiman.

3. **Tren Pemakaian Berdasarkan Hari**  
   - **Hari Kerja**: Aktivitas peminjaman cenderung lebih tinggi pada pagi hari (sekitar pukul 08.00) dan sore hari (antara pukul 17.00-18.00). Ini mencerminkan pola penggunaan sepeda untuk perjalanan ke dan dari tempat kerja.  
   - **Akhir Pekan**: Pada hari Sabtu dan Minggu, peminjaman lebih ramai di siang hari (antara pukul 12.00-15.00), mengindikasikan penggunaan sepeda untuk rekreasi.

4. **Rekomendasi Strategi Bisnis**  
   - Memperluas layanan selama jam-jam puncak, terutama di pagi dan sore hari pada hari kerja.  
   - Mengoptimalkan promosi akhir pekan untuk menarik pelanggan casual.  
   - Mengadakan kampanye pemasaran khusus di musim gugur untuk memaksimalkan potensi penggunaan sepeda pada musim tersebut.  
   - Menawarkan insentif kepada pelanggan casual agar tertarik untuk mendaftar sebagai pelanggan tetap.

Strategi-strategi ini dapat membantu meningkatkan total peminjaman sepeda, memperluas basis pelanggan, serta memaksimalkan penggunaan aset yang tersedia.


# Dashboard Bike Sharing Dataset (2011-2012)

Untuk menjalankan dashboard ini di _local_ ada beberapa langkah yang perlu dilakukan

## Instal Dependencies
Untuk menginstall dependencies, anda dapat menjalankan code ini

### Anaconda

```
conda create --name main-ds python=3.11.9
conda activate main-ds
pip install -r requirements.txt
```

### Shell/Terminal

```
mkdir proyek_analisis_data
cd proyek_analisis_data
pipenv install
pipenv shell
pip install -r requirements.txt
```

## Run Dashboard di Local

```
cd dashboard
streamlit run main.py
```