# Generated by Django 4.2.2 on 2023-11-09 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_principal', '0004_profesional_especialidades'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='crearturno',
            name='especialidad',
        ),
        migrations.AddField(
            model_name='crearturno',
            name='especialidades',
            field=models.ManyToManyField(to='app_principal.especialidades'),
        ),
    ]
