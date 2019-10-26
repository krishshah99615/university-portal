
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',view=views.home,name='home'),
    path('student/',include('student.urls')),
    path('teacher/',include('teacher.urls')),
]
