# Generated by Django 5.0.4 on 2024-05-26 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VENTAS', '0003_remove_pedido_fechapedido'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='pais',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='provincia',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='telefono',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]