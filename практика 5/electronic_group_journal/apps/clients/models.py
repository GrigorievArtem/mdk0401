from django.db import models
from django.conf import settings

class StudyGroup(models.Model):
    name = models.CharField("Название группы", max_length=50, unique=True)
    course = models.PositiveSmallIntegerField("Курс", default=1)
    specialty = models.CharField("Специальность", max_length=150, blank=True)
    curator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
                                null=True, blank=True, related_name="curated_groups",
                                verbose_name="Куратор")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Учебная группа"
        verbose_name_plural = "Учебные группы"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Student(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                related_name="student_profile", verbose_name="Учетная запись")
    group = models.ForeignKey(StudyGroup, on_delete=models.PROTECT,
                              related_name="students", verbose_name="Группа")
    student_number = models.CharField("Номер студенческого билета", max_length=30, unique=True)
    admission_year = models.PositiveSmallIntegerField("Год поступления")

    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"
        ordering = ["user__full_name"]

    def __str__(self):
        return self.user.full_name or self.user.username
