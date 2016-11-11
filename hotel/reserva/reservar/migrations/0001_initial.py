# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-09 15:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_completo_admin', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dni_cliente', models.CharField(max_length=8)),
                ('nombre_cliente', models.CharField(max_length=50)),
                ('apellidos_cliente', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Habitacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_habitacion', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=200)),
                ('capacidad', models.IntegerField()),
                ('precio', models.DecimalField(decimal_places=2, max_digits=5)),
                ('estado', models.CharField(choices=[('O', 'Ocupada'), ('D', 'Desocupada')], default='D', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_pago', models.DateTimeField(auto_now_add=True)),
                ('tpago', models.CharField(choices=[('E', 'Efectivo'), ('T', 'Tarjeta')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_in', models.DateField()),
                ('fecha_out', models.DateField()),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservar.Admin')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservar.Cliente')),
                ('habitacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservar.Habitacion')),
            ],
        ),
        migrations.AddField(
            model_name='pago',
            name='reserva',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='reservar.Reserva'),
        ),
    ]
