from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Group
from django.contrib import messages

# Create your views here.
def signup(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            position = form.cleaned_data.get('position')
            if position == "Student":
                user = form.save()
                group = Group.objects.get(name="Student")
                user.groups.add(group)
                login(request, user)
                return redirect("/signup_2")
            elif position == "Faculty":
                user = form.save()
                group = Group.objects.get(name="Faculty")
                user.groups.add(group)
                login(request, user)
                return redirect("/signup_2")
            elif position == "Research Office":
                user = form.save()
                group = Group.objects.get(name="Research Office")
                user.groups.add(group)
                login(request, user)
                return redirect("/signup_2")
    else:
        form = RegisterForm()
    
    context = {
        "form": form
    }
    return render(request, "register/register.html", context)

def personal(request):
    if request.method == "POST":
        form = PersonalRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            program = form.cleaned_data.get('program')
            first_name = form.cleaned_data.get('first_name')
            middle_name = form.cleaned_data.get('middle_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            contact_no = form.cleaned_data.get('contact_no')
            full_address = form.cleaned_data.get('full_address')
            profile_image = form.cleaned_data.get('profile_image')
            
            end_user = EndUser()
            end_user.user = request.user
            end_user.program = program
            end_user.first_name = first_name
            end_user.middle_name = middle_name
            end_user.last_name = last_name
            end_user.email = email
            end_user.contact_no = contact_no
            end_user.full_address = full_address
            end_user.profile_image = profile_image

            end_user.save()
            return redirect("/dashboard")
         
    else:
        form = PersonalRegisterForm()
    
    context = {
        "form": form
    }
    return render(request, "register/personal.html", context)

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/dashboard")
        else:
            messages.error(request, ("Please enter a correct username and password. Note that both fields may be case-sensitive."))
            return redirect("/login")
    else:
        return render(request, "register/login.html", {})