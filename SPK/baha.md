### Tahapan Perhitungan dengan Metode Profile Matching

Mari kita bahas tahapan perhitungan dengan metode Profile Matching lebih detail menggunakan contoh kasus yang sama.

#### Contoh Kasus
Posisi yang dinilai: Manajer Proyek
Kriteria yang digunakan:
1. Pendidikan
2. Pengalaman kerja
3. Keterampilan manajerial
4. Kemampuan komunikasi

Bobot untuk masing-masing kriteria:
1. Pendidikan: 20%
2. Pengalaman kerja: 30%
3. Keterampilan manajerial: 30%
4. Kemampuan komunikasi: 20%

Profil ideal:
1. Pendidikan: S2
2. Pengalaman kerja: 5 tahun
3. Keterampilan manajerial: Sangat Baik
4. Kemampuan komunikasi: Baik

Nilai gap dan skornya:
- Gap 0: Skor 5
- Gap 1: Skor 4
- Gap 2: Skor 3
- Gap 3: Skor 2
- Gap 4: Skor 1

#### Profil Kandidat
**Kandidat A:**
1. Pendidikan: S1 (gap 1)
2. Pengalaman kerja: 4 tahun (gap 1)
3. Keterampilan manajerial: Baik (gap 1)
4. Kemampuan komunikasi: Baik (gap 0)

**Kandidat B:**
1. Pendidikan: S2 (gap 0)
2. Pengalaman kerja: 6 tahun (gap 1)
3. Keterampilan manajerial: Sangat Baik (gap 0)
4. Kemampuan komunikasi: Cukup (gap 2)

### Tahap Perhitungan

1. **Hitung Gap:**
   - Gap dihitung dengan mengurangi nilai profil kandidat dari nilai profil ideal.

**Kandidat A:**
1. Pendidikan: Ideal (S2) - Kandidat (S1) = 1
2. Pengalaman kerja: Ideal (5 tahun) - Kandidat (4 tahun) = 1
3. Keterampilan manajerial: Ideal (Sangat Baik) - Kandidat (Baik) = 1
4. Kemampuan komunikasi: Ideal (Baik) - Kandidat (Baik) = 0

**Kandidat B:**
1. Pendidikan: Ideal (S2) - Kandidat (S2) = 0
2. Pengalaman kerja: Ideal (5 tahun) - Kandidat (6 tahun) = 1
3. Keterampilan manajerial: Ideal (Sangat Baik) - Kandidat (Sangat Baik) = 0
4. Kemampuan komunikasi: Ideal (Baik) - Kandidat (Cukup) = 2

2. **Pemberian Skor:**
   - Skor diberikan berdasarkan gap yang telah dihitung.

**Kandidat A:**
1. Pendidikan: Gap 1 -> Skor 4
2. Pengalaman kerja: Gap 1 -> Skor 4
3. Keterampilan manajerial: Gap 1 -> Skor 4
4. Kemampuan komunikasi: Gap 0 -> Skor 5

**Kandidat B:**
1. Pendidikan: Gap 0 -> Skor 5
2. Pengalaman kerja: Gap 1 -> Skor 4
3. Keterampilan manajerial: Gap 0 -> Skor 5
4. Kemampuan komunikasi: Gap 2 -> Skor 3

3. **Normalisasi dan Penilaian Akhir:**
   - Hitung total skor berdasarkan bobot kriteria.

**Kandidat A:**
1. Pendidikan: Skor 4 * 20% = 0.8
2. Pengalaman kerja: Skor 4 * 30% = 1.2
3. Keterampilan manajerial: Skor 4 * 30% = 1.2
4. Kemampuan komunikasi: Skor 5 * 20% = 1.0

Total Skor = 0.8 + 1.2 + 1.2 + 1.0 = 4.2

**Kandidat B:**
1. Pendidikan: Skor 5 * 20% = 1.0
2. Pengalaman kerja: Skor 4 * 30% = 1.2
3. Keterampilan manajerial: Skor 5 * 30% = 1.5
4. Kemampuan komunikasi: Skor 3 * 20% = 0.6

Total Skor = 1.0 + 1.2 + 1.5 + 0.6 = 4.3

### Kesimpulan

Dari hasil perhitungan, Kandidat B memiliki skor total 4.3, lebih tinggi dibandingkan dengan Kandidat A yang memiliki skor total 4.2. Oleh karena itu, Kandidat B dianggap lebih cocok untuk posisi manajer proyek berdasarkan metode profile matching.

### Diagram Alur Perhitungan

Berikut adalah alur perhitungan dengan metode Profile Matching:

1. **Identifikasi Kriteria dan Bobot:**
   - Tentukan kriteria yang relevan dan bobotnya.
   
2. **Profil Ideal:**
   - Tentukan profil ideal untuk masing-masing kriteria.
   
3. **Gap Analysis:**
   - Hitung gap antara profil ideal dan profil kandidat.
   
4. **Skor Gap:**
   - Berikan skor berdasarkan nilai gap.

5. **Total Skor:**
   - Hitung total skor dengan memperhatikan bobot kriteria.

6. **Pengambilan Keputusan:**
   - Pilih kandidat dengan skor tertinggi sebagai yang paling sesuai dengan profil ideal.

Metode ini memberikan cara yang terstruktur dan objektif untuk menilai kesesuaian kandidat dengan profil yang diinginkan, membantu pengambil keputusan dalam memilih kandidat yang terbaik.