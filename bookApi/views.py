from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse
from .serializers import BookSerialiser
from .models import Book

# Create your views here.

# GET request
@api_view(['GET'])
def book_list(request):
    books = Book.objects.all() # Return data type known as Complex data
    serializer = BookSerialiser(books, many=True) # many=True means that we want to serialize many differents objects into Json
    return Response(serializer.data)

# POST request
@api_view(['POST'])
def book_create(request):
    serializer = BookSerialiser(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)
    
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def book(request, pk):
    if request.method == 'GET':
        book = Book.objects.get(pk=pk)
        serializer = BookSerialiser(book)
        return Response(serializer.data)