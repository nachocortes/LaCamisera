# Generated by Django 5.0.4 on 2024-05-26 19:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RRHH', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empleado',
            name='user',
        ),
    ]
