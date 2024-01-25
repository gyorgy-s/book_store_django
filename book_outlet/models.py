from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=150, null=False, blank=False, default=None)
    rating = models.DecimalField(
        decimal_places=2,
        max_digits=3,
        validators=[MinValueValidator(limit_value=1), MaxValueValidator(limit_value=5)],
    )
    author = models.CharField(max_length=50, null=True)
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="", null=False)

    def get_absolute_url(self):
        return reverse("book_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title}"
