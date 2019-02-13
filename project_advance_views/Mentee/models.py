from django.db import models
from django.db.models import CharField
from django.db.models import TextField
from datetime import datetime
from django.utils import timezone

# Create your models here.
class Menteebase(models.Model):
    nama = models.CharField(max_length = 100)
    pesan = models.TextField(max_length = 1024)
    profilePict = models.ImageField(upload_to='img')

    def __str__(self):
        return self.nama