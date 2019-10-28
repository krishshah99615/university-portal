from django import forms
class StudentForm(forms.Form):
    stud_name=forms.CharField()
    section=forms.IntegerField()
    year=forms.IntegerField()
