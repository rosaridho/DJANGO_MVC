from django import forms
from .models import Menteebase

class PostForm(forms.ModelForm):

    class Meta:
        model = Menteebase
        fields = ('nama', 'pesan', 'profilePict')