from django.db import models
from django.conf import settings
from apps.clients.models import Student, StudyGroup
from apps.catalog.models import Subject

class Lesson(models.Model):
    group = models.ForeignKey(StudyGroup, on_delete=models.CASCADE,
                              related_name="lessons", verbose_name="Группа")
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT,
                                related_name="lessons", verbose_name="Дисциплина")
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT,
                                related_name="lessons", verbose_name="Преподаватель")
    lesson_date = models.DateField("Дата занятия")
    topic = models.CharField("Тема занятия", max_length=200)
    room = models.CharField("Аудитория", max_length=30, blank=True)

    class Meta:
        verbose_name = "Занятие"
        verbose_name_plural = "Занятия"
        ordering = ["-lesson_date"]

    def __str__(self):
        return f"{self.lesson_date}: {self.group} — {self.subject}"


class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE,
                                related_name="grades", verbose_name="Студент")
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE,
                               related_name="grades", verbose_name="Занятие")
    value = models.PositiveSmallIntegerField("Оценка")
    comment = models.CharField("Комментарий", max_length=250, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Оценка"
        verbose_name_plural = "Оценки"
        constraints = [models.UniqueConstraint(fields=["student", "lesson"],
                                                name="one_grade_per_student_lesson")]
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.student}: {self.value}"

    def clean(self):
        from django.core.exceptions import ValidationError
        if self.value < 1 or self.value > 5:
            raise ValidationError({"value": "Оценка должна быть от 1 до 5."})
        if self.student_id and self.lesson_id and self.student.group_id != self.lesson.group_id:
            raise ValidationError("Студент должен состоять в группе занятия.")


class Attendance(models.Model):
    class Status(models.TextChoices):
        PRESENT = "present", "Присутствовал"
        ABSENT = "absent", "Отсутствовал"
        LATE = "late", "Опоздал"
        EXCUSED = "excused", "Уважительная причина"

    student = models.ForeignKey(Student, on_delete=models.CASCADE,
                                 related_name="attendance", verbose_name="Студент")
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE,
                               related_name="attendance", verbose_name="Занятие")
    status = models.CharField("Статус", max_length=10, choices=Status.choices)
    note = models.CharField("Примечание", max_length=250, blank=True)

    class Meta:
        verbose_name = "Посещаемость"
        verbose_name_plural = "Посещаемость"
        constraints = [models.UniqueConstraint(fields=["student", "lesson"],
                                                name="one_attendance_per_student_lesson")]

    def __str__(self):
        return f"{self.student}: {self.get_status_display()}"
