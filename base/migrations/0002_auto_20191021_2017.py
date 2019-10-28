# Generated by Django 2.2.6 on 2019-10-21 23:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyecto',
            name='tester',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='proyectos_testeados', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='programador',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='proyectos_programados', to=settings.AUTH_USER_MODEL),
        ),
    ]