from django.contrib import admin

# Register your models here.

from personal_info.models import PersonalInfo , PermamentAddress , GraduatedEdu

class UserAdmin(admin.ModelAdmin):
    ordering=['id']
    list_display=(
        'first_name',
        
    )

admin.site.register(PersonalInfo)
admin.site.register(PermamentAddress)
admin.site.register(GraduatedEdu)