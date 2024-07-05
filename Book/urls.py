from django.urls import path
from .views import homepage,author,books
urlpatterns=[
    path('',homepage,name='homepage'),
    path('author',author,name='author'),
    path('books',books,name='books')
]