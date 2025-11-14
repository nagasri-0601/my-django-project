from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('add/', views.add_student, name='add_student'),
    path('students/', views.show_students, name='show_students'),
]



