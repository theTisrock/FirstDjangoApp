# Generated by Django 3.0.2 on 2020-01-12 20:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0002_auto_20200112_2004'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listitem',
            name='of_list',
        ),
    ]
