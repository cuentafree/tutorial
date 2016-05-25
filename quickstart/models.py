from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Libro(models.Model):
    nombre = models.TextField(max_length=100)
    editorial = models.TextField(max_length=100)
    genero = models.TextField(max_length=100)
    