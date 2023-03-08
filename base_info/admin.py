from django.contrib import admin
from base_info.models import Citizenship , States , Regions , Districts , InstitutionType , Institutions
from djangorestapp.models import User
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    ordering=['id']
    list_display=('citizens','state','region','district','type','institution')
    search_fields=('citizens','state','region','district','type','institution') # search qo'shib beradi

admin.site.register(Citizenship)
admin.site.register(States)
admin.site.register(Regions)
admin.site.register(Districts)
admin.site.register(InstitutionType)
admin.site.register(Institutions)
