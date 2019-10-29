from django.shortcuts import render
from .forms import StudentForm,StaffForm
from .models import Staff,Student
# Create your views here.
def student_login(request):
    return render(request,'student_login.html')
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



    context={
             'form':staff_form,'form2':student_form
    }
    return render(request,'student_register.html',context)
