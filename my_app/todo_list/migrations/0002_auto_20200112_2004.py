# Generated by Django 3.0.2 on 2020-01-12 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listitem',
            name='of_list',
            field=models.CharField(default=None, max_length=50),
        ),
    ]
