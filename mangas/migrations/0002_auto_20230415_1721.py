# Generated by Django 3.1.3 on 2023-04-15 23:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mangas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manga',
            name='lanzamientomanga',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
