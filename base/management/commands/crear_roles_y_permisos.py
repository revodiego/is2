import logging

from django.contrib.auth.models import Group, User, Permission
from django.contrib.contenttypes.models import ContentType
from django.core.management.base import BaseCommand

logger = logging.getLogger('django')


class Command(BaseCommand):
    help = 'Crea los roles y asigna los permisos a dichos roles'

    def handle(self, *args, **options):
        # Creamos los grupos
        staff_g, _ = Group.objects.get_or_create(name='Staff')
        lider_g, _ = Group.objects.get_or_create(name='Lider')
        programador_g, _ = Group.objects.get_or_create(name='Programador')
        tester_g, _ = Group.objects.get_or_create(name='Tester')

        # Creamos los usuarios
        if not User.objects.filter(username='admin').exists():
            admin_u = User.objects.create_superuser(
                username='admin',
                email='admin@a.com',
                password='admin',
                first_name='Armando',
                last_name='Amarilla'
            )
            logger.info('Admin creado')
        else:
            admin_u = User.objects.get(username='admin')
            logger.info('Admin existente')

        if not User.objects.filter(username='staff').exists():
            staff_u = User.objects.create_user(
                username='staff',
                email='staff@a.com',
                password='staff',
                is_staff=True,
                first_name='Sergio',
                last_name='Salazar'
            )
            logger.info('Staff creado')
        else:
            staff_u = User.objects.get(username='staff')
            logger.info('Staff existente')

        if not User.objects.filter(username='lider').exists():
            lider_u = User.objects.create_user(
                username='lider',
                email='lider@a.com',
                password='lider',
                is_staff=True,
                first_name='Luis',
                last_name='Lopez'
            )
            logger.info('Lider creado')
        else:
            lider_u = User.objects.get(username='lider')
            logger.info('Lider existente')

        if not User.objects.filter(username='programador').exists():
            programador_u = User.objects.create_user(
                username='programador',
                email='programador@a.com',
                password='programador',
                is_staff=True,
                first_name='Pedro',
                last_name='Picapiedras'
            )
            logger.info('Programador creado')
        else:
            programador_u = User.objects.get(username='programador')
            logger.info('Programador existente')

        if not User.objects.filter(username='tester').exists():
            tester_u = User.objects.create_user(
                username='tester',
                email='tester@a.com',
                password='tester',
                is_staff=True,
                first_name='Tony',
                last_name='Tortillas'
            )
            logger.info('Tester creado')
        else:
            tester_u = User.objects.get(username='tester')
            logger.info('Tester existente')

        # Agregamos los usuarios a los grupos
        staff_g.user_set.add(admin_u)
        staff_g.user_set.add(staff_u)
        staff_g.save()
        logger.info('Agregado usuarios al grupo Staff')
        lider_g.user_set.add(lider_u)
        lider_g.save()
        logger.info('Agregado usuario al grupo Lider')
        programador_g.user_set.add(programador_u)
        programador_g.save()
        logger.info('Agregado usuario al grupo Programador')
        tester_g.user_set.add(tester_u)
        tester_g.save()
        logger.info('Agregado usuario al grupo Tester')

        # Agregamos los permisos a los grupos
        pstaff = [
            ('administracion', 'userproxy', 'add_userproxy'),
            ('administracion', 'userproxy', 'change_userproxy'),
            ('administracion', 'userproxy', 'delete_userproxy'),
            ('administracion', 'userproxy', 'view_userproxy'),

            ('administracion', 'proyectoproxy', 'add_proyectoproxy'),
            ('administracion', 'proyectoproxy', 'change_proyectoproxy'),
            ('administracion', 'proyectoproxy', 'delete_proyectoproxy'),
            ('administracion', 'proyectoproxy', 'view_proyectoproxy'),

            ('configuracion', 'lineabaseproxy', 'add_lineabaseproxy'),
            ('configuracion', 'lineabaseproxy', 'change_lineabaseproxy'),
            ('configuracion', 'lineabaseproxy', 'delete_lineabaseproxy'),
            ('configuracion', 'lineabaseproxy', 'view_lineabaseproxy'),

            ('configuracion', 'itemproxy', 'add_itemproxy'),
            ('configuracion', 'itemproxy', 'change_itemproxy'),
            ('configuracion', 'itemproxy', 'delete_itemproxy'),
            ('configuracion', 'itemproxy', 'view_itemproxy'),
        ]
        plider = [
            ('administracion', 'proyectoproxy', 'change_proyectoproxy'),
            ('administracion', 'proyectoproxy', 'view_proyectoproxy'),

            ('configuracion', 'lineabaseproxy', 'change_lineabaseproxy'),
            ('configuracion', 'lineabaseproxy', 'view_lineabaseproxy'),

            ('configuracion', 'itemproxy', 'change_itemproxy'),
            ('configuracion', 'itemproxy', 'view_itemproxy'),
        ]
        pprogramador = [
            ('administracion', 'proyectoproxy', 'view_proyectoproxy'),
            ('configuracion', 'lineabaseproxy', 'view_lineabaseproxy'),
            ('configuracion', 'itemproxy', 'view_itemproxy'),
        ]
        ptester = [
            ('administracion', 'proyectoproxy', 'view_proyectoproxy'),
            ('configuracion', 'lineabaseproxy', 'view_lineabaseproxy'),
            ('configuracion', 'itemproxy', 'view_itemproxy'),
        ]
        for permiso in Permission.objects.all():
            logger.info('permiso {} => {}'.format(permiso, permiso.codename))

        for ctype in ContentType.objects.all():
            logger.info('ctype {} => {}'.format(ctype.app_label, ctype.model))

        for p in pstaff:
            ctype = ContentType.objects.get(app_label=p[0], model=p[1])
            perm = Permission.objects.get(content_type=ctype, codename=p[2])
            staff_g.permissions.add(perm)
            logger.info('Agregado permiso {}_{}.{} a {}'.format(p[0], p[1], p[2], staff_g.name))

        for p in plider:
            ctype = ContentType.objects.get(app_label=p[0], model=p[1])
            perm = Permission.objects.get(content_type=ctype, codename=p[2])
            lider_g.permissions.add(perm)
            logger.info('Agregado permiso {}_{}.{} a {}'.format(p[0], p[1], p[2], lider_g.name))

        for p in pprogramador:
            ctype = ContentType.objects.get(app_label=p[0], model=p[1])
            perm = Permission.objects.get(content_type=ctype, codename=p[2])
            programador_g.permissions.add(perm)
            logger.info('Agregado permiso {}_{}.{} a {}'.format(p[0], p[1], p[2], programador_g.name))

        for p in ptester:
            ctype = ContentType.objects.get(app_label=p[0], model=p[1])
            perm = Permission.objects.get(content_type=ctype, codename=p[2])
            tester_g.permissions.add(perm)
            logger.info('Agregado permiso {}_{}.{} a {}'.format(p[0], p[1], p[2], tester_g.name))
