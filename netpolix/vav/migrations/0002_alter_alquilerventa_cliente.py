# Generated by Django 5.1.1 on 2024-10-20 02:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0002_remove_cliente_referido_perfil'),
        ('vav', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alquilerventa',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.perfil'),
        ),
    ]
