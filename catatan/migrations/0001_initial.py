# Generated by Django 2.0 on 2020-09-28 08:42

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Catatan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tgl_kegiatan', models.DateField(default=datetime.datetime.now)),
                ('judul', models.CharField(max_length=100)),
                ('ket', models.TextField(max_length=200)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='catatan', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Gambar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload_img', models.ImageField(blank=True, default='', upload_to='images/')),
                ('catatan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='catatan', to='catatan.Catatan')),
            ],
        ),
    ]
