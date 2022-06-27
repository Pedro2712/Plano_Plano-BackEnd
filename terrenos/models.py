# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class Terreno(models.Model):
    title = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id}. {self.title}"