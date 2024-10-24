# Generated by Django 5.1.1 on 2024-10-20 21:08

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vav', '0005_video_precio_alquiler_video_precio_venta_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('alquiler', 'Alquiler'), ('venta', 'Venta')], max_length=10)),
                ('cantidad', models.PositiveIntegerField(default=1)),
                ('fecha_agregado', models.DateTimeField(auto_now_add=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vav.video')),
            ],
        ),
    ]
