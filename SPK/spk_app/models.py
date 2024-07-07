from django import forms
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    jk = models.CharField(max_length=20)
    alamat = models.TextField()
    nim = models.CharField(max_length=20)
    prodi = models.CharField(max_length=100)
    semester = models.CharField(max_length=10)  
    nomor_hp = models.CharField(max_length=13)

    def formatted_username(self):
        return self.username.replace('_', ' ')

class Jadwal(models.Model):
    tanggal = models.DateField()
    waktu = models.TimeField()
    link_tes = models.CharField(max_length=100)
    status = models.BooleanField()

class Alternatif(models.Model):
    simbol = models.CharField(max_length=10)
    nama = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.simbol


class Kriteria(models.Model):
    nama = models.CharField(max_length=100)
    gap = models.IntegerField(default=0)
    factor = models.CharField(max_length=100, default='CF & SF')
    persentase = models.FloatField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nama

class SubKriteria(models.Model):
    kriteria = models.ForeignKey(Kriteria, on_delete=models.CASCADE, related_name='subkriteria')
    nama_sub = models.CharField(max_length=100)
    nilai = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return str(self.nilai)

class Bobot(models.Model):
    selisih = models.IntegerField()
    bobot = models.IntegerField()
    nilai = models.FloatField()
    keterangan = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.keterangan
    
class Penilaian(models.Model):
    alternatif = models.ForeignKey(Alternatif, on_delete=models.CASCADE)
    kriteria1 = models.ForeignKey(SubKriteria, related_name='kriteria1', on_delete=models.CASCADE)
    kriteria2 = models.ForeignKey(SubKriteria, related_name='kriteria2', on_delete=models.CASCADE)
    kriteria3 = models.ForeignKey(SubKriteria, related_name='kriteria3', on_delete=models.CASCADE)
    kriteria4 = models.ForeignKey(SubKriteria, related_name='kriteria4', on_delete=models.CASCADE)
    
class PenilaianGap(models.Model):
    alternatif = models.ForeignKey(Alternatif, on_delete=models.CASCADE)
    kriteria1 = models.IntegerField()
    kriteria2 = models.IntegerField()
    kriteria3 = models.IntegerField()
    kriteria4 = models.IntegerField()

class PenilaianRangking(models.Model):
    alternatif = models.ForeignKey(Alternatif, on_delete=models.CASCADE)
    kriteria1 = models.FloatField()
    kriteria2 = models.FloatField()
    kriteria3 = models.FloatField()
    kriteria4 = models.FloatField()

class PenilaianHasil(models.Model):
    alternatif = models.ForeignKey(Alternatif, on_delete=models.CASCADE)
    ncf = models.FloatField()
    nsf = models.FloatField()
    hasil = models.FloatField()
    
