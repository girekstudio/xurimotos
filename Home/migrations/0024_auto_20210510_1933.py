# Generated by Django 3.2 on 2021-05-10 19:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0023_auto_20210510_1625'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Empresa_Xurimotos',
        ),
        migrations.AlterModelOptions(
            name='galeria_comunidad',
            options={'verbose_name_plural': '3. Galeria Comunidad'},
        ),
        migrations.AlterModelOptions(
            name='galeria_xurimotos',
            options={'verbose_name_plural': '5. Galeria_XuriMotos'},
        ),
        migrations.AlterModelOptions(
            name='slider',
            options={'verbose_name_plural': '4. Slider'},
        ),
        migrations.AlterModelOptions(
            name='valores',
            options={'verbose_name_plural': '2. Valores Empresa '},
        ),
    ]
