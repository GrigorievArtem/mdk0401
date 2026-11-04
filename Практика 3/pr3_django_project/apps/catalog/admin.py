from django.contrib import admin
from .models import Location, Category, Vendor, Model

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ("name", "address")
    search_fields = ("name", "address")

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)

@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ("name", "contact_person", "phone", "email")
    search_fields = ("name", "contact_person", "phone", "email")

@admin.register(Model)
class ModelAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "vendor", "location", "created_at")
    list_filter = ("category", "vendor", "location")
    search_fields = ("name", "description")
