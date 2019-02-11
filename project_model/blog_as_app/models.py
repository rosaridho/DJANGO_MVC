from django.db.models import CharField
from django.db.models import TextField

from datetime import datetime
from django.utils import timezone

from django.db.models import ForeignKey
from django.db.models import CASCADE

from django.db import models

# Create your models here.
class Mentee(models.Model):
    name = models.CharField(max_length = 255)
    full_name = models.TextField(max_length = 255)
    gender = models.CharField(max_length = 255)
    telephone = models.TextField(max_length = 255)
    mobile = models.TextField(max_length = 255)
    address = models.TextField(max_length = 255)
    nick_name = models.CharField(max_length = 50)

    def __str__(self):
        return self.name + '  the phone number is:' + self.mobile

class BlogPost(models.Model):
    created = models.DateTimeField(default = timezone.now)
    updated = models.DateTimeField(default = timezone.now)
    title = models.CharField(max_length = 255)
    content = models.CharField(max_length = 255)
    created_by = models.CharField(max_length = 255)
    posted_by = models.ForeignKey(Mentee, on_delete=models.CASCADE)