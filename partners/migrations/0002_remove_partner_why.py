# Generated by Django 5.0.6 on 2024-09-11 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('partners', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='partner',
            name='why',
        ),
    ]
