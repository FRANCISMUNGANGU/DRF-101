from rest_framework import serializers
from .models import Book, Order

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

"""
So I have set the `read_only_fields` for the `OrderSerializer` to include `order_date`, `total_price`, `is_returned`, and `rate`. 
This means that when creating or updating an order, these fields will not be editable by the user.
"""

class OrderSerializer(serializers.ModelSerializer):
    book = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all())
    quantity = serializers.IntegerField(required=True, min_value=1)
    order_date = serializers.DateTimeField(required=True)
    return_date = serializers.DateTimeField(required=True)
    total_price = serializers.DecimalField(max_digits=10, decimal_places=2, required=True, min_value=0)
    is_returned = serializers.BooleanField(required=True)
    rate = serializers.DecimalField(max_digits=3, decimal_places=2, min_value=0, default=4.00)

    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ['order_date', 'total_price', 'is_returned', 'rate']

    # """
    # This will be the template to check if the ordered quantity is more than the available quantity of the book.
    # It also checks if the book is available for ordering. If either of these conditions is not met, it raises a validation error.
    # """

    # def validate(self, data):
