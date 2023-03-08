from django.db import models
from dj_rest_auth import app_settings
from djangorestapp.models import User
from base_info.models import Citizenship ,States , Regions , Districts , InstitutionType , Institutions

# Create your models here.

class PersonalInfo(models.Model):
    citizenship=models.ForeignKey(Citizenship,on_delete=models.CASCADE)
    jshshir=models.CharField(max_length=14,verbose_name='Personal identification number of individuals')
    passport_series=models.CharField(max_length=2,verbose_name='Passport series')
    passport_num=models.CharField(max_length=7,verbose_name='Passport number')
    first_name=models.CharField(max_length=20,verbose_name='first_name')
    last_name=models.CharField(max_length=20,verbose_name='Last_name')
    surname=models.CharField(max_length=20,verbose_name='Last_name')
    birth_date=models.DateField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    # ['%Y-%m-%d']
    # phone_number=models.AutoField()
    
    def __str__(self):
        return self.user.phone


class PermamentAddress(models.Model):
    region=models.ForeignKey(Regions,on_delete=models.CASCADE)
    # district=models.ForeignKey(Regions.objects.get('district'),on_delete=models.CASCADE)
    district=models.ForeignKey(Districts,on_delete=models.CASCADE)
    address=models.TextField(max_length=100,verbose_name='Home address')
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.address


class GraduatedEdu(models.Model):
    state=models.ForeignKey(States,on_delete=models.CASCADE)
    region=models.ForeignKey(Regions,on_delete=models.CASCADE)
    district=models.ForeignKey(Districts,on_delete=models.CASCADE)
    graduate_institution_type=models.ForeignKey(InstitutionType,on_delete=models.CASCADE)
    graduate_institution=models.ForeignKey(Institutions,on_delete=models.CASCADE)
    graduated_date=models.DateField()
    doc_ser_num=models.TextField(max_length=20,verbose_name='Document series and number of your graduated Institution')
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.doc_ser_num3

