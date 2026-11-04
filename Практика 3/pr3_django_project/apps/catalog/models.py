from django.db import models

class Location(models.Model):
    name = models.CharField("Название локации", max_length=150, unique=True)
    address = models.CharField("Адрес", max_length=255, blank=True)

    class Meta:
        verbose_name = "Локация"
        verbose_name_plural = "Локации"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField("Название категории", max_length=100, unique=True)
    description = models.TextField("Описание", blank=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Vendor(models.Model):
    name = models.CharField("Поставщик", max_length=150, unique=True)
    contact_person = models.CharField("Контактное лицо", max_length=150, blank=True)
    phone = models.CharField("Телефон", max_length=30, blank=True)
    email = models.EmailField("Email", blank=True)

    class Meta:
        verbose_name = "Поставщик"
        verbose_name_plural = "Поставщики"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Model(models.Model):
    name = models.CharField("Модель", max_length=150)
    category = models.ForeignKey(Category, on_delete=models.PROTECT,
                                 related_name="models", verbose_name="Категория")
    vendor = models.ForeignKey(Vendor, on_delete=models.PROTECT,
                               related_name="models", verbose_name="Поставщик")
    location = models.ForeignKey(Location, on_delete=models.PROTECT,
                                 related_name="models", verbose_name="Локация")
    description = models.TextField("Описание", blank=True)
    created_at = models.DateTimeField("Создано", auto_now_add=True)

    class Meta:
        verbose_name = "Модель"
        verbose_name_plural = "Модели"
        ordering = ["name"]
        constraints = [
            models.UniqueConstraint(fields=["name", "vendor"],
                                    name="unique_model_per_vendor")
        ]

    def __str__(self):
        return f"{self.vendor}: {self.name}"
