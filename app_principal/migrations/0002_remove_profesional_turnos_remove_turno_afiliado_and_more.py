# Generated by Django 4.2.2 on 2023-10-30 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_principal', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profesional',
            name='turnos',
        ),
        migrations.RemoveField(
            model_name='turno',
            name='afiliado',
        ),
        migrations.AddField(
            model_name='turno',
            name='afiliados',
            field=models.ManyToManyField(related_name='turnos', to='app_principal.afiliado'),
        ),
        migrations.AddField(
            model_name='turno',
            name='profesionales',
            field=models.ManyToManyField(related_name='turnos', to='app_principal.profesional'),
        ),
    ]
