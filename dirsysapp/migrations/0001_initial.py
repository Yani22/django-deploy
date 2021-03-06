# Generated by Django 3.2.9 on 2021-11-13 01:44

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EndUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('contact_no', models.CharField(max_length=11, null=True)),
                ('full_address', models.CharField(max_length=200, null=True)),
                ('profile_image', models.ImageField(null=True, upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('program_type', models.CharField(choices=[('BSN', 'BSN'), ('BSHM', 'BSHM'), ('BSTM', 'BSTM'), ('BSN', 'BSN'), ('BSA', 'BSA'), ('AB', 'AB'), ('BSCrim', 'BSCrim'), ('BSBA', 'BSBA'), ('BSCE', 'BSCE'), ('BEED', 'BEED'), ('BSED', 'BSED'), ('BSCS', 'BSCS')], max_length=6)),
                ('program_logo', models.ImageField(null=True, upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='ResearchOutput',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('file', models.FileField(null=True, upload_to='documents/')),
                ('image', models.ImageField(null=True, upload_to='images/')),
                ('date_created', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('author', models.ManyToManyField(to='dirsysapp.EndUser')),
            ],
            options={
                'verbose_name_plural': 'Researches_Outputs',
            },
        ),
        migrations.AddField(
            model_name='enduser',
            name='program',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dirsysapp.program'),
        ),
        migrations.AddField(
            model_name='enduser',
            name='research',
            field=models.ManyToManyField(null=True, related_name='researchoutput', to='dirsysapp.ResearchOutput'),
        ),
        migrations.AddField(
            model_name='enduser',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
