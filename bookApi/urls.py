from django.urls import path
from . views import book_list, book_create, book

urlpatterns = [
    path('books/', book_list),
    path('create/', book_create),
    path('<int:pk>/', book)
]