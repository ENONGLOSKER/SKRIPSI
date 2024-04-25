# Generated by Django 5.0.3 on 2024-04-19 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spk_app', '0017_alter_penilaian_kriteria1_alter_penilaian_kriteria2_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PenilaianGap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alternatif', models.CharField(max_length=255)),
                ('kriteria1', models.FloatField()),
                ('kriteria2', models.FloatField()),
                ('kriteria3', models.FloatField()),
                ('kriteria4', models.FloatField()),
            ],
        ),
    ]
