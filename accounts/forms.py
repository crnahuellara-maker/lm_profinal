from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'nombre', 'apellido', 'bio', 'fecha_nacimiento']
