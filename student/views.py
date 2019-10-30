from django.shortcuts import render,redirect,render_to_response
from .forms import StudentForm,StaffForm
from .models import Staff,Student
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.http import HttpResponseRedirect,HttpResponse
# Create your views here.
def student_login(request):
    logout(request)
    id = password = ''
    if request.POST:
        id = request.POST['rollnum']
        password = request.POST['password']
        if id:
            user = authenticate(id=id, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(f'student_info/{id}/')
            else:
                return HttpResponse("INVALID PASSWORD")

    return render(request,'student_login.html')




def student_info(request,id):
    return render(request,'stud_info.html',{'id':id})

def student_register(request):
    student_form=StudentForm()
    staff_form=StaffForm()
    if request.method=='POST':
        student_form=StudentForm(request.POST)
        staff_form=StaffForm(request.POST)
        if staff_form.is_valid() and student_form.is_valid():
            newstaff=staff_form.save()
            newstudent=student_form.save(commit=False)
            newstudent.staff=newstaff
            newstudent.save()
            return HttpResponseRedirect('student_login')
    else:
        staff_form = StaffForm()
        student_form = StudentForm()



    context={
             'form':staff_form,'form2':student_form
    }
    return render(request,'student_register.html',context)
