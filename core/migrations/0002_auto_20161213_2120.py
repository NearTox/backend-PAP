# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-13 21:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orden',
            old_name='detalles',
            new_name='observaciones',
        ),
        migrations.AddField(
            model_name='cliente',
            name='empresa',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='orden',
            name='latitud_mensajero',
            field=models.DecimalField(decimal_places=10, default=0, max_digits=13),
        ),
        migrations.AddField(
            model_name='orden',
            name='longitud_mensajero',
            field=models.DecimalField(decimal_places=10, default=0, max_digits=13),
        ),
        migrations.AddField(
            model_name='orden',
            name='numero_interior',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='orden',
            name='peso_del_paquete',
            field=models.DecimalField(decimal_places=3, default=0.1, max_digits=5),
        ),
        migrations.AlterField(
            model_name='orden',
            name='latitud_destino',
            field=models.DecimalField(decimal_places=10, max_digits=13),
        ),
        migrations.AlterField(
            model_name='orden',
            name='latitud_origen',
            field=models.DecimalField(decimal_places=10, max_digits=13),
        ),
        migrations.AlterField(
            model_name='orden',
            name='longitud_destino',
            field=models.DecimalField(decimal_places=10, max_digits=13),
        ),
        migrations.AlterField(
            model_name='orden',
            name='longitud_origen',
            field=models.DecimalField(decimal_places=10, max_digits=13),
        ),
        migrations.AlterField(
            model_name='orden',
            name='precio',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterUniqueTogether(
            name='cliente',
            unique_together=set([('nombre', 'email', 'telefono', 'empresa')]),
        ),
    ]
