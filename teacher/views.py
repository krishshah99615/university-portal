from django.shortcuts import render

# Create your views here.
def teacher_login(request):
    return render(request,'teacher_login.html')
def teacher_dashboard(request):
    return render(request,'teacher_dashboard.html')
