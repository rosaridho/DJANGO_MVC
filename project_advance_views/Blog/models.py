from django.db import models
from django.db.models import CharField
from django.db.models import TextField
from datetime import datetime
from django.utils import timezone

# Create your models here.
class Artikel(models.Model):
    title = models.CharField(max_length = 100)
    isi = models.TextField(max_length = 1024)
    tanggal = models.DateTimeField(default = timezone.now)
    jumlahComment = models.CharField(max_length = 100)
    gambar = models.ImageField(upload_to='img')

    def __str__(self):
        return self.title