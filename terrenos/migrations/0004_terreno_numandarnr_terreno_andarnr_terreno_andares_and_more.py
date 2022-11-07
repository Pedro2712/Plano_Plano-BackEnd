# Generated by Django 4.0.4 on 2022-06-27 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('terrenos', '0003_alter_terreno_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='terreno',
            name='NumAndarNr',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='terreno',
            name='andarNr',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='terreno',
            name='andares',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='terreno',
            name='andaresGaragem',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='terreno',
            name='andaresMall',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='terreno',
            name='codigo',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='terreno',
            name='garagem',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='terreno',
            name='gestor',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='terreno',
            name='metragem',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='terreno',
            name='metragemMall',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='terreno',
            name='nomeTerreno',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='terreno',
            name='numAndar',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='terreno',
            name='numMotos',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='terreno',
            name='numVagas',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='terreno',
            name='publico',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='terreno',
            name='quantNr',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='terreno',
            name='quantTorre',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='terreno',
            name='torre',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='terreno',
            name='zoneamento',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]
