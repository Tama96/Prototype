# Generated by Django 2.2.9 on 2020-10-15 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mahasiswa', '0002_auto_20201014_0320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pkl',
            name='reject',
            field=models.BooleanField(default=True),
        ),
    ]
