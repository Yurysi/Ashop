from django.db import models
from datetime import date

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


    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField(default=date.today)
    authors = models.ManyToManyField(Author)
    categories = models.CharField(max_length=12, choices=category_choises, default= fashion_week)
    number_of_comments = models.IntegerField(default=0)
    number_of_pingbanks = models.IntegerField(default=0)
    rating = models.IntegerField(default=5)

    def __str__(self):
        return self.headline
