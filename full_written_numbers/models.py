from django.db import models


class EnglishNumbers(models.Model):
    number = models.IntegerField(unique=True, null=False)
    written_number = models.TextField()

    class Meta:
        indexes = [
            models.Index(fields=["number"])
        ]
