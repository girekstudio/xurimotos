# Generated by Django 3.2 on 2022-04-11 18:48

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0068_auto_20220411_1346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto_galeria_carrusel',
            name='codigo_color_imag_1',
            field=colorfield.fields.ColorField(default='', image_field=None, max_length=18, samples=None),
        ),
        migrations.AlterField(
            model_name='producto_galeria_carrusel',
            name='codigo_color_imag_2',
            field=colorfield.fields.ColorField(default='', image_field=None, max_length=18, samples=None),
        ),
        migrations.AlterField(
            model_name='producto_galeria_carrusel',
            name='codigo_color_imag_3',
            field=colorfield.fields.ColorField(default='', image_field=None, max_length=18, samples=None),
        ),
        migrations.AlterField(
            model_name='producto_galeria_carrusel',
            name='codigo_color_imag_4',
            field=colorfield.fields.ColorField(default='', image_field=None, max_length=18, samples=None),
        ),
        migrations.AlterField(
            model_name='producto_galeria_carrusel',
            name='codigo_color_imag_5',
            field=colorfield.fields.ColorField(default='', image_field=None, max_length=18, samples=None),
        ),
        migrations.AlterField(
            model_name='producto_galeria_carrusel',
            name='codigo_color_imag_6',
            field=colorfield.fields.ColorField(default='', image_field=None, max_length=18, samples=None),
        ),
    ]
