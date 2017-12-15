# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Galaxy(models.Model):
    name = models.CharField(max_length=15, null=True)


class GravitationalBoundSystem(models.Model):
    name = models.CharField(max_length=15, null=True)
    galaxy = models.ForeignKey('Galaxy', on_delete=models.CASCADE, null=True)
