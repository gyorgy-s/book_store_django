from django.db.models import Avg
from django.shortcuts import get_object_or_404, render

from .models import Book


def home(request):
    books = Book.objects.all().order_by("-rating")
    number_of_books = books.count()
    avg_rating = books.aggregate(Avg("rating"))

    return render(
        request,
        "book_outlet/index.html",
        {
            "books": books,
            "total_number_of_books": number_of_books,
            "average_rating": avg_rating,
        },
    )


def book_detail(request, slug):
    # try:
    #     book = Book.objects.get(id=book_id)
    # except Book.DoesNotExist:
    #     raise Http404()

    book = get_object_or_404(Book, slug=slug)

    return render(
        request,
        "book_outlet/book_detail.html",
        {
            "title": book.title,
            "author": book.author,
            "rating": book.rating,
            "is_bestselling": book.is_bestselling,
        },
    )
