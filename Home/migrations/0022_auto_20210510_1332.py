# Generated by Django 3.2 on 2021-05-10 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0021_auto_20210510_1254'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Contacto_xurimotos',
        ),
        migrations.AddField(
            model_name='envio_email',
            name='mensaje_personalizado',
            field=models.TextField(default='Gracias por elegir xurimotos'),
        ),
    ]
