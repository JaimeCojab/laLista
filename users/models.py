from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Usuario(models.Model):
	name = models.CharField(max_length = 255)
	email = models.CharField(max_length = 255)
	donador = models.BooleanField()


		