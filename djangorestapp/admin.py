from django.contrib import admin

# Register your models here.

from djangorestapp.models import User,PhoneOTP

class UserAdmin(admin.ModelAdmin):
    ordering=['id']
    list_display=(
        ['phone']
    )

admin.site.register(User,UserAdmin)
admin.site.register(PhoneOTP)
# admin.site.register(Actor)
# admin.site.register(Movie)
# admin.site.register(Comment)