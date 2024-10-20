# Generated by Django 5.1.1 on 2024-10-20 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vav', '0004_alter_alquilerventa_puntos_ganados_alter_video_ano_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='precio_alquiler',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=6),
        ),
        migrations.AddField(
            model_name='video',
            name='precio_venta',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='video',
            name='ano',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='video',
            name='duracion',
            field=models.IntegerField(),
        ),
    ]
