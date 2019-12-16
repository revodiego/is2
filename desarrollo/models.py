from django.db import models

from base.models import Item


class ItemProxy(Item):

    class Meta:
        proxy = True
        verbose_name = 'Item'
        verbose_name_plural = 'Items'

    def __str__(self):
        return '{} - {}'.format(self.pk, self.nombre)
