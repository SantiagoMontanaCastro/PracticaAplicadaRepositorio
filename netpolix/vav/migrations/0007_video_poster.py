# Generated by Django 5.1.2 on 2024-10-21 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vav', '0006_carrito'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='poster',
            field=models.ImageField(default=0, upload_to='posters/'),
            preserve_default=False,
        ),
    ]