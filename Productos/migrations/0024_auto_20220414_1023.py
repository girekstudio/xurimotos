# Generated by Django 3.2 on 2022-04-14 15:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Productos', '0023_auto_20220414_1020'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='catalogo',
            name='aux',
        ),
        migrations.RemoveField(
            model_name='catalogo',
            name='categoria',
        ),
        migrations.RemoveField(
            model_name='catalogo',
            name='codigo',
        ),
        migrations.RemoveField(
            model_name='catalogo',
            name='color',
        ),
        migrations.RemoveField(
            model_name='catalogo',
            name='descripcion',
        ),
        migrations.RemoveField(
            model_name='catalogo',
            name='descuento',
        ),
        migrations.RemoveField(
            model_name='catalogo',
            name='foto',
        ),
        migrations.RemoveField(
            model_name='catalogo',
            name='info_tecnica',
        ),
        migrations.RemoveField(
            model_name='catalogo',
            name='precio_final',
        ),
        migrations.RemoveField(
            model_name='catalogo',
            name='precio_unitario',
        ),
        migrations.RemoveField(
            model_name='catalogo',
            name='unidad_medida',
        ),
        migrations.RemoveField(
            model_name='catalogo',
            name='unidades_por_caja',
        ),
    ]
