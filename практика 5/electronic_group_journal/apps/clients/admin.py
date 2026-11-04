from django.contrib import admin
from .models import StudyGroup, Student

@admin.register(StudyGroup)
class StudyGroupAdmin(admin.ModelAdmin):
    list_display = ("name", "course", "specialty", "curator")
    list_filter = ("course",)
    search_fields = ("name", "specialty")

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("user", "group", "student_number", "admission_year")
    list_filter = ("group", "admission_year")
    search_fields = ("user__full_name", "student_number")
