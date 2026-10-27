from django.urls import path
from . import views


urlpatterns = [
    path('books/', views.BookViewSet.as_view({'get': 'list'}), name='home'),
    path('add_book/', views.BookViewSet.as_view({'post': 'post'}), name='add_book'),
] 