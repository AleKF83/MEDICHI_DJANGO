# Generated by Django 4.2.2 on 2023-11-08 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_principal', '0003_remove_especialidadesprofesionales_profesional_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profesional',
            name='especialidades',
            field=models.ManyToManyField(related_name='profesionales', to='app_principal.especialidades'),
        ),
    ]