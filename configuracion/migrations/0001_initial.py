# Generated by Django 2.2.6 on 2019-10-31 02:53

from django.db import migrations


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemProxy',
            fields=[
            ],
            options={
                'verbose_name': 'Item',
                'verbose_name_plural': 'Items',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('base.item',),
        ),
        migrations.CreateModel(
            name='LineaBaseProxy',
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
