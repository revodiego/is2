from django.contrib import admin
from desarrollo.models import ItemProxy
from administracion.models import ProyectoProxy



class ItemProxyAdmin(admin.ModelAdmin):
    list_display = ['id', 'get_proyecto_nombre', 'get_lineaBase_nombre', 'nombre', 'estado']

    def get_proyecto_nombre(self, obj):
        return obj.lineaBase.proyecto.nombre

    get_proyecto_nombre.short_description = 'Proyecto'

    def get_lineaBase_nombre(self, obj):
        return obj.lineaBase.nombre

    get_lineaBase_nombre.short_description = 'Linea Base'

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

        return ItemProxy.objects.filter(lineaBase__proyecto__in=queryset.distinct())


    def get_readonly_fields(self, request, obj=None):

        if request.user.groups.filter(name__in=['Programador', 'Tester']).exists():
            return ['nombre', 'lineaBase']   

        return []


admin.site.register(ItemProxy, ItemProxyAdmin)