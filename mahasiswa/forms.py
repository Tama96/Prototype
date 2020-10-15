from django.forms import ModelForm
from bootstrap_datepicker_plus import DatePickerInput
from countable_field.widgets import CountableWidget
from crispy_forms.helper import FormHelper
from mitra.models import Mitra

from . import models

class PklForm(ModelForm):
    class Meta:
        model = models.Pkl
        exclude = ['owner', 'approve', 'catatan', 'reject']
        widgets = {
            'tanggal_mulai': DatePickerInput(options={'debug': True}).start_of('event active dtime'),
            'tanggal_selesai': DatePickerInput().end_of('event active dtime'),
            # 'catatan': CountableWidget(attrs={'data-count': 'characters','data-max-count': 1500, 'data-count-direction': 'down'}),                                            
        }
 
class RejectForm(ModelForm):
    class Meta:
        model = models.Pkl
        exclude = ['owner', 'judul', 'nama_mitra', 'dosen', 'tanggal_mulai', 'tanggal_selesai', 'approve']
        widgets = {
            'catatan': CountableWidget(attrs={'data-count': 'characters','data-max-count': 1500, 'data-count-direction': 'down'}),               
        }
