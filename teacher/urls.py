
from django.contrib import admin
from django.urls import path
from . import views
app='teacher'
urlpatterns = [
    
    path('teacher_login',view=views.teacher_login,name='teacher_login')
]
