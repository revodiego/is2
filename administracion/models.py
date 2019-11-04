from django.contrib.auth.models import User, UserManager
from django.db import models

from base.models import Proyecto


class UserProxyManager(UserManager):

    def get_queryset(self):
        return super(UserProxyManager, self).get_queryset().filter(is_superuser=False)


class UserProxy(User):
    objects = UserProxyManager()

    class Meta:
        proxy = True
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return '{}, {}'.format(self.last_name, self.first_name)


class ProyectoProxy(Proyecto):

    class Meta:
        proxy = True
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'

    def __str__(self):
        return '{} - {}'.format(self.pk, self.nombre)

