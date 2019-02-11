from django.db import models

from django.db.models import CharField
from django.db.models import TextField
from django.db.models import DateField
from django.db.models import TimeField

from django.db.models import ForeignKey
from django.db.models import CASCADE

from datetime import datetime
from django.utils import timezone

# Create your models here.
class Direksi(models.Model):
    nama_lengkap = models.CharField(max_length = 255)
    no_telepon = models.TextField(max_length = 255)
    jabatan = models.CharField(max_length = 255)

    def __str__(self):
        return self.nama_lengkap

class Mentee(models.Model):
    nama_lengkap = models.CharField(max_length = 255)
    no_telepon = models.TextField(max_length = 255)
    nomor_absen = models.TextField(max_length = 255)
    nilai_rata_rata = models.TextField(max_length = 255)

    def __str__(self):
        return self.nama_lengkap

class MataPelajaran(models.Model):
    nama_pelajaran = models.CharField(max_length = 255)
    jadwal_dimulai = models.CharField(max_length = 255)
    jadwal_berakhir = models.CharField(max_length = 255)
    def __str__(self):
        return self.nama_pelajaran


class Mentor(models.Model):
    nama_lengkap = models.CharField(max_length = 255)
    no_telepon = models.TextField(max_length = 255)
    mata_pelajaran = models.ForeignKey(MataPelajaran, on_delete=models.CASCADE)

    def __str__(self):
        return self.nama_lengkap

class Challenge(models.Model):
    nama_challenge = models.CharField(max_length = 255)
    banyak_soal = models.TextField(max_length = 255)
    bobot_nilai = models.TextField(max_length = 255)
    mata_pelajaran = models.ForeignKey(MataPelajaran, on_delete=models.CASCADE)

    def __str__(self):
        return self.nama_challenge

class LiveCode(models.Model):
    nama_live_code = models.CharField(max_length = 255)
    banyak_soal = models.TextField(max_length = 255)
    bobot_nilai = models.TextField(max_length = 255)
    tanggal_pelaksaan = models.DateTimeField(default = timezone.now)
    mata_pelajaran = models.ForeignKey(MataPelajaran, on_delete=models.CASCADE)

    def __str__(self):
        return self.nama_live_code