from django import forms
from .models import Lesson, Grade, Attendance

class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ["group", "subject", "teacher", "lesson_date", "topic", "room"]
        widgets = {"lesson_date": forms.DateInput(attrs={"type": "date"})}

class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ["student", "lesson", "value", "comment"]

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ["student", "lesson", "status", "note"]
