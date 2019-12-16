from django.contrib.auth import get_user_model

from base.models import Item, LineaBase


class ItemReportesProxy(Item):

    class Meta:
        proxy = True
        verbose_name = 'Item'
        verbose_name_plural = 'Items'

    def __str__(self):
        return '{} - {}'.format(self.pk, self.nombre)


class LineaBaseReportesProxy(LineaBase):

    class Meta:
        proxy = True
        verbose_name = 'Linea Base'
        verbose_name_plural = 'Lineas Base'

    def __str__(self):
        return '{} - {}'.format(self.pk, self.nombre)


class UserReportesProxy(get_user_model()):

    class Meta:
        proxy = True
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

