# Generated by Django 3.2 on 2021-05-08 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0015_auto_20210508_1429'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto_redes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook', models.CharField(blank=True, max_length=100, null=True)),
                ('instagram', models.CharField(blank=True, max_length=100, null=True)),
                ('twitter', models.CharField(blank=True, max_length=100, null=True)),
                ('linkedin', models.CharField(blank=True, max_length=100, null=True)),
                ('youtube', models.CharField(blank=True, max_length=100, null=True)),
                ('behance', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name_plural': '8. Contácto Redes Sociales',
            },
        ),
        migrations.CreateModel(
            name='Contacto_xurimotos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('whatsapp', models.CharField(blank=True, max_length=13, null=True)),
                ('telefono', models.CharField(blank=True, max_length=11, null=True)),
                ('celular', models.CharField(blank=True, max_length=100, null=True)),
                ('correo', models.EmailField(blank=True, max_length=254, null=True)),
                ('direccion', models.CharField(blank=True, max_length=100, null=True)),
                ('horario_lu_vier', models.CharField(blank=True, max_length=100, null=True)),
                ('horario_sab', models.CharField(blank=True, max_length=100, null=True)),
                ('horario_dom', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name_plural': '7. Contacto Xurimotos',
            },
        ),
        migrations.CreateModel(
            name='Empresa_Xurimotos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quienes_somos', models.TextField(blank=True, max_length=100, null=True)),
                ('mision', models.CharField(blank=True, max_length=100, null=True)),
                ('vision', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name_plural': '2. Empresa Xurimotos',
            },
        ),
        migrations.RemoveField(
            model_name='marca_xurimotos',
            name='behance',
        ),
        migrations.RemoveField(
            model_name='marca_xurimotos',
            name='celular',
        ),
        migrations.RemoveField(
            model_name='marca_xurimotos',
            name='correo',
        ),
        migrations.RemoveField(
            model_name='marca_xurimotos',
            name='direccion',
        ),
        migrations.RemoveField(
            model_name='marca_xurimotos',
            name='facebook',
        ),
        migrations.RemoveField(
            model_name='marca_xurimotos',
            name='horario_dom',
        ),
        migrations.RemoveField(
            model_name='marca_xurimotos',
            name='horario_lu_vier',
        ),
        migrations.RemoveField(
            model_name='marca_xurimotos',
            name='horario_sab',
        ),
        migrations.RemoveField(
            model_name='marca_xurimotos',
            name='instagram',
        ),
        migrations.RemoveField(
            model_name='marca_xurimotos',
            name='linkedin',
        ),
        migrations.RemoveField(
            model_name='marca_xurimotos',
            name='mision',
        ),
        migrations.RemoveField(
            model_name='marca_xurimotos',
            name='quienes_somos',
        ),
        migrations.RemoveField(
            model_name='marca_xurimotos',
            name='telefono',
        ),
        migrations.RemoveField(
            model_name='marca_xurimotos',
            name='twitter',
        ),
        migrations.RemoveField(
            model_name='marca_xurimotos',
            name='vision',
        ),
        migrations.RemoveField(
            model_name='marca_xurimotos',
            name='whatsapp',
        ),
        migrations.RemoveField(
            model_name='marca_xurimotos',
            name='youtube',
        ),
    ]
