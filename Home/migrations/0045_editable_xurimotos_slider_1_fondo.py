# Generated by Django 3.2 on 2022-03-30 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0044_auto_20220328_1520'),
    ]

    operations = [
        migrations.AddField(
            model_name='editable_xurimotos',
            name='slider_1_fondo',
            field=models.ImageField(blank=True, help_text='1680x617 - Secc-Inicio P1 Fondo Slider ', null=True, upload_to='galeria'),
        ),
    ]
