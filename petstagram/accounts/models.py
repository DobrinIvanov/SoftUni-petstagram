from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
from django.db import models

from petstagram.accounts.enums import Gender
from petstagram.accounts.validators import ValidateOnlyLetters


# Create your models here.
class PetstagramUser(AbstractUser):

    MIN_LENGTH_NAME = 2
    MAX_LENGTH_NAME = 30

    email = models.EmailField(
        unique=True,
    )

    first_name = models.CharField(
        max_length=MAX_LENGTH_NAME,
        validators=[
            MinValueValidator(MIN_LENGTH_NAME),
            ValidateOnlyLetters,
        ]
    )

    last_name = models.CharField(
        max_length=MAX_LENGTH_NAME,
        validators=[
            MinValueValidator(MIN_LENGTH_NAME),
            ValidateOnlyLetters,
        ]
    )

    profile_picture = models.URLField()

    gender = models.CharField(
        max_length=15,
        choices=Gender.choices(),
    )
