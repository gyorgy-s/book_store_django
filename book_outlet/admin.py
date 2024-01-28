from django.contrib import admin

from .models import Author, Book

# Register your models here.


class AuthorAdmin(admin.ModelAdmin):
    list_filter = ("first_name", "last_name")
    list_display = ("first_name", "last_name")


class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_filter = (
        "author",
        "rating",
    )
    list_display = ("id", "title", "author", "rating")


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
