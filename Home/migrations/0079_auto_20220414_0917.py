# Generated by Django 3.2 on 2022-04-14 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0078_auto_20220413_0948'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='editable_xurimotos',
            name='img_fondo_vide_horiz',
        ),
        migrations.RemoveField(
            model_name='editable_xurimotos',
            name='img_fondo_vide_verti',
        ),
    ]
