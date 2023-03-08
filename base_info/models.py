from django.db import models

# Create your models here.

class Citizenship(models.Model):
    citizens=models.CharField(max_length=100,verbose_name='Citizenship')
    
    def __str__(self):
        return self.citizens

class States(models.Model):
    state=models.CharField(max_length=50,verbose_name='States')
    
    def __str__(self):
        return self.state

class Regions(models.Model):
    region=models.CharField(max_length=50,verbose_name='Regions')
    states=models.ForeignKey(States,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.region

class Districts(models.Model):
    district=models.CharField(max_length=20,verbose_name='districts')
    regions=models.ForeignKey(Regions,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.district

class InstitutionType(models.Model):
    type=models.CharField(max_length=50,verbose_name='Institutions types')
    
    def __str__(self):
        return self.type

class Institutions(models.Model):
    institution=models.CharField(max_length=100,verbose_name='Educational Institutions')
    type=models.ForeignKey(InstitutionType,on_delete=models.CASCADE)
    region=models.ForeignKey(Regions,on_delete=models.CASCADE)
    state=models.ForeignKey(States,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.institution
