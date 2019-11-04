from django.db import models

from base.models import LineaBase


class LineaBaseProxy(LineaBase):

    class Meta:
        proxy = True
        verbose_name = 'Linea Base'
        verbose_name_plural = 'Lineas Base'

    def __str__(self):
        return '{} - {}'.format(self.pk, self.nombre)
