from django import forms
from .models import Artikel

class PostForm(forms.ModelForm):

    class Meta:
        model = Artikel
        fields = ('title', 'isi', 'tanggal', 'jumlahComment', 'gambar', 'linkComment')