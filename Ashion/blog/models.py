from django.db import models
from django.utils import timezone


class Blog(models.Model):
    name = models.CharField(max_length=255)
    tagline = models.TextField()

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Entry(models.Model):
    fashion_week = 'fashion_week'
    street_style = 'street_style'
    lifestyle = 'lifestyle'
    beauty = 'beauty'

    category_choises = [
        (fashion_week, 'Fashion week'),
        (street_style, 'Street style'),
        (lifestyle, 'Lifestyle'),
        (beauty, 'Beauty'),
    ]

    title = models.CharField(max_length=255)
    content = models.TextField()
    published_at = models.DateTimeField(default=timezone.now)
    authors = models.ManyToManyField(Author)
    categories = models.CharField(max_length=12, choices=category_choises, default=fashion_week)
    number_of_comments = models.IntegerField(default=0)
    number_of_pingbanks = models.IntegerField(default=0)
    rating = models.IntegerField(default=5)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-published_at']


class Hotel(models.Model):
    name = models.CharField(max_length=50)
    hotel_Main_Img = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name
