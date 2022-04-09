from django.contrib.auth import models as auth_models, get_user_model
from django.core.validators import MinLengthValidator
from django.db import models
from motherearth.auth_app.managers import MotherearthUserManager
from motherearth.common.validators import validate_only_letters


class MotherearthUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    USERNAME_MAX_LENGTH = 25
    username = models.CharField(
        max_length=USERNAME_MAX_LENGTH,
        unique=True,

    )

    is_staff = models.BooleanField(
        default=False
    )

    USERNAME_FIELD = 'username'

    objects = MotherearthUserManager()

    def __str__(self):
        return f'{self.username}'


class Profile(models.Model):
    FIRST_NAME_MIN_LENGTH = 2
    FIRST_NAME_MAX_LENGTH = 30
    LAST_NAME_MIN_LENGTH = 2
    LAST_NAME_MAX_LENGTH = 30

    REGIONS = (
        ("Западно Северняшко", "Западно Северняшко"),
        ("Лудогорие", "Лудогорие"),
        ("Добруджа", "Добруджа"),
        ("Шоплук", "Шоплук"),
        ("Тракия", "Тракия"),
        ("Македония", "Македония"),
        ("Родопа", "Родопа"),
        ("Странджа", "Странджа"),
    )

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LENGTH),
            validate_only_letters,
        )
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(LAST_NAME_MIN_LENGTH),
            validate_only_letters,
        )
    )

    region = models.CharField(
        max_length=20,
        choices=REGIONS,

    )

    email = models.EmailField()
    description = models.TextField(
        null=True,
        blank=True,
    )
    photo = models.ImageField(
        null=True,
        blank=True
    )
    place = models.CharField(
        max_length=20,
        null=True,
        blank=True
    )
    phone_number = models.IntegerField(
        unique=True,
    )

    user = models.OneToOneField(
        MotherearthUser,
        on_delete=models.CASCADE,
        primary_key=True
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
