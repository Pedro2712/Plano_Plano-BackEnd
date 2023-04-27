# Generated by Django 4.0.4 on 2023-04-08 01:07

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('terrenos', '0020_alter_terreno_codigo_alter_terreno_coef_aprov_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='terreno',
            name='codigo',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='terreno',
            name='coef_aprov',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='terreno',
            name='eficiencia',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='terreno',
            name='fachada_ativa',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='terreno',
            name='garagem',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='terreno',
            name='gestor',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='terreno',
            name='metragem',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='terreno',
            name='nomeTerreno',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='terreno',
            name='numVagas',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='terreno',
            name='operacao_urbana',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='terreno',
            name='publico',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='terreno',
            name='qnt_andares_Garagem',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='terreno',
            name='qnt_andares_torre',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), null=True, size=None),
        ),
        migrations.AlterField(
            model_name='terreno',
            name='qnt_apartamentos_andar',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), null=True, size=None),
        ),
        migrations.AlterField(
            model_name='terreno',
            name='qnt_torres_tipo',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), null=True, size=None),
        ),
        migrations.AlterField(
            model_name='terreno',
            name='quantTorre',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='terreno',
            name='tipo_torre',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), null=True, size=None),
        ),
        migrations.AlterField(
            model_name='terreno',
            name='tipo_vaga',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='terreno',
            name='zoneamento',
            field=models.CharField(max_length=200, null=True),
        ),
    ]