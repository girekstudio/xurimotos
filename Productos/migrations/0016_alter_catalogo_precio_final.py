# Generated by Django 3.2 on 2021-06-01 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Productos', '0015_alter_catalogo_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalogo',
            name='precio_final',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9),
        ),
    ]
