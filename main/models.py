from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(max_length=500, verbose_name="Описание")
    price = models.PositiveIntegerField(verbose_name="Цена")
    image = models.ImageField(upload_to="images/", null=True, blank=True, verbose_name="Изображение")
    amount = models.PositiveIntegerField(verbose_name="Количество")
    place_1 = models.BooleanField(default=False, verbose_name="На складе")
    place_2 = models.BooleanField(default=False, verbose_name="В магазине")

    def __str__(self):
        if self.place_1:
            return f"Название: {self.title}.  Цена: {self.price}. Количество: {self.amount}(шт).  Находится: На складе"
        elif self.place_2:
            return f"Название: {self.title}.  Цена: {self.price}. Находится: В магазине"


    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


class Person(models.Model):
    image = models.ImageField(upload_to='images/', null=True, blank=True, verbose_name="Изображение")
    email = models.EmailField(max_length=100, verbose_name="Электронная почта")
    name = models.CharField(max_length=100, verbose_name="Имя")
    surname = models.CharField(max_length=100, verbose_name="Фамилия", null=True, blank=True)
    phone = models.CharField(max_length=100, verbose_name="Телефон")
    address = models.CharField(max_length=250, verbose_name="Адрес")
    city = models.CharField(max_length=100, verbose_name="Город")
    country = models.CharField(max_length=100, verbose_name="Страна", null=True, blank=True)
    chef = models.BooleanField(default=False, verbose_name="Повар")
    director = models.BooleanField(default=False, verbose_name="Директор")
    manager = models.BooleanField(default=False, verbose_name="Менеджер")
    seller = models.BooleanField(default=False, verbose_name="Продавец")

    def __str__(self):
        if self.chef:
            return f"Имя: {self.name}. Фамилия: {self.surname}. Должность: Повар"
        elif self.director:
            return f"Имя: {self.name}. Фамилия: {self.surname}.  Должность: Директор"
        elif self.manager:
            return f"Имя: {self.name}. Фамилия: {self.surname}.  Должность: Менеджер"
        elif self.seller:
            return f"Имя: {self.name}. Фамилия: {self.surname}.  Должность: Продавец"


    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"


class Branches(models.Model):
    branches = models.CharField(max_length=100, verbose_name="Филиал в городе")
    address = models.CharField(max_length=200, verbose_name="Адрес")
    employees_num = models.PositiveIntegerField(verbose_name="Количество сотрудников")

    def __str__(self):
        return f"Филиал в городе: {self.branches}.  Адрес: {self.address}"


    class Meta:
        verbose_name = "Филиал"
        verbose_name_plural = "Филиалы"

