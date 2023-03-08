from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.validators import RegexValidator

# Create your models here.

# class Actor(models.Model):
#     first_name=models.CharField(max_length=20,verbose_name='first_name')
#     last_name=models.CharField(max_length=20,verbose_name='Last_name')
#     gender=models.CharField(max_length=10,verbose_name='Gender')
#     # photos=models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True , verbose_name="Rasm")
    
#     def __str__(self):
#         return self.first_name


# class Movie(models.Model):
#     name=models.CharField(max_length=50,verbose_name='Movie name')
#     genre=models.CharField(max_length=50,verbose_name='Genre')
#     year=models.DateField(verbose_name='Reliesed year')
#     # photos=models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True , verbose_name="Rasm")
#     actor=models.ManyToManyField(Actor)
    
#     def __str__(self):
#         return self.name
    


    

class UserManager(BaseUserManager):
    def create_user(self,phone,password=None,is_staff=False,is_active=True,is_admin=False):
        if not phone:
            raise ValueError('Users must have a phone number')
        if not password:
            raise ValueError('Users must have a password')
        
        user_obj=self.model(phone=phone)
        user_obj.set_password(password)
        # user_obj.username=username
        user_obj.staff=is_staff
        user_obj.admin=is_admin
        user_obj.active=is_active
        user_obj.save(using=self._db)
        return user_obj
    
    def create_staffuser(self,phone,password=None):
        user=self.create_user(phone,password=password,is_staff=True)
        return user
    
    def create_superuser(self, phone, password=None):
        user = self.create_user(phone=phone,password=password,is_staff=True,is_admin=True)
        return user
    

class User(AbstractBaseUser):
    phone_regex=RegexValidator(regex=r'^\+?1?\d{9,14}$',message="Phone number nust be entered in the format: '+998906417999'. Up to 14 digits allowed")
    phone=models.CharField(validators=[phone_regex],max_length=20,unique=True)
    # photos=models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True , verbose_name="Rasm")
    first_login=models.BooleanField(default=False)
    active=models.BooleanField(default=True)
    staff=models.BooleanField(default=False)
    admin=models.BooleanField(default=False)
    # comment=models.ForeignKey(Comment,on_delete=models.CASCADE)
    username=None #models.CharField(max_length=20,blank=True,verbose_name='username')
    USERNAME_FIELD='phone'
    REQUIRED_FIELDS=[]
    
    objects=UserManager()
    
    def __str__(self):
        return self.phone
    
    def get_full_name(self):
        if self.phone:
            return self.phone
    
    def get_short_name(self):
        return self.phone

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
    
    @property
    def is_staff(self):
        return self.staff
    
    @property
    def is_admin(self):
        return self.admin
    
    @property
    def is_active(self):
        return self.active

class PhoneOTP(models.Model):
    phone_regex=RegexValidator(regex=r'^\+?1?\d{9,14}$',message="Phone number nust be entered in the format: '+998906417999'. Up to 14 digits allowed")
    phone=models.CharField(validators=[phone_regex],max_length=20,unique=True)
    otp=models.CharField(max_length=6,blank=True,null=True)
    validated=models.BooleanField(default=False,help_text='if it is true,that means user have validate otp correctly i second API')
    
    def __str__(self):
        return str(self.phone) + ' if sent ' + str(self.otp)


# class Comment(models.Model):
#     comment=models.TextField(max_length=500,verbose_name='Add comment to movie')
#     created_at=models.DateTimeField(auto_now_add=True)
#     movie=models.ForeignKey(Movie,on_delete=models.CASCADE)
#     user=models.ForeignKey(User,on_delete=models.CASCADE)
    
#     def __str__(self):
#         return self.user.phone
    