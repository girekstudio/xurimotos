# Generated by Django 3.2 on 2021-05-03 02:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0008_rename_xurimotos_xurimotos_datos'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Xurimotos_datos',
            new_name='Empresa_Xurimotos',
        ),
        migrations.AlterModelOptions(
            name='empresa_xurimotos',
            options={'verbose_name_plural': '2. Xurimotos'},
        ),
    ]
