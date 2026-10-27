from django.shortcuts import render
from .models import Book, Order
from .serializers import BookSerializer, OrderSerializer
from rest_framework import viewsets
from rest_framework.response import Response
# Create your views here.


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def list(self, request, *args, **kwargs):
        books = self.get_queryset()
        serializer = self.get_serializer(books, many=True)
        return Response({'books': serializer.data})

    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if not serializer.is_valid():
            return Response({'errors': serializer.errors}, status=400)

        else:
            self.perform_create(serializer)
        return Response({'message': 'Book added successfully.', 'book': serializer.data}, status=201)

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def list(self, request, *args, **kwargs):
        orders = self.get_queryset()
        serializer = self.get_serializer(orders, many=True)
        return Response({'orders': serializer.data})

    """
        Homework:
        Using the BookViewSet post method as a template, create a post method for the OrderViewSet.
        Hint: 
        You should not be able to make an order for a book who's quantity is less than the quantity being ordered. 
        You should also not be able to make an order for a book that is not available.

    """
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Check if book is available and if the ordered quantity is less than or equal to the available quantity
        # use the serializer.validated_data to get the book and quantity being ordered
        book = serializer.validated_data['book']
        quantity = serializer.validated_data['quantity']


        """
        Now, write the logic to check if the book is available and if the ordered quantity is less than or equal to the available quantity.
        If either of these conditions is not met, return a response with a status code of 400 and a message indicating the error.
        If both conditions are met, save the order and return a response with a status code of 201 and a message indicating that the order was created successfully
        """