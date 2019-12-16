from django.contrib import admin

from administracion.models import ProyectoProxy
from configuracion.models import LineaBaseProxy
from desarrollo.models import ItemProxy

class ItemProxyInline(admin.TabularInline):
    model = ItemProxy
    show_change_link = True


class LineaBaseProxyAdmin(admin.ModelAdmin):
    list_display = ['id', 'get_proyecto_nombre', 'nombre', 'estado']
    inlines = [
        ItemProxyInline,
    ]

    def get_proyecto_nombre(self, obj):
        return obj.proyecto.nombre

    get_proyecto_nombre.short_description = 'Proyecto'

    def get_queryset(self, request):

        queryset = ProyectoProxy.objects.none()

        if request.user.groups.filter(name='Administrador').exists():
            queryset = queryset | ProyectoProxy.objects.all()

        if request.user.groups.filter(name='Lider').exists():
            queryset = queryset | request.user.proyectos_comandados.all()

        if request.user.groups.filter(name='Programador').exists():
            queryset = queryset | request.user.proyectos_programados.all()

        if request.user.groups.filter(name='Tester').exists():
            queryset = queryset | request.user.proyectos_testeados.all()

        return LineaBaseProxy.objects.filter(proyecto__in=queryset.distinct())


admin.site.register(LineaBaseProxy, LineaBaseProxyAdmin)
