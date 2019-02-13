from django.contrib import admin
from .models import Mentorbase

# Register your models here.
my_model = [Mentorbase]
admin.site.register(my_model)
