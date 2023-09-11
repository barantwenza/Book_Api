from rest_framework import serializers
from .models import Book

class BookSerialiser(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    number_of_pages = serializers.IntegerField()
    published_date = serializers.DateField()
    quantity = serializers.IntegerField()

    # create method. will be called in order to create a book in the data base
    def create(self, data):
        return Book.objects.create(**data)