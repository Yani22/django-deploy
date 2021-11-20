from datetime import date
from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import CharField, EmailField

# Create your models here.
class Program(models.Model):
    PROGRAM_TYPE = (
        ('Nursing Program', 'Nursing Program'),
        ('Hospitality Management Program', 'Hospitality Management Program'),
        ('Tourism Management Program', 'Tourism Management Program'),
        ('Accountancy Program', 'Accountancy Program'),
        ('Liberal Arts Program', 'Liberal Arts Program'),
        ('Criminology Program', 'Criminology Program'),
        ('Business Administration Program', 'Business Administration Program'),
        ('Civil Engineering Program', 'Civil Engineering Program'),
        ('Elementary Education Program', 'Elementary Education Program'),
        ('Secondary Education Program', 'Secondary Education Program'),
        ('Computer Science Program', 'Computer Science Program'),
        ('Faculty Program', 'Faculty Program'),
        ('Research Office Program', 'Research Office Program'),
    )
    program_type = models.CharField(max_length=31,  choices=PROGRAM_TYPE)
    program_logo = models.ImageField(upload_to='images/', null=True)

    def __str__(self):
        return self.program_type

class EndUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    program = models.ForeignKey(Program, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = EmailField(null=True)
    contact_no = CharField(max_length=11, null=True)
    full_address = models.CharField(max_length=200, null=True)
    profile_image = models.ImageField(upload_to='images/', null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

class ResearchOutput(models.Model):
    title = models.CharField(max_length=100)
    author = models.ManyToManyField(EndUser)
    file = models.FileField(upload_to='documents/', null=True)
    image = models.ImageField(upload_to='images/', null=True)
    date_created = models.DateField(("Date"), default=date.today)

    def __str__(self):
        return self.title