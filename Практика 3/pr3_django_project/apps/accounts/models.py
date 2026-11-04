from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    full_name = models.CharField("ФИО", max_length=150, blank=True)
    phone = models.CharField("Телефон", max_length=30, blank=True)
    position = models.CharField("Должность", max_length=100, blank=True)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.full_name or self.username
