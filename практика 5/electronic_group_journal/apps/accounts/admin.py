from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (("Данные журнала", {"fields": ("full_name", "role", "phone")}),)
    add_fieldsets = UserAdmin.add_fieldsets + (("Данные журнала", {"fields": ("full_name", "role", "phone")}),)
    list_display = ("username", "full_name", "email", "role", "is_active")
    list_filter = ("role", "is_active")
    search_fields = ("username", "full_name", "email")
