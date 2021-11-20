# Generated by Django 3.2.9 on 2021-11-13 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dirsysapp', '0011_alter_program_program_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='program',
            name='program_type',
            field=models.CharField(choices=[('BSN', 'Nursing Program'), ('BSHM', 'Hospitality Management Program'), ('BSTM', 'Tourism Management Program'), ('BSA', 'Accountancy Program'), ('AB', 'Liberal Arts Program'), ('BSCrim', 'Criminology Program'), ('BSBA', 'Administration Program'), ('BSCE', 'Civil Engineering Program'), ('BEED', 'Elementary Education Program'), ('BSED', 'Secondary Education Program'), ('BSCS', 'Computer Science Program')], max_length=6),
        ),
    ]
