from django.forms import ModelForm
from bootstrap_datepicker_plus import DatePickerInput
from countable_field.widgets import CountableWidget
from crispy_forms.helper import FormHelper
from django.core.exceptions import ValidationError
from django.core import validators
from mitra.models import Mitra

from . import models

class PklForm(ModelForm):

    class Meta:
        model = models.Pkl
        exclude = ['owner', 'approve']
        widgets = {
            'tanggal_mulai': DatePickerInput(options={'debug': True}).start_of('event active dtime'),
            'tanggal_selesai': DatePickerInput().end_of('event active dtime'),
            #'catatan': CountableWidget(attrs={'data-count': 'characters','data-max-count': 1500, 'data-count-direction': 'down'}),                                            
        }
    def present_or_future_date(value):
        if value < datetime.date.today():
            raise forms.ValidationError("Tanggal mulai tidak boleh kurang dari hari ini!!! BLOG!!")
        return value

class RejectForm(ModelForm):
    class Meta:
        model = models.Reject
        fields = ['catatan', 'reject']
        widgets = {
            'catatan': CountableWidget(attrs={'data-count': 'characters','data-max-count': 1500, 'data-count-direction': 'down'}),               
        }
