from django.shortcuts import render,redirect,render_to_response
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.http import HttpResponseRedirect,HttpResponse
from .models import Notice
from student.models import Staff,Student,Attendence,Marks
def notice(request):
    if request.POST:
        n = request.POST['notice']
        obj=Notice(notice=n)
        obj.save()

        return render(request,'teacher_dashboard.html')
    return render(request,'noticeform.html')


def attend(request):
    list_of_student_id=[]
    list_of_staff=Staff.objects.all()
    for staff in list_of_staff:
        if not staff.is_teacher:
            list_of_student_id.append(staff.id)
    if request.POST:
        student_id=request.POST['student_id']
        days_attended_s1=request.POST['days_attended_s1']
        total_attended_s1=request.POST['total_attended_s1']
        days_attended_s2=request.POST['days_attended_s2']
        total_attended_s2=request.POST['total_attended_s2']
        days_attended_s3=request.POST['days_attended_s3']
        total_attended_s3=request.POST['total_attended_s3']
        days_attended_s4=request.POST['days_attended_s4']
        total_attended_s4=request.POST['total_attended_s4']
        days_attended_s5=request.POST['days_attended_s5']
        total_attended_s5=request.POST['total_attended_s5']
        final1=(int(days_attended_s1)/int(total_attended_s1))*100
        final2=(int(days_attended_s2)/int(total_attended_s2))*100
        final3=(int(days_attended_s3)/int(total_attended_s3))*100
        final4=(int(days_attended_s4)/int(total_attended_s4))*100
        final5=(int(days_attended_s5)/int(total_attended_s5))*100
        Attendence.objects.create(student=Student.objects.get(staff=Staff.objects.get(id=student_id)),
                                  s1=final1,
                                  s2=final2,
                                  s3=final3,
                                  s4=final4,
                                  s5=final5)
        return render(request,'teacher_dashboard.html')
    return render(request,'attendence.html',{'list':list_of_student_id})

def marks(request):
    list_of_student_id=[]
    list_of_staff=Staff.objects.all()
    for staff in list_of_staff:
        if not staff.is_teacher:
            list_of_student_id.append(staff.id)
    if request.POST:
        student_id=request.POST['student_id']
        marks_s1=request.POST['marks_s1']
        total_marks_s1=request.POST['total_marks_s1']
        marks_s2=request.POST['marks_s2']
        total_marks_s2=request.POST['total_marks_s2']
        marks_s3=request.POST['marks_s3']
        total_marks_s3=request.POST['total_marks_s3']
        marks_s4=request.POST['marks_s4']
        total_marks_s4=request.POST['total_marks_s4']
        marks_s5=request.POST['marks_s5']
        total_marks_s5=request.POST['total_marks_s5']
        final1=(int(marks_s1)/int(total_marks_s1))*100
        final2=(int(marks_s2)/int(total_marks_s2))*100
        final3=(int(marks_s3)/int(total_marks_s3))*100
        final4=(int(marks_s4)/int(total_marks_s4))*100
        final5=(int(marks_s5)/int(total_marks_s5))*100
        Marks.objects.create(student=Student.objects.get(staff=Staff.objects.get(id=student_id)),
                                  s1=final1,
                                  s2=final2,
                                  s3=final3,
                                  s4=final4,
                                  s5=final5)
        return render(request,'teacher_dashboard.html')
    return render(request,'marks.html',{'list':list_of_student_id})






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
