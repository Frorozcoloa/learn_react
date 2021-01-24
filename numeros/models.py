from django.db import models
from jsonfield import JSONField
import json
 

class Todo(models.Model):
  title = models.CharField(max_length=120)
  description = models.TextField()
  completed = models.BooleanField(default=False)

  def _str_(self):
    return self.title


class ModelNumero(models.Model):
  numero = models.IntegerField(primary_key=True)
  primos  = JSONField()
  primos_gemelos = JSONField()

  def _str_(self):
    return self.numero



