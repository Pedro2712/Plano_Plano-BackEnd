# Generated by Django 4.0.4 on 2022-06-27 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('terrenos', '0004_terreno_numandarnr_terreno_andarnr_terreno_andares_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='terreno',
            name='ca',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='terreno',
            name='eficiencia',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]