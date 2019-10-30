from django.db import models
from student.models import Staff
department_choice=['Maths','Comp','Music']


class Teacher(models.Model):
    staff=models.OneToOneField(Staff,on_delete=models.CASCADE,related_name='teacher_profile')
    teacher_name=models.CharField(max_length=200)
    department=models.IntegerField(choices=((i,x) for i,x in enumerate(department_choice)),default=0)

    def __str__(self):
        return self.teacher_name
class Notice(models.Model):
    notice=models.CharField(max_length=500)
    date_published=models.DateField(auto_now=True)

    def __str__(self):
        return str(self.notice)
