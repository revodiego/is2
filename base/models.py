from django.db import models

# Create your models here.


class Proyecto(models.Model):
    ESTADO_PENDIENTE = 'PE'
    ESTADO_EN_PROCESO = 'EP'
    ESTADO_FINALIZADO = 'FI'
    ESTADOS = (
        (ESTADO_PENDIENTE, 'Pendiente'),
        (ESTADO_EN_PROCESO, 'En proceso'),
        (ESTADO_FINALIZADO, 'Finalizado'),
        )
    nombre = models.CharField(max_length=255)
    estado = models.CharField(max_length=2, choices=ESTADOS, default=ESTADO_PENDIENTE)
    lider = models.ForeignKey(
        'auth.User',
        on_delete=models.PROTECT,
        blank=True,
        null=True, 
        related_name='proyectos_comandados')
    programador = models.ForeignKey(
        'auth.User',
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        related_name='proyectos_programados')
    tester = models.ForeignKey(
        'auth.User',
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        related_name='proyectos_testeados')

    def __str__(self):
        return '{} - {}'.format(self.id, self.nombre)
        
class LineaBase(models.Model):
    ESTADO_PENDIENTE = 'PE'
    ESTADO_EN_PROCESO = 'EP'
    ESTADO_FINALIZADO = 'FI'
    ESTADOS = (
        (ESTADO_PENDIENTE, 'Pendiente'),
        (ESTADO_EN_PROCESO, 'En proceso'),
        (ESTADO_FINALIZADO, 'Finalizado'),
        )
    nombre = models.CharField(max_length=255)
    estado = models.CharField(max_length=2, choices=ESTADOS, default=ESTADO_PENDIENTE)
    proyecto = models.ForeignKey(
        'base.Proyecto',
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        related_name='lineas_base')

    def __str__(self):
        return '{} - {}'.format(self.id, self.nombre)
        
class Item(models.Model):
    ESTADO_PENDIENTE = 'PE'
    ESTADO_EN_PROCESO = 'EP'
    ESTADO_FINALIZADO = 'FI'
    ESTADOS = (
        (ESTADO_PENDIENTE, 'Pendiente'),
        (ESTADO_EN_PROCESO, 'En proceso'),
        (ESTADO_FINALIZADO, 'Finalizado'),
        )
    nombre = models.CharField(max_length=255)
    estado = models.CharField(max_length=2, choices=ESTADOS, default=ESTADO_PENDIENTE)
    lineaBase = models.ForeignKey(
        'base.LineaBase',
        on_delete=models.PROTECT,
        related_name='items')

    def __str__(self):
        return '{} - {}'.format(self.id, self.nombre)
    
