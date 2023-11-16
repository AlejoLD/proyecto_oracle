# Generated by Django 4.2.6 on 2023-10-05 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Ingrese el Nombre del Cliente', max_length=100)),
                ('direccion', models.CharField(help_text='Ingrese la Direccion del Cliente', max_length=100)),
                ('telefono', models.CharField(help_text='Ingrese el Telefono del Cliente', max_length=12)),
                ('correo', models.EmailField(help_text='Ingrese el Correo del Cliente', max_length=100)),
                ('password', models.CharField(help_text='Ingrese el Password del Cliente', max_length=100)),
            ],
            options={
                'verbose_name': 'cliente',
                'verbose_name_plural': 'clientes',
            },
        ),
    ]
