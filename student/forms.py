from django import forms
from .models import Staff,Student
class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ('id', 'password')

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('stud_name', 'section','year')
