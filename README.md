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
Berdasarkan analisis data peminjaman sepeda selama periode 2011-2012, berikut adalah beberapa kesimpulan utama:  

1. **Hari dengan Peminjaman Sepeda Tertinggi**  
   Jumlah rata-rata peminjaman sepeda tertinggi terjadi pada **hari Jumat** dengan rata-rata **196,44 peminjaman per hari**, diikuti oleh Sabtu. Aktivitas ini mencerminkan penggunaan sepeda baik untuk perjalanan kerja di hari kerja maupun rekreasi pada akhir pekan.

2. **Pengaruh Musim terhadap Peminjaman Sepeda**  
   **Musim gugur (Fall)** mencatat total peminjaman sepeda tertinggi (1,061,129 peminjaman), sementara **musim semi (Spring)** memiliki jumlah peminjaman terendah (471,348 peminjaman). Hal ini menunjukkan bahwa kondisi cuaca pada musim gugur lebih mendukung aktivitas bersepeda dibandingkan musim lainnya.  

3. **Pelanggan Terdaftar Mendominasi**  
   Berdasarkan data, **81,2% peminjaman dilakukan oleh pelanggan terdaftar (registered)**, sedangkan hanya **18,8% berasal dari pelanggan tidak terdaftar (casual)**. Proporsi ini tergambar jelas **melalui diagram pie yang menunjukkan dominasi pelanggan terdaftar**. Hal ini mencerminkan loyalitas yang tinggi dari pelanggan terdaftar, namun juga menunjukkan adanya peluang besar untuk meningkatkan jumlah pelanggan casual.

## Rekomendasi

1. **Tingkatkan Pelanggan Casual**: Fokuskan kampanye pemasaran untuk menarik pelanggan casual dengan promosi akhir pekan dan kemudahan registrasi.

2. **Optimalisasi Jam Puncak**: Tambahkan sepeda di stasiun yang ramai pada pukul 08.00 pagi dan 17.00-18.00 sore, serta pertimbangkan layanan pengantaran sepeda.

3. **Promosi Musim Gugur**: Tawarkan paket spesial musim gugur untuk meningkatkan peminjaman selama periode ini.

4. **Program Loyalitas untuk Pelanggan Terdaftar**: Berikan insentif kepada pelanggan terdaftar dengan potongan harga dan akses sepeda premium.

5. **Edukasi Keuntungan Bersepeda**: Jalankan kampanye edukasi tentang manfaat bersepeda untuk kesehatan dan lingkungan.

6. **Event Komunitas**: Selenggarakan event bersepeda untuk memperkenalkan layanan dan menarik lebih banyak pelanggan.

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