from django.forms import ModelForm
from django.forms import ClearableFileInput
from . import models

class CatatanForm(ModelForm):
    class Meta :
        model = models.Catatan
        fields = '__all__'

class GambarForm(ModelForm):
    class Meta :
        model = models.Gambar
        fields = ['gambar']
        widgets = {
            'gambar': ClearableFileInput(attrs={'multiple': True}),
        }
