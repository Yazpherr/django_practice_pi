# Generated by Django 5.1 on 2024-08-29 14:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("gestionPedidos", "0002_alter_clientes_email"),
    ]

    operations = [
        migrations.AlterField(
            model_name="clientes",
            name="direccion",
            field=models.CharField(max_length=50, verbose_name="La direccion"),
        ),
    ]
