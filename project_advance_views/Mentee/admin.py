from django.contrib import admin
from .models import Menteebase

# Register your models here.
my_model = [Menteebase]
admin.site.register(my_model)