from django.db import models

from petstagram.photos.models import Photo


# Create your models here.


class Comment(models.Model):
    MAX_COMMENT_LENGTH = 300

    class Meta:
        ordering = ["-date_time_publication"]

    text = models.CharField(
        max_length=MAX_COMMENT_LENGTH,
        null=False,
        blank=False,
    )
    date_time_publication = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        null=False
    )
    to_photo = models.ForeignKey(
        Photo,
        on_delete=models.CASCADE,
        null=False,
        blank=True,
    )


class Like(models.Model):
    to_photo = models.ForeignKey(
        Photo,
        on_delete=models.CASCADE,
        null=False,
        blank=True,
    )

    # When we have Users:
    # user = models.ForeignKey(
    #     User,
    #     on_delete=models.CASCADE,
    # )
