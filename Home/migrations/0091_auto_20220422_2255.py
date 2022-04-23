# Generated by Django 3.2 on 2022-04-23 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0090_auto_20220422_0959'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogs',
            name='tipo_video_link',
        ),
        migrations.AddField(
            model_name='blogs',
            name='activar_galeria',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='blogs',
            name='activar_youtube',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='blogs',
            name='imagen_galeria_1',
            field=models.FileField(blank=True, help_text='imagen galeria de 1280*500', null=True, upload_to='blog'),
        ),
        migrations.AddField(
            model_name='blogs',
            name='imagen_galeria_2',
            field=models.FileField(blank=True, help_text='imagen galeria de 1280*500', null=True, upload_to='blog'),
        ),
        migrations.AddField(
            model_name='blogs',
            name='imagen_galeria_3',
            field=models.FileField(blank=True, help_text='imagen galeria de 1280*500', null=True, upload_to='blog'),
        ),
        migrations.AddField(
            model_name='blogs',
            name='link_youtube',
            field=models.CharField(blank=True, help_text='Pegar el código del video', max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='blogs',
            name='tipo_video',
            field=models.FileField(blank=True, help_text='video en mp4', null=True, upload_to='blog'),
        ),
    ]
