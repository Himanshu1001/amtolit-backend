from django.contrib import admin
from django.apps import apps
from .models import *
from django.contrib.auth.models import User

app = apps.get_app_config('polls')

class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name')
    list_filter = ('is_staff', 'is_superuser')

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Question)
admin.site.register(TextAnswer)
admin.site.register(Custom_User)
admin.site.register(Choice)
admin.site.register(PhoneOTP)