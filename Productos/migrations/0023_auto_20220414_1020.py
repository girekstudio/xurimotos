# Generated by Django 3.2 on 2022-04-14 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Productos', '0022_alter_catalogo_nombre_producto'),
    ]

    operations = [
        migrations.RenameField(
            model_name='catalogo',
            old_name='nombre_producto',
            new_name='descripcion',
        ),
        migrations.RemoveField(
            model_name='catalogo',
            name='detalle',
        ),
        migrations.AddField(
            model_name='catalogo',
            name='color',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='catalogo',
            name='descuento',
            field=models.IntegerField(blank=True, default=30, null=True),
        ),
        migrations.AddField(
            model_name='catalogo',
            name='precio_final',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=9, null=True),
        ),
        migrations.AddField(
            model_name='catalogo',
            name='precio_unitario',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True),
        ),
        migrations.AddField(
            model_name='catalogo',
            name='unidad_medida',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='catalogo',
            name='unidades_por_caja',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='catalogo',
            name='info_tecnica',
            field=models.TextField(blank=True, max_length=900, null=True),
        ),
    ]