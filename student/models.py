from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
section_choice=['CSE-IS','CSE-NS','CSE-CORE','IT']
year_choice=['First Year','Second Year','Third Year','Fourth Year']


class MyStaffManager(BaseUserManager):
    def create_user(self,id,password):
        if not id:
            raise ValueError("id is required")
        if not password:
            raise ValueError("password required")
        user = self.model(
                          id=id,

        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self,id,password):
        user = self.create_user(
                          id=id,
                          password=password,
        )
        user.is_admin=True
        user.is_staff=True
        user.is_superuser=True

        user.save(using=self._db)
        return user





class Staff(AbstractBaseUser):
    id=models.IntegerField(unique=True,primary_key=True)
    password=models.CharField(max_length=100)
    is_admin =models.BooleanField(default=True)
    is_staff=models.BooleanField(default=True)
    is_superuser=models.BooleanField(default=True)
    is_teacher=models.BooleanField(default=False)

    USERNAME_FIELD = 'id'
    REQUIRED_FIELDS=[]
    objects=MyStaffManager()

    def __str__(self):
        return str(self.id)
    def has_perm(self,perm,obj=None):
        return self.is_admin
    def has_module_perms(self,app_label):
        return True
class Student(models.Model):
    staff=models.OneToOneField(Staff,on_delete=models.CASCADE,null=True,related_name='student_profile')
    stud_name=models.CharField(max_length=200)
    section=models.IntegerField(choices=((i,x) for i,x in enumerate(section_choice)),default=0)
    year = models.IntegerField(choices=((i,x) for i,x in enumerate(year_choice)),default=0)
    def __str__(self):
        return self.stud_name
