# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

CATEGORIES = (
    ('Conferencia', 'Conferencia'),
    ('Seminario', 'Seminario'),
    ('Congreso', 'Congreso'),
    ('Curso', 'Curso')
)

TYPES = (
    ('Presencial', 'Presencial'),
    ('Virtual', 'Virtual')
)

class Event(models.Model):
    name = models.CharField(max_length=255, verbose_name=u'Nombre')
    category = models.CharField(max_length=50, choices=CATEGORIES, verbose_name=u'Categoría')
    type = models.CharField(max_length=50, choices=TYPES, verbose_name=u'Tipo de evento')
    place = models.CharField(blank=True, null=True,max_length=255, verbose_name=u'Lugar')    
    address = models.CharField(blank=True, null=True,max_length=255, verbose_name=u'Dirección')
    start_date = models.DateField(blank=True, null=True, verbose_name=u'Fecha de inicio')
    end_date = models.DateField(blank=True, null=True, verbose_name=u'Fecha de término')
    register_date = models.DateField(blank=True, null=True, verbose_name=u'Fecha de registro', auto_now_add=True)

    def __unicode__(self):
        return self.name