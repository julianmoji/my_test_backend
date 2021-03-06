# Generated by Django 2.2.13 on 2021-07-01 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='eye_color',
            field=models.CharField(blank=True, choices=[('ebc', 'Negro'), ('ebr', 'Café'), ('eyl', 'Amarillo'), ('erd', 'Rojo'), ('egr', 'Verde'), ('epu', 'Morado'), ('euk', 'Desconocido')], max_length=32),
        ),
        migrations.AlterField(
            model_name='people',
            name='hair_color',
            field=models.CharField(blank=True, choices=[('bc', 'Negro'), ('br', 'Café'), ('bl', 'Rubio'), ('rd', 'Rojo'), ('wh', 'Blanco'), ('bd', 'Calvo')], max_length=32),
        ),
    ]
