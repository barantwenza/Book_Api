from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse
from .serializers import BookSerialisers
from .models import Book

# Create your views here.

@api_view(['GET'])
def book_list(request):
    books = Book.objects.all() # Return data type known as Complex data
    serializer = BookSerialisers(books, many=True) # many=True means that we want to serialize many differents objects into Json
    return Response(serializer.data)