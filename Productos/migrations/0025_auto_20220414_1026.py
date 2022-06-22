# Generated by Django 3.2 on 2022-04-14 15:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Productos', '0024_auto_20220414_1023'),
    ]

    operations = [
        migrations.AddField(
            model_name='catalogo',
            name='aux',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='catalogo',
            name='categoria',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Productos.categoria'),
        ),
        migrations.AddField(
            model_name='catalogo',
            name='codigo',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='catalogo',
            name='detalle',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='catalogo',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='producto'),
        ),
        migrations.AddField(
            model_name='catalogo',
            name='info_tecnica',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='catalogo',
            name='nombre_producto',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
    ]
