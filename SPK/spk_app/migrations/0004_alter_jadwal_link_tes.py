# Generated by Django 5.0.3 on 2024-04-12 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spk_app', '0003_jadwal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jadwal',
            name='link_tes',
            field=models.CharField(max_length=100),
        ),
    ]
