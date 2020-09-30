from django.forms import ModelForm
from bootstrap_datepicker_plus import DatePickerInput
from countable_field.widgets import CountableWidget
from crispy_forms.helper import FormHelper

from mitra.models import Mitra

from . import models

class PklForm(ModelForm):

    class Meta:
        model = models.Pkl
        exclude = ['owner', 'approve']
        widgets = {
            'tanggal_mulai': DatePickerInput(),
            'tanggal_selesai': DatePickerInput(),
            #'catatan': CountableWidget(attrs={'data-count': 'characters','data-max-count': 1500, 'data-count-direction': 'down'}),                                            
        }

class CatatanForm(ModelForm):
    class Meta:
        model = models.Catatan
        fields = ['catatan', 'reject']
        widgets = {
            'catatan': CountableWidget(attrs={'data-count': 'characters','data-max-count': 1500, 'data-count-direction': 'down'}),               
        }
