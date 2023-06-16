from django.db import models


class Certificate(models.Model):

    title = models.CharField(
        max_length=50,
        blank=False,
        null=False,
    )
    photo = models.ImageField(
        upload_to='',
        blank=False,
        null=False,
    )

    def __str__(self):
        return self.title
