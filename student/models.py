from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
section_choice=['CSE-NS']
year_choice=['Third Year']


class MyStaffManager(BaseUserManager):
    def create_user(self, id, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not id:
            raise ValueError('Users must have an id ')

        user = self.model(
            id=id,

        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, id,  password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(id,
            password=password,

        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class Staff(AbstractBaseUser):
    id=models.IntegerField(unique=True,primary_key=True)
    password=models.CharField(max_length=100)
    is_teacher=models.BooleanField(default=False)
    is_admin =models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)


    objects = MyStaffManager()

    USERNAME_FIELD = 'id'
    REQUIRED_FIELDS = []

    def get_full_name(self):
        # The user is identified by their email address
        return self.id

    def get_short_name(self):
        # The user is identified by their email address
        return self.id

    def __str__(self):              # __unicode__ on Python 2
        return str(self.id)

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin














class Student(models.Model):
    staff=models.OneToOneField(Staff,on_delete=models.CASCADE,null=True,related_name='student_profile')
    stud_name=models.CharField(max_length=200)
    section=models.IntegerField(choices=((i,x) for i,x in enumerate(section_choice)),default=0)
    year = models.IntegerField(choices=((i,x) for i,x in enumerate(year_choice)),default=0)
    def __str__(self):
        return str(self.stud_name)
class Marks(models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE,related_name='mark_profile')
    s1=models.IntegerField(default=0)
    s2=models.IntegerField(default=0)
    s3=models.IntegerField(default=0)
    s4=models.IntegerField(default=0)
    s5=models.IntegerField(default=0)
class Attendence(models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE,related_name='attendence_profile')
    s1=models.IntegerField(default=0)
    s2=models.IntegerField(default=0)
    s3=models.IntegerField(default=0)
    s4=models.IntegerField(default=0)
    s5=models.IntegerField(default=0)
