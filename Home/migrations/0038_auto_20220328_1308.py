# Generated by Django 3.2 on 2022-03-28 18:08

from django.db import migrations, models
import xurimotos.snippers


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0037_distribuidores_xurimotos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrusel_producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=False)),
                ('titulo', models.CharField(blank=True, help_text='Título - Secc-Productos', max_length=100, null=True)),
                ('enlace', models.CharField(blank=True, help_text='Link - Secc-Productos ', max_length=100, null=True)),
                ('imagen_1', models.ImageField(blank=True, help_text='Producto - Carrusel Producto  Imagenes 706*246, si se envia en otro tamaño la aplicación cambiará el tamaño automáticamente', null=True, upload_to='carrusel')),
                ('imagen_2', models.ImageField(blank=True, help_text='Producto - Carrusel Producto  Imagenes 706*246, si se envia en otro tamaño la aplicación cambiará el tamaño automáticamente', null=True, upload_to='carrusel')),
                ('imagen_3', models.ImageField(blank=True, help_text='Producto - Carrusel Producto Imagenes 706*246, si se envia en otro tamaño la aplicación cambiará el tamaño automáticamente', null=True, upload_to='carrusel')),
                ('color_hexadecimal', models.CharField(blank=True, help_text='Color variante', max_length=100, null=True)),
            ],
            options={
                'verbose_name_plural': '4. Carrusel_producto',
            },
            bases=(models.Model, xurimotos.snippers.ResizeImageMixin),
        ),
        migrations.DeleteModel(
            name='Slider_2',
        ),
        migrations.RemoveField(
            model_name='marca_xurimotos',
            name='imagen_principal',
        ),
        migrations.RemoveField(
            model_name='marca_xurimotos',
            name='imagen_slider',
        ),
        migrations.RemoveField(
            model_name='marca_xurimotos',
            name='mision',
        ),
        migrations.RemoveField(
            model_name='marca_xurimotos',
            name='quienes_somos',
        ),
        migrations.RemoveField(
            model_name='marca_xurimotos',
            name='vision',
        ),
    ]
