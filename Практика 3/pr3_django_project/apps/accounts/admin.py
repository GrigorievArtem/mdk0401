from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ("Дополнительная информация", {"fields": ("full_name", "phone", "position")}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Дополнительная информация", {"fields": ("full_name", "phone", "position")}),
    )
    list_display = ("username", "full_name", "email", "phone", "position", "is_staff")
    search_fields = ("username", "full_name", "email", "phone")
