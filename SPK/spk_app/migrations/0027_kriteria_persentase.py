# Generated by Django 5.0.3 on 2024-04-21 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spk_app', '0026_penilaianhasil'),
    ]

    operations = [
        migrations.AddField(
            model_name='kriteria',
            name='persentase',
            field=models.FloatField(default=0),
        ),
    ]
