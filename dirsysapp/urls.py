from django.urls import path
from . import views

app_name = 'reports'

urlpatterns = [
    path('dashboard/', views.home),
    path('add_research/', views.add_research),
    path('reports_researcher/<str:pk>', views.reports_researcher, name='reports_researcher'),
    path('reports_faculty/<str:pk>', views.reports_faculty, name='reports_faculty'),
    path('reports_student/<str:pk>', views.reports_student, name='reports_student'),
    path('reports_program/<str:pk>', views.reports_program, name='reports_program'),
    path('reports_research_output/<str:pk>', views.reports_research_output, name='reports_research_output'),
    path('reports_authors_and_titles/<str:pk>', views.reports_authors_titles, name='reports_authors_titles'),
    path('all_faculty/', views.all_faculty, name='all_faculty'),
    path('all_student/', views.all_student, name='all_student'),
    path('all_program/', views.all_program, name='all_program'),
    path('all_research_output/', views.all_research_output, name='all_research_output'),
    path('all_researcher/', views.all_researcher, name='all_researcher'),
    path('all_authors_and_titles/', views.all_authors_titles, name='all_authors_titles'),
]