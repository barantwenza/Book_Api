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
    
    def update(self, instance, data):
        instance.title = data.get('title', instance.title)
        instance.number_of_pages = data.get('number_of_pages', instance.number_of_pages)
        instance.published_date = data.get('published_date', instance.published_date)
        instance.quantity = data.get('quantity', instance.quantity)
        instance.save()
        return instance