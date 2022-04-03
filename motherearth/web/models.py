from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models
from motherearth.auth_app.models import Profile


UserModel = get_user_model()


class Post(models.Model):
    title = models.CharField(
        max_length=30
    )
    content = models.TextField(
    )

    publication_date = models.DateTimeField(
        auto_now_add=True,
    )
    photo = models.ImageField(
        null=True,
        blank=True
    )
    user = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
    )


class Plants(models.Model):
    KINDS = (
        ("Семе", "Семе"),
        ("Луковица", "Луковица"),
        ("Разсад", "Разсад"),
        ("Плод", "Плод"),
    )

    TYPES = (
        ("Домат", "Домат"),
        ("Краставица", "Краставица"),
        ("Лук", "Лук"),
    )

    kind = models.CharField(max_length=10, choices=KINDS)

    type = models.CharField(max_length=20, choices=TYPES)

    owner = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
    )
    publication_date = models.DateTimeField(
        auto_now_add=True,
    )
    description = models.TextField(
        null=True,
        blank=True
    )
    photo = models.FileField(
        null=True,
        blank=True
    )
    price = models.FloatField(validators=[MinValueValidator(0)])


class Product(models.Model):
    PRODUCTS = (
        ("Грънчарство", "Грънчарство"),
        ("Кошничарство", "Кошничарство"),
        ("Посуда", "Посуда"),
        ("Накити", "Накити"),
        ("Инструменти", "Инструменти"),
        ("Дървени занаяти", "Дървени занаяти"),
        ("Текстил", "Текстил"),
        ("Козметика", "Козметика"),
        ("Други", "Други")
    )

    product = models.CharField(
        max_length=20,
        choices=PRODUCTS
    )
    owner = models.ForeignKey(
        to=Profile,
        on_delete=models.CASCADE,
    )
    description = models.TextField(
        null=True,
        blank=True
    )
    photo = models.ImageField(
        null=True,
        blank=True
    )
    price = models.FloatField(validators=[MinValueValidator(0)])


class Place(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    description = models.TextField(
        null=True,
        blank=True
    )
    photo = models.ImageField(
        null=True,
        blank=True
    )
    phone_number = models.IntegerField(
        null=True,
        blank=True,
        unique=True,
    )


class Event(models.Model):
    date = models.DateTimeField()
    name = models.CharField(max_length=20)
    description = models.TextField(
        null=True,
        blank=True
    )
    location = models.CharField(max_length=50)
    publication_date = models.DateTimeField(
        auto_now_add=True,
    )


