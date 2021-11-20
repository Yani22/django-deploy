from django.contrib.auth.models import User
from django import forms
from dirsysapp.models import *
from django.contrib.auth.forms import UserCreationForm, UsernameField

class RegisterForm(UserCreationForm):
    type = (('Student', 'Student'), ('Faculty', 'Faculty'), ('Research Office', 'Research Office'))
    position = forms.ChoiceField(choices=type)
    username = UsernameField(
        label='ID Number',
        widget=forms.TextInput(attrs={'autofocus': True}))

    class Meta:
        model = User
        fields = ["username", "password1", "password2"]

class PersonalRegisterForm(forms.ModelForm):
    first_name = forms.CharField(required=True)
    middle_name = forms.CharField(required=False)
    last_name = forms.CharField(required=True)
    full_address = forms.CharField(required=True)
    email = forms.EmailField()
    contact_no = forms.CharField()
    profile_image = forms.ImageField()

    class Meta:
        model = EndUser
        fields = ["program", "first_name", "middle_name", 
        "last_name", "email", "contact_no", 
        "full_address", "profile_image"]