# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField


class Terreno(models.Model):
    gestor           = models.CharField(max_length=200, null=True)
    codigo           = models.IntegerField(null=True)
    nomeTerreno      = models.CharField(max_length=200, null=True)
    metragem         = models.FloatField(null=True)
    zoneamento       = models.CharField(max_length=200, null=True)
    publico          = models.CharField(max_length=200, null=True)
    tipoFachadaAtiva = models.IntegerField(null=True)
    garagem          = models.CharField(max_length=200, null=True)
    numVagas         = models.IntegerField(null=True)
    andaresGaragem   = models.IntegerField(null=True)
    tipovaga         = models.CharField(max_length=200, null=True)
    fachadaAtiva     = models.IntegerField(null=True)
    
    tipoTorre        = ArrayField(models.CharField(max_length=200), null=True)
    quantAndar       = ArrayField(models.IntegerField(), null=True)
    apartAndar       = ArrayField(models.IntegerField(), null=True)
    quantTorre       = ArrayField(models.IntegerField(), null=True)
    
    coef_aprov       = models.FloatField(null=True)
    eficiencia       = models.FloatField(null=True)
    user             = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id}. {self.nomeTerreno}"