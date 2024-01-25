from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=150, null=False, blank=False, default=None)
    rating = models.IntegerField(
        validators=[MinValueValidator(limit_value=1), MaxValueValidator(limit_value=5)]
    )
    author = models.CharField(max_length=50, null=True)
    is_bestselling = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title}"
