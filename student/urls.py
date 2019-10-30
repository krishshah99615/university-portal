
from django.contrib import admin
from django.urls import path
from . import views
app_name='student'
urlpatterns = [

    path('student_login',view=views.student_login,name='student_login'),
    path('student_register',view=views.student_register,name='student_register'),
    path('student_info/<int:id>/',view=views.student_info,name='student_info'),
]
