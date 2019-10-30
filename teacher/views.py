from django.shortcuts import render,redirect,render_to_response
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.http import HttpResponseRedirect,HttpResponse
from .models import Notice
def notice(request):
    if request.POST:
        n = request.POST['notice']
        obj=Notice(notice=n)
        obj.save()

        return render(request,'teacher_dashboard.html')
    return render(request,'noticeform.html')
# Create your views here.
def teacher_login(request):
    logout(request)
    id = password = ''
    if request.POST:
        id = request.POST['id']
        password = request.POST['password']
        if id:
            user = authenticate(id=id, password=password)
            if user is not None:
                if user.is_active and user.is_teacher:
                    login(request, user)
                    return HttpResponseRedirect(f'teacher_dashboard/{id}/')
            else:
                return HttpResponse("INVALID PASSWORD")

    return render(request,'teacher_login.html')


def teacher_dashboard(request,id):
    return render(request,'teacher_dashboard.html')
