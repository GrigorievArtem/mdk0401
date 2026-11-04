from django.db import models
from django.conf import settings

class Subject(models.Model):
    name = models.CharField("Название дисциплины", max_length=120, unique=True)
    description = models.TextField("Описание", blank=True)
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT,
                                 related_name="subjects", verbose_name="Преподаватель",
                                 limit_choices_to={"role": "teacher"})

    class Meta:
        verbose_name = "Дисциплина"
        verbose_name_plural = "Дисциплины"
        ordering = ["name"]

    def __str__(self):
        return self.name
