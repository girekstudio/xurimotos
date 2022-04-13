# Generated by Django 3.2 on 2022-04-07 23:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0050_auto_20220406_1653'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto_carrusel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=False)),
                ('titulo', models.CharField(blank=True, help_text='Título - Secc-Productos', max_length=100, null=True)),
                ('enlace', models.CharField(blank=True, help_text='Link - Secc-Productos ', max_length=100, null=True)),
                ('imagen_1', models.ImageField(blank=True, help_text='Producto - Carrusel Producto  Imagenes 200*160', null=True, upload_to='carrusel')),
            ],
            options={
                'verbose_name_plural': '5. Producto Carrusel',
            },
        ),
        migrations.CreateModel(
            name='Producto_galeria_carrusel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen_1', models.ImageField(blank=True, help_text='Producto - Carrusel Producto  Imagenes 706*246, si se envia en otro tamaño la aplicación cambiará el tamaño automáticamente', null=True, upload_to='carrusel')),
                ('imagen_2', models.ImageField(blank=True, help_text='Producto - Carrusel Producto  Imagenes 706*246, si se envia en otro tamaño la aplicación cambiará el tamaño automáticamente', null=True, upload_to='carrusel')),
                ('imagen_3', models.ImageField(blank=True, help_text='Producto - Carrusel Producto Imagenes 706*246, si se envia en otro tamaño la aplicación cambiará el tamaño automáticamente', null=True, upload_to='carrusel')),
                ('producto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Home.producto_carrusel')),
            ],
            options={
                'verbose_name_plural': '6. Galeria Producto Carrusel',
            },
        ),
        migrations.RemoveField(
            model_name='galeria_carrusel_producto',
            name='producto_carrusel',
        ),
        migrations.DeleteModel(
            name='Carrusel_producto',
        ),
        migrations.DeleteModel(
            name='Galeria_carrusel_producto',
        ),
    ]
