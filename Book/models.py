from django.db import models
from django.contrib.auth.models import User
from .helpers import SaveMedia
class Author(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    image = models.ImageField(upload_to=SaveMedia.save_book_image_path, null=True)
    birth_date=models.DateField()
    nationality=models.CharField(max_length=25)
    genre=models.CharField(max_length=50)
    created_time=models.DateTimeField(auto_now_add=True)
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

class Book(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    author=models.ForeignKey(Author,on_delete=models.CASCADE)
    image=models.ImageField(upload_to=SaveMedia.save_book_image_path,null=True)
    price=models.PositiveIntegerField()
    count=models.PositiveIntegerField(default=1)
    created_time=models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    text=models.TextField()
    book=models.ManyToManyField(Book)
    created_time=models.DateTimeField(auto_now_add=True)
