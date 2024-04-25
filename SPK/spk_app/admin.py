from django.contrib import admin
from .models import CustomUser, Jadwal, Alternatif, Kriteria, SubKriteria, Bobot, Penilaian, PenilaianGap, PenilaianRangking, PenilaianHasil
admin.site.register([CustomUser,Jadwal, Alternatif, Kriteria, SubKriteria,Bobot, Penilaian, PenilaianGap, PenilaianRangking, PenilaianHasil])

