# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class Terreno(models.Model):
    nomeTerreno    = models.CharField(max_length=200)
    codigo         = models.IntegerField(null=True)
    metragem       = models.FloatField(null=True)
    zoneamento     = models.CharField(max_length=200)
    publico        = models.CharField(max_length=200)
    gestor         = models.CharField(max_length=200)
    torre          = models.CharField(max_length=200)
    andares        = models.IntegerField(null=True)
    numAndar       = models.IntegerField(null=True)
    quantTorre     = models.IntegerField(null=True)
    garagem        = models.CharField(max_length=200)
    numVagas       = models.IntegerField(null=True)
    numMotos       = models.IntegerField(null=True)
    andaresGaragem = models.IntegerField(null=True)
    metragemMall   = models.FloatField(null=True)
    andaresMall    = models.IntegerField(null=True)
    andarNr        = models.IntegerField(null=True)
    NumAndarNr     = models.IntegerField(null=True)
    quantNr        = models.IntegerField(null=True)
    ca             = models.FloatField()
    eficiencia     = models.FloatField()
    user           = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id}. {self.title}"