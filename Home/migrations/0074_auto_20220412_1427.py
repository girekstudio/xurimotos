# Generated by Django 3.2 on 2022-04-12 19:27

import colorfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0073_alter_editable_xurimotos_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto_carrusel',
            name='codigo_color_imag_1',
            field=colorfield.fields.ColorField(default='FFFFFF', image_field=None, max_length=18, samples=None),
        ),
        migrations.AddField(
            model_name='producto_carrusel',
            name='codigo_color_imag_2',
            field=colorfield.fields.ColorField(default='FFFFFF', image_field=None, max_length=18, samples=None),
        ),
        migrations.AddField(
            model_name='producto_carrusel',
            name='codigo_color_imag_3',
            field=colorfield.fields.ColorField(default='FFFFFF', image_field=None, max_length=18, samples=None),
        ),
        migrations.AddField(
            model_name='producto_carrusel',
            name='codigo_color_imag_4',
            field=colorfield.fields.ColorField(default='FFFFFF', image_field=None, max_length=18, samples=None),
        ),
        migrations.AddField(
            model_name='producto_carrusel',
            name='codigo_color_imag_5',
            field=colorfield.fields.ColorField(default='FFFFFF', image_field=None, max_length=18, samples=None),
        ),
        migrations.AddField(
            model_name='producto_carrusel',
            name='imagen_2',
            field=models.ImageField(blank=True, help_text='368X313 Producto - Carrusel', null=True, upload_to='carrusel'),
        ),
        migrations.AddField(
            model_name='producto_carrusel',
            name='imagen_3',
            field=models.ImageField(blank=True, help_text='368X313 Producto - Carrusel', null=True, upload_to='carrusel'),
        ),
        migrations.AddField(
            model_name='producto_carrusel',
            name='imagen_4',
            field=models.ImageField(blank=True, help_text='368X313 Producto - Carrusel', null=True, upload_to='carrusel'),
        ),
        migrations.AddField(
            model_name='producto_carrusel',
            name='imagen_5',
            field=models.ImageField(blank=True, help_text='368X313 Producto - Carrusel', null=True, upload_to='carrusel'),
        ),
        migrations.AlterField(
            model_name='producto_carrusel',
            name='imagen_1',
            field=models.ImageField(blank=True, help_text='368X313 Producto - Carrusel', null=True, upload_to='carrusel'),
        ),
        migrations.DeleteModel(
            name='Producto_galeria_carrusel',
        ),
    ]
