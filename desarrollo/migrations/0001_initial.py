# Generated by Django 2.2.6 on 2019-11-04 22:35

from django.db import migrations


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base', '0002_proyecto_fase'),
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
    ]
