# Generated by Django 3.2 on 2022-04-22 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0089_auto_20220422_0843'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='destacados_xurimotos',
            name='dest_sub_titulo_01',
        ),
        migrations.AddField(
            model_name='destacados_xurimotos',
            name='dest_link_01',
            field=models.CharField(blank=True, help_text='Link  - Secc-Productos P3', max_length=100, null=True),
        ),
    ]