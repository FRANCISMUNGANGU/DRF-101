from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    pages = models.IntegerField()
    cover_image = models.ImageField(upload_to='cover_images/')
    available = models.BooleanField(default=True)
    number_of_copies = models.IntegerField(default=1)  # New field for number of copies

    def __str__(self):
        return self.title

class Order(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order of {self.quantity} copies of {self.book.title}"