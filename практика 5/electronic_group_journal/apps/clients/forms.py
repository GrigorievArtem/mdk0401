from django import forms
from .models import StudyGroup, Student

class StudyGroupForm(forms.ModelForm):
    class Meta:
        model = StudyGroup
        fields = ["name", "course", "specialty", "curator"]

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["user", "group", "student_number", "admission_year"]
