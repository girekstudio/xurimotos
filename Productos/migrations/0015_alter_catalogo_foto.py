# Generated by Django 3.2 on 2021-05-14 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Productos', '0014_alter_galeria_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalogo',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='producto'),
        ),
    ]
