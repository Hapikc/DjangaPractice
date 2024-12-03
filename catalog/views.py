from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre


def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_genre = Genre.objects.all().count()
    num_books_title = Book.objects.filter(title='Первая стена').count()

    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()

    return render(
        request,
        'index.html',
        context={'num_books': num_books, 'num_instances': num_instances, 'num_genre': num_genre,
                 'num_books_title': num_books_title,
                 'num_instances_available': num_instances_available, 'num_authors': num_authors},
    )