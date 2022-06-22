# Generated by Django 3.2 on 2022-04-11 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0062_auto_20220411_1205'),
    ]

    operations = [
        migrations.CreateModel(
            name='Color_Productos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(blank=True, help_text='Título - Secc-Productos', max_length=7, null=True)),
                ('codigo_color', models.CharField(blank=True, help_text='Título - Secc-Productos', max_length=7, null=True)),
            ],
            options={
                'verbose_name_plural': '7.Colores para producto',
            },
        ),
    ]
