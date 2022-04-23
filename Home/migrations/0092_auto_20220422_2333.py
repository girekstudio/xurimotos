# Generated by Django 3.2 on 2022-04-23 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0091_auto_20220422_2255'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogs',
            name='activar_galeria',
        ),
        migrations.RemoveField(
            model_name='blogs',
            name='activar_youtube',
        ),
        migrations.AlterField(
            model_name='blogs',
            name='tipo_archivo',
            field=models.CharField(choices=[('imagen', 'imagen'), ('video', 'video'), ('youtube', 'youtube'), ('galeria', 'galeria')], default='imagen', max_length=20),
        ),
    ]
