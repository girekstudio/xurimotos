# Generated by Django 3.2 on 2022-04-21 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0084_remove_banner_activo'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner',
            name='activo',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='editable_xurimotos',
            name='mision_img_3',
            field=models.ImageField(blank=True, help_text='660x840 - Secc-Empresa P1 Imagen misión', null=True, upload_to='galeria'),
        ),
        migrations.AddField(
            model_name='editable_xurimotos',
            name='vision_img_3',
            field=models.ImageField(blank=True, help_text='455x310 - Secc-Empresa P1 Imagen misión', null=True, upload_to='galeria'),
        ),
    ]
