from django.db import models
from django.contrib.auth.models import User
from django.db.models.enums import Choices
from django.urls import reverse
from datetime import datetime, date

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)     
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')

class Post(models.Model):
    title = models.CharField(max_length=100)
    # title_tag = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # category = models.ForeignKey(Category, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    body = models.TextField()
    published_date = models.DateField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='blog_posts_likes')
    # dislikes = models.ManyToManyField(User, related_name='blog_posts_dislikes')

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('home')

    def total_likes(self): # returns likes count 
        return self.likes.count()
    
    # def total_dislikes(self): # return dislikes count
    #     return self.dislikes.count()

        