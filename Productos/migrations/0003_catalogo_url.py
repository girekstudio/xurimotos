# Generated by Django 3.2 on 2021-05-01 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Productos', '0002_alter_catalogo_unidades_por_caja'),
    ]

    operations = [
        migrations.AddField(
            model_name='catalogo',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
