# Generated by Django 5.0.3 on 2024-04-13 19:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spk_app', '0006_kriteria_subkriteria'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subkriteria',
            name='kriteria',
        ),
    ]
