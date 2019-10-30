
from django.contrib import admin
from django.urls import path
from . import views
app_name='teacher'
urlpatterns = [

    path('teacher_login',view=views.teacher_login,name='teacher_login'),
    path('teacher_dashboard/<int:id>/',view=views.teacher_dashboard,name='teacher_dashboard'),
    path('teacher_dashboard/notice',view=views.notice,name='notice')
]
