# Generated by Django 4.0.4 on 2023-04-07 04:24

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('terrenos', '0011_alter_terreno_qnt_andares_torre_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='terreno',
            name='qnt_andares_torre',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), blank=True, size=None),
        ),
        migrations.AlterField(
            model_name='terreno',
            name='qnt_apartamentos_andar',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), blank=True, size=None),
        ),
        migrations.AlterField(
            model_name='terreno',
            name='qnt_torres_tipo',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), blank=True, size=None),
        ),
        migrations.AlterField(
            model_name='terreno',
            name='tipo_torre',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, size=None),
        ),
    ]
