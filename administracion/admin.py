from django.contrib import admin

from administracion.models import UserProxy, ProyectoProxy
from configuracion.models import LineaBaseProxy


class UserProxyAdmin(admin.ModelAdmin):
    fields = ['username', 'first_name', 'last_name', 'groups']
    list_display = ['id', 'first_name', 'last_name', 'username']

    def save_model(self, request, obj, form, change):
        super(UserProxyAdmin, self).save_model(request, obj, form, change)
        if obj.password == '':
            obj.set_password('inicial')
        obj.is_staff = True
        obj.save()

class LineaBaseProxyInline(admin.TabularInline):
    model = LineaBaseProxy
    show_change_link = True


class ProyectoProxyAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'estado', 'lider', 'programador', 'tester']
    inlines = [
        LineaBaseProxyInline,
    ]

    def get_queryset(self, request):

        queryset = ProyectoProxy.objects.none()

        if request.user.groups.filter(name='Staff').exists():
            queryset = queryset | ProyectoProxy.objects.all()

        if request.user.groups.filter(name='Lider').exists():
            queryset = queryset | request.user.proyectos_comandados.all()

        if request.user.groups.filter(name='Programador').exists():
            queryset = queryset | request.user.proyectos_programados.all()

        if request.user.groups.filter(name='Tester').exists():
            queryset = queryset | request.user.proyectos_testeados.all()

        return queryset.distinct()

    def get_readonly_fields(self, request, obj=None):

        if request.user.groups.filter(name='Lider').exists():
            return ['lider', 'nombre', 'estado', 'programador', 'tester']

        return []


admin.site.register(UserProxy, UserProxyAdmin)
admin.site.register(ProyectoProxy, ProyectoProxyAdmin)
