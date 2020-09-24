from django.db import models
from datetime import datetime
from django.core.files import File
from django.conf import settings

import PIL.Image

class Catatan(models.Model):
    tgl_kegiatan = models.DateField(default=datetime.now)
    judul = models.CharField(max_length=100)
    ket = models.TextField(max_length=200)

class Gambar(models.Model):
    gambar = models.ImageField(default='', upload_to='images/', null=False, blank=True)
    catatan = models.ForeignKey(Catatan, on_delete=models.CASCADE, related_name='catatan')

    def save(self,force_insert=False, force_update=False, using=None,*args, **kwargs):
        super(Gambar, self).save(*args, **kwargs)
        if self.gambar:
            gambar = self.gambar
            if gambar.size > 0.3*1024*1024: #jika file yang di upload > 300kb maka akan di compress
                self.compress_image(gambar)
                print(gambar)
    
    def compress_image(self, uploadedImage):
        im = PIL.Image.open("{}/{}".format(settings.MEDIA_ROOT,uploadedImage))
        if im.mode != 'RGB':
            im = im.convert('RGB')
        new_image = im.resize((round(im.size[0]*0.5), round(im.size[1]*0.5)))
        new_image.save("{}/{}".format(settings.MEDIA_ROOT,uploadedImage))
        # self.image = "{}{}".format(settings.MEDIA_ROOT,uploadedImage)
    
    def upload_location(instance, filename, **kwargs):
        file_path = 'images/{filename}'.format(filename=filename)
        return file_path

    def __str__(self):
        return self.gambar.url


