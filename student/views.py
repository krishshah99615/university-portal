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
            user = staff_form.save(commit=False)
            user.save()

            user.student_profile.stud_name = student_form.cleaned_data.get('stud_name')
            user.student_profile.section =  student_form.cleaned_data.get('section')
            user.student_profile.year =  student_form.cleaned_data.get('year')

            user.student_profile.save()



    context={
             'form':staff_form,'form2':student_form
    }
    return render(request,'student_register.html',context)
