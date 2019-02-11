from django.db import models
from django.db.models import CharField
from django.db.models import TextField
from datetime import datetime
from django.utils import timezone

# Create your models here.
class Dokter(models.Model):
    nama = models.CharField(max_length = 255)
    nomor_telepon = models.TextField(max_length = 255)
    bidang = models.CharField(max_length = 255)
    jadwal_praktek = models.DateTimeField(default = timezone.now)
    
    def __str__(self):
        return self.nama


class Pasien(models.Model):
    nama = models.CharField(max_length = 255)
    nomor_telepon = models.TextField(max_length = 255)
    alamat = models.CharField(max_length = 255)
    keluhan = models.CharField(max_length = 255)

    def __str__(self):
        return self.nama


class Resep(models.Model):
    nama = models.CharField(max_length = 255)
    total_harga = models.TextField(max_length = 255)
    kumpulan_obat = models.CharField(max_length = 255)

    def __str__(self):
        return self.nama


class Obat(models.Model):
    nama = models.CharField(max_length = 255)
    kandungan = models.CharField(max_length = 255)
    khasiat = models.CharField(max_length = 255)

    def __str__(self):
        return self.nama
