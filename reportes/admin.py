from django.contrib import admin
from django.contrib.auth import get_user_model
from django.db.models import Count

from reportes.models import ItemReportesProxy, LineaBaseReportesProxy, UserReportesProxy


class ItemProxyAdmin(admin.ModelAdmin):

    def changelist_view(self, request, extra_context=None):
        if not extra_context:
            extra_context = {}
        extra_context.update({
            'super_data': ItemReportesProxy.objects.values('estado').annotate(
                cantidad=Count('pk')
            )
        })
        return super().changelist_view(request, extra_context)


admin.site.register(ItemReportesProxy, ItemProxyAdmin)


class LineaBaseProxyAdmin(admin.ModelAdmin):

    def changelist_view(self, request, extra_context=None):
        if not extra_context:
            extra_context = {}
        extra_context.update({
            'super_data': LineaBaseReportesProxy.objects.values('estado').annotate(
                cantidad=Count('pk')
            )
        })
        return super().changelist_view(request, extra_context)


admin.site.register(LineaBaseReportesProxy, LineaBaseProxyAdmin)


class UserProxyAdmin(admin.ModelAdmin):

    def changelist_view(self, request, extra_context=None):
        if not extra_context:
            extra_context = {}
        extra_context.update({
            'super_data': get_user_model().objects.values('first_name', 'last_name', 'username').annotate(
                comanda=Count('proyectos_comandados'),
                programa=Count('proyectos_programados'),
                testea=Count('proyectos_testeados'),
            )
        })
        return super().changelist_view(request, extra_context)


admin.site.register(UserReportesProxy, UserProxyAdmin)
