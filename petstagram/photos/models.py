from django.core.validators import MinLengthValidator
from django.db import models

from petstagram.pets.models import Pet


# Create your models here.

class Photo(models.Model):
    photo = models.ImageField()
    description = models.TextField(
        max_length=10,
        validators=(MinLengthValidator(10),),
        blank=True,
        null=True,
    )
    location = models.CharField(
        max_length=30,
        blanks=True,
        null=True,
    )
    tagged_pets = models.ManyToManyField(
        Pet,
        blank=True,
    )
    date_of_publications = models.DateField(
        auto_now=True,
    )
