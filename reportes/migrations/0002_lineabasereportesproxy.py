# Generated by Django 2.2.6 on 2019-12-16 22:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_auto_20191216_1920'),
        ('reportes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LineaBaseReportesProxy',
            fields=[
            ],
            options={
                'verbose_name': 'Linea Base',
                'verbose_name_plural': 'Lineas Base',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('base.lineabase',),
        ),
    ]
