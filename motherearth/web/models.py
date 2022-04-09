from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MinLengthValidator
from django.db import models
from motherearth.auth_app.models import Profile
from motherearth.common.validators import validate_only_letters

UserModel = get_user_model()


class Post(models.Model):
    title = models.CharField(
        max_length=30,
        validators=(
            MinLengthValidator(2),
        )
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

    def __str__(self):
        return f'{self.title}'


class Kind(models.Model):

    name = models.CharField(
        max_length=10,
    )

    def __str__(self):
        return f'{self.name}'


class Type(models.Model):

    name = models.CharField(
        max_length=20,
    )

    def __str__(self):
        return f'{self.name}'


class Plants(models.Model):
    name = models.CharField(
        max_length=20,
        validators=(
            MinLengthValidator(2),
            validate_only_letters,
        )
    )
    kind = models.ForeignKey(
        Kind,
        on_delete=models.PROTECT,
    )
    type = models.ForeignKey(
        Type,
        on_delete=models.PROTECT,
    )

    owner = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
    )
    publication_date = models.DateTimeField(
        auto_now_add=True,
    )
    description = models.TextField(
        null=True,
        blank=True,
    )
    photo = models.FileField(
        null=True,
        blank=True
    )
    price = models.FloatField(validators=[MinValueValidator(0)])

    def __str__(self):
        return f'{self.name}'


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
