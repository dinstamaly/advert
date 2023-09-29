from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name="название")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class City(models.Model):
    name = models.CharField(max_length=255, verbose_name="название")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"


class Advert(models.Model):
    created = models.DateTimeField(auto_now=True, verbose_name="дата создание")
    title = models.CharField(max_length=255, verbose_name="заголовок")
    description = models.TextField(verbose_name="описание")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="категория")
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name="город")
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"
