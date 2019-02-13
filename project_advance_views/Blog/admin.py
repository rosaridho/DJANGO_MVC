from django.contrib import admin
from .models import Artikel

# Register your models here.
my_model = [Artikel]
admin.site.register(my_model)