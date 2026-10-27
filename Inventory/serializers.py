from rest_framework import serializers
from .models import Book
from django.http import JsonResponse

class BookSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=True)
    author = serializers.CharField(required=True)
    published_date = serializers.DateField(required=True)
    pages = serializers.IntegerField(required=True, min_value=1)
    cover_image = serializers.ImageField(required=True)
    available = serializers.BooleanField(required=True)
    number_of_copies = serializers.IntegerField(required=True, min_value=1)

    class Meta:
        model = Book
        fields = '__all__'
