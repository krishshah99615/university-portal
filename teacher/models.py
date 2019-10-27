from django.db import models

from student.models import Staff
department_choice=['Maths','Comp','Music']
class Teacher(models.Model):
    staff=models.ForeignKey(Staff,on_delete=True)
    teacher_name=models.CharField(max_length=200)
    department=models.IntegerField(choices=((i,x) for i,x in enumerate(department_choice)),default=0)
    
