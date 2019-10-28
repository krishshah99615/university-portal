from django.shortcuts import render
from .forms import StudentForm
# Create your views here.
def student_login(request):
    return render(request,'student_login.html')
def student_register(request):
    context={
             'form':StudentForm()
    }
    return render(request,'student_register.html',context)
