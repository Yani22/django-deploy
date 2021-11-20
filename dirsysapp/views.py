from django.contrib.auth.models import Group
from django.shortcuts import render
from .forms import *
from .models import *
from django.contrib import messages
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q, query
from operator import attrgetter

# Create your views here.
def home(request): 
    end_user = EndUser.objects.all()
    res_out = ResearchOutput.objects.all()
    context = {
        "end_user": end_user,
        "res_out": res_out,
    }
    return render(request, "main/home.html", context)

def add_research(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, ("Research successfully saved."))
    else:
        form = UploadForm()
    context = {
        "form": form,
    }
    return render(request, "main/add_research.html", context)

def reports_researcher(request, pk):
    end_user = EndUser.objects.filter(id = pk)
    res_out = ResearchOutput.objects.all().order_by('-date_created')
    context = {
        "end_user": end_user,
        "res_out": res_out,
    }
    return render(request, "reports/researcher.html", context)

def reports_faculty(request, pk):
    res_out = ResearchOutput.objects.filter(id = pk)
    context = {
        "res_out": res_out,
    }
    return render(request, "reports/faculty.html", context)

def reports_student(request, pk):
    res_out = ResearchOutput.objects.filter(id = pk)
    context = {
        "res_out": res_out,
    }
    return render(request, "reports/student.html", context)

def reports_program(request, pk):
    res_out = ResearchOutput.objects.filter(id = pk)
    context = {
        "res_out": res_out,
    }
    return render(request, "reports/program.html", context)

def reports_research_output(request, pk):
    res_out = ResearchOutput.objects.filter(id = pk)
    context = {
        "res_out": res_out,
    }
    return render(request, "reports/research_output.html", context)

def reports_authors_titles(request, pk):
    res_out = ResearchOutput.objects.filter(id = pk)
    context = {
        "res_out": res_out,
    }
    return render(request, "reports/authors_titles.html", context)


#### START ####
def all_researcher(request):
    BLOG_POSTS_PER_PAGE = 12
    end_user = EndUser.objects.all()
    context = {
        "end_user": end_user,
    }
    
    query = ""
    if request.GET:
        query = request.GET.get('q', '')
        context['query'] = str(query)

    end_user_post = sorted(get_researcher_queryset(query), key=attrgetter('email'), reverse=True)
    
    page = request.GET.get('page', 1)
    end_user_post_paginator = Paginator(end_user_post, BLOG_POSTS_PER_PAGE)
    try:
        end_user_post = end_user_post_paginator.page(page)
    except PageNotAnInteger:
        end_user_post = end_user_post_paginator.page(BLOG_POSTS_PER_PAGE)
    except EmptyPage:
        end_user_post = end_user_post_paginator.page(end_user_post_paginator.num_pages)

    context['end_user_post'] = end_user_post
    return render(request, "all/all_researcher.html", context)

def get_researcher_queryset(query=None):
    queryset = []
    queries = query.split(" ") #python install 2021 = [python, install, 2021]
    for q in queries:
        researchers = EndUser.objects.filter(
            Q(first_name__icontains=q) |
            Q(middle_name__icontains=q) |
            Q(last_name__icontains=q)
        ).distinct()

        for researcher in researchers:
            queryset.append(researcher)

    return list(set(queryset))
#### END ####

#### START ####
def all_faculty(request):
    BLOG_POSTS_PER_PAGE = 12
    res_out = ResearchOutput.objects.all()
    context = {
        "res_out": res_out,
    }

    query = ""
    if request.GET:
        query = request.GET.get('q', '')
        context['query'] = str(query)
    faculty_user_post = sorted(get_faculty_queryset(query), key=attrgetter('date_created'), reverse=True)
    
    page = request.GET.get('page', 1)
    faculty_user_post_paginator = Paginator(faculty_user_post, BLOG_POSTS_PER_PAGE)
    try:
        faculty_user_post = faculty_user_post_paginator.page(page)
    except PageNotAnInteger:
        faculty_user_post = faculty_user_post_paginator.page(BLOG_POSTS_PER_PAGE)
    except EmptyPage:
        faculty_user_post = faculty_user_post_paginator.page(faculty_user_post_paginator.num_pages)
    
    context['faculty_user_post'] = faculty_user_post
    return render(request, "all/all_faculty.html", context)

def get_faculty_queryset(query=None):
    queryset = []
    queries = query.split(" ") #python install 2021 = [python, install, 2021]
    
    for q in queries:
        facultys = ResearchOutput.objects.filter(
            Q(title__icontains=q) |
            Q(author__first_name__icontains=q) |
            Q(author__middle_name__icontains=q) |
            Q(author__last_name__icontains=q)
        ).distinct()

        for faculty in facultys:
            queryset.append(faculty)

    return list(set(queryset))
##### END ####

#### START ####
def all_student(request):
    BLOG_POSTS_PER_PAGE = 12
    res_out = ResearchOutput.objects.all()
    context = {
        "res_out": res_out,
    }

    query = ""
    if request.GET:
        query = request.GET.get('q', '')
        context['query'] = str(query)
    student_user_post = sorted(get_student_queryset(query), key=attrgetter('date_created'), reverse=True)
    page = request.GET.get('page', 1)
    student_user_post_paginator = Paginator(student_user_post, BLOG_POSTS_PER_PAGE)
    try:
        student_user_post = student_user_post_paginator.page(page)
    except PageNotAnInteger:
        student_user_post = student_user_post_paginator.page(BLOG_POSTS_PER_PAGE)
    except EmptyPage:
        student_user_post = student_user_post_paginator.page(student_user_post_paginator.num_pages)
    
    context['student_user_post'] = student_user_post
    return render(request, "all/all_student.html", context)

def get_student_queryset(query=None):
    queryset = []
    queries = query.split(" ") #python install 2021 = [python, install, 2021]
    
    for q in queries:
        students = ResearchOutput.objects.filter(
            Q(title__icontains=q) |
            Q(author__first_name__icontains=q) |
            Q(author__middle_name__icontains=q) |
            Q(author__last_name__icontains=q)
        ).distinct()

        for student in students:
            queryset.append(student)

    return list(set(queryset))
##### END ####

#### START ####
def all_program(request):
    BLOG_POSTS_PER_PAGE = 12
    res_out = ResearchOutput.objects.all()
    context = {
        "res_out": res_out,
    }

    query = ""
    if request.GET:
        query = request.GET.get('q', '')
        context['query'] = str(query)
    program_user_post = sorted(get_program_queryset(query), key=attrgetter('date_created'), reverse=True)
    page = request.GET.get('page', 1)
    program_user_post_paginator = Paginator(program_user_post, BLOG_POSTS_PER_PAGE)
    try:
        program_user_post = program_user_post_paginator.page(page)
    except PageNotAnInteger:
        program_user_post = program_user_post_paginator.page(BLOG_POSTS_PER_PAGE)
    except EmptyPage:
        program_user_post = program_user_post_paginator.page(program_user_post_paginator.num_pages)
    
    context['program_user_post'] = program_user_post
    return render(request, "all/all_program.html", context)

def get_program_queryset(query=None):
    queryset = []
    queries = query.split(" ") #python install 2021 = [python, install, 2021]
    
    for q in queries:
        programs = ResearchOutput.objects.filter(
            Q(title__icontains=q) |
            Q(author__program__program_type__icontains=q)
        ).distinct()

        for program in programs:
            queryset.append(program)

    return list(set(queryset))
##### END ####

#### START ####
def all_research_output(request):
    BLOG_POSTS_PER_PAGE = 12
    res_out = ResearchOutput.objects.all()
    context = {
        "res_out": res_out,
    }

    query = ""
    if request.GET:
        query = request.GET.get('q', '')
        context['query'] = str(query)
    research_user_post = sorted(get_research_queryset(query), key=attrgetter('date_created'), reverse=True)
    page = request.GET.get('page', 1)
    research_user_post_paginator = Paginator(research_user_post, BLOG_POSTS_PER_PAGE)
    try:
        research_user_post = research_user_post_paginator.page(page)
    except PageNotAnInteger:
        research_user_post = research_user_post_paginator.page(BLOG_POSTS_PER_PAGE)
    except EmptyPage:
        research_user_post = research_user_post_paginator.page(research_user_post_paginator.num_pages)
    
    context['research_user_post'] = research_user_post
    return render(request, "all/all_researchOutput.html", context)

def get_research_queryset(query=None):
    queryset = []
    queries = query.split(" ") #python install 2021 = [python, install, 2021]
    
    for q in queries:
        researchs = ResearchOutput.objects.filter(
            Q(title__icontains=q) |
            Q(author__first_name__icontains=q) |
            Q(author__middle_name__icontains=q) |
            Q(author__last_name__icontains=q)
        ).distinct()

        for research in researchs:
            queryset.append(research)

    return list(set(queryset))
##### END ####

#### START ####
def all_authors_titles(request):
    BLOG_POSTS_PER_PAGE = 12
    end_user = EndUser.objects.all()
    res_out = ResearchOutput.objects.all()
    context = {
        "end_user": end_user,
        "res_out": res_out,
    }

    query = ""
    if request.GET:
        query = request.GET.get('q', '')
        context['query'] = str(query)
    auth_title_user_post = sorted(get_auth_title_queryset(query), key=attrgetter('date_created'), reverse=True)
    page = request.GET.get('page', 1)
    auth_title_user_post_paginator = Paginator(auth_title_user_post, BLOG_POSTS_PER_PAGE)
    try:
        auth_title_user_post = auth_title_user_post_paginator.page(page)
    except PageNotAnInteger:
        auth_title_user_post = auth_title_user_post_paginator.page(BLOG_POSTS_PER_PAGE)
    except EmptyPage:
        auth_title_user_post = auth_title_user_post_paginator.page(auth_title_user_post_paginator.num_pages)
    
    context['auth_title_user_post'] = auth_title_user_post
    return render(request, "all/all_authorsTitles.html", context)

def get_auth_title_queryset(query=None):
    queryset = []
    queries = query.split(" ") #python install 2021 = [python, install, 2021]
    
    for q in queries:
        auth_titles = ResearchOutput.objects.filter(
            Q(title__icontains=q) |
            Q(author__first_name__icontains=q) |
            Q(author__middle_name__icontains=q) |
            Q(author__last_name__icontains=q)
        ).distinct()

        for auth_title in auth_titles:
            queryset.append(auth_title)

    return list(set(queryset))
##### END ####