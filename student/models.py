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
                          password=password,
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
    name=models.CharField(max_length=200)
    id=models.IntegerField(unique=True,primary_key=True)
    year = models.IntegerField(choices=((i,x) for i,x in enumerate(year_choice) ),default=3)
    section=models.IntegerField(choices=((i,x) for i,x in enumerate(section_choice) ),default=3)
    password=models.CharField(max_length=100)
    is_admin =models.BooleanField(default=True)
    is_staff=models.BooleanField(default=True)
    is_superuser=models.BooleanField(default=True)
    is_teacher=models.BooleanField(default=False)

    USERNAME_FIELD = 'id'
    REQUIRED_FIELDS=['password']
    objects=MyStaffManager()

    def __str__(self):
        return self.name
    def has_perm(self,perm,obj=None):
        return self.is_admin
    def has_module_perms(self,app_label):
        return True
