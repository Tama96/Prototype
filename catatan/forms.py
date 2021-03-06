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
            'ket': CountableWidget(attrs={'data-count': 'characters','data-max-count': 500, 'data-count-direction': 'down'}),                                            
        }
    
class GambarForm(ModelForm):
    class Meta :
        model = models.Gambar
        fields = ['upload_img']
        widgets = {
            'upload_img': ClearableFileInput(attrs={'multiple': True}),
        }
