# Generated by Django 3.2 on 2021-05-12 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0022_auto_20210510_1332'),
    ]

    operations = [
        migrations.AddField(
            model_name='marca_xurimotos',
            name='logo_dorado',
            field=models.ImageField(blank=True, null=True, upload_to='marca'),
        ),
        migrations.AlterField(
            model_name='galeria_xurimotos',
            name='imag_4',
            field=models.ImageField(blank=True, help_text='Imagen empresa', null=True, upload_to='media'),
        ),
        migrations.AlterField(
            model_name='galeria_xurimotos',
            name='imag_5',
            field=models.ImageField(blank=True, help_text='imagenes mision', null=True, upload_to='media'),
        ),
        migrations.AlterField(
            model_name='galeria_xurimotos',
            name='imag_6',
            field=models.ImageField(blank=True, help_text='imagenes vision', null=True, upload_to='media'),
        ),
    ]
