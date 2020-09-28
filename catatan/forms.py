from django.forms import ModelForm
from django.forms import ClearableFileInput
from countable_field.widgets import CountableWidget
from crispy_forms.helper import FormHelper
from . import models

class CatatanForm(ModelForm):
    class Meta :
        model = models.Catatan
        exclude=['owner']
        widgets = {
            'judul': CountableWidget(attrs={'data-min-count': 10,'data-max-count': 200}),         
            'ket': CountableWidget(attrs={'data-min-count': 100,'data-max-count': 200}),                                            
        }
       
class GambarForm(ModelForm):
    class Meta :
        model = models.Gambar
        fields = ['upload_img']
        widgets = {
            'upload_img': ClearableFileInput(attrs={'multiple': True}),
        }
