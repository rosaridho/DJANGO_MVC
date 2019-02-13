from django import forms
from .models import Mentorbase

class PostForm(forms.ModelForm):

    class Meta:
        model = Mentorbase
        fields = ('nama', 'pesan', 'profilePict', 'wokingExp', 'jobPosition')