from django.contrib import admin
from .models import Lesson, Grade, Attendance

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ("lesson_date", "group", "subject", "teacher", "topic", "room")
    list_filter = ("group", "subject", "teacher", "lesson_date")
    search_fields = ("topic",)

@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ("student", "lesson", "value", "created_at")
    list_filter = ("value", "lesson__subject", "lesson__group")
    search_fields = ("student__user__full_name",)

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ("student", "lesson", "status")
    list_filter = ("status", "lesson__group", "lesson__subject")
    search_fields = ("student__user__full_name",)
