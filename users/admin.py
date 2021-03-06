# users/admin.py
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
#from django.contrib.auth.models import User

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username','image','date_joined']

    fieldsets = UserAdmin.fieldsets + (
            ('Profile', {'fields': ('image',)}),
    )

#admin.site.unregister(User)
admin.site.register(CustomUser, CustomUserAdmin)

