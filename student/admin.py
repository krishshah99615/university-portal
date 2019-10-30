from django.contrib import admin
from .models import Staff,Student,Marks,Attendence

admin.site.register(Student)
admin.site.register(Staff)
admin.site.register(Marks)
admin.site.register(Attendence)

# Register your models here.
