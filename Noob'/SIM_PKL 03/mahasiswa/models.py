from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.core.files import File
from django.conf import settings
from mitra.models import Mitra
from django.db import IntegrityError

class Pkl(models.Model):
    owner = models.ForeignKey(User, on_delete = models.DO_NOTHING,related_name='mahasiswa', null=True, blank=True)
    judul = models.CharField(max_length=255)
    nama_mitra = models.ForeignKey(Mitra, on_delete = models.DO_NOTHING)
    dosen = models.CharField(max_length=255, default='')
    tanggal_mulai = models.DateField(default=datetime.now)
    tanggal_selesai = models.DateField(default=datetime.now,null = True)
    approve = models.BooleanField(default=False)
    catatan = models.TextField(max_length=1500, help_text="maksimal 1500 karakter")
    reject = models.BooleanField(default=False)

    def tanggal_selesai_format(self):
        return self.tanggal_selesai.strftime('%Y-%m=%d')
    def tanggal_selesai_format(self):
        return self.tanggal_selesai.strftime('%Y-%m=%d')

# class Reject(models.Model):
#     pkl = models.ForeignKey(Pkl, on_delete = models.CASCADE,related_name='rejection')
#     catatan = models.TextField(max_length=1500, help_text="maksimal 1500 karakter")
#     reject = models.BooleanField(default=True)
#     def __str__(self):
#         return self.catatan 


