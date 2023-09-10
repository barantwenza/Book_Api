from django.shortcuts import render
from .models import Book
from django.http import JsonResponse

# Create your views here.

def book_list(request):
    books = Book.objects.all() # Return data type known as Complex data
    books_python = list(books.values()) # Python DS
    # Converts in json
    return JsonResponse({
        'books': books_python
    })