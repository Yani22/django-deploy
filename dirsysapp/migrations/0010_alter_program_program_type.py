# Generated by Django 3.2.9 on 2021-11-13 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dirsysapp', '0009_auto_20211113_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='program',
            name='program_type',
            field=models.CharField(choices=[('BSN', 'Bachelor of Science in Nursing'), ('BSHM', 'Bachelor of Science in Hospitality Management'), ('BSTM', 'Bachelor of Science in Tourism Management'), ('BSA', 'Bachelor of Science in Accountanct'), ('AB', 'Bachelor of Arts in English'), ('BSCrim', 'Bachelor of Science in Criminology'), ('BSBA', 'Bachelor of Science in Business Administration'), ('BSCE', 'Bachelor of Science in Civil Engineering'), ('BEED', 'Bachelor of Elementary Education'), ('BSED', 'Bachelor of Secondary Education'), ('BSCS', 'Bachelor of Science in Computer Science')], max_length=6),
        ),
    ]
