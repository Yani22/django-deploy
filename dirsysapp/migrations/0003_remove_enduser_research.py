# Generated by Django 3.2.9 on 2021-11-13 03:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dirsysapp', '0002_alter_enduser_research'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enduser',
            name='research',
        ),
    ]
