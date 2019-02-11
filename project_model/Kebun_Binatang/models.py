from django.db import models
from django.db.models import CharField
from django.db.models import TextField
from datetime import datetime
from django.utils import timezone

# Create your models here.
class Hewan(models.Model):
    nama = models.CharField(max_length = 255)
    species = models.CharField(max_length = 255)
    berat = models.TextField(max_length = 255)
    umur = models.TextField(max_length = 255)

    def __str__(self):
        return self.nama

class Kandang(models.Model):
    nama = models.CharField(max_length = 255)
    isi_kandang = models.CharField(max_length = 255)
    luas_kandang = models.CharField(max_length = 255)

    def __str__(self):
        return self.nama

class Penjaga(models.Model):
    nama = models.CharField(max_length = 255)
    nomor_telepon = models.TextField(max_length = 255)
    jadwal_jaga = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.nama

class Pengunjung(models.Model):
    nama = models.CharField(max_length = 255)
    nomor_telepon = models.TextField(max_length = 255)
    hari_berkunjung = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.nama