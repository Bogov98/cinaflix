# Generated by Django 4.2.1 on 2023-05-23 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favorito',
            name='rating',
        ),
        migrations.AddField(
            model_name='vista',
            name='rating',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]