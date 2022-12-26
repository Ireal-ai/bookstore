from django.db import models
from django.utils import timezone

import user.models as user_model


class Genre(models.Model):
    name = models.CharField(verbose_name='Genre', max_length=20)
    userId = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='rating',
                               verbose_name='user id', null=True, blank=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    genre = models.ManyToManyField(Genre, related_name='genres')
    title = models.CharField(verbose_name='Book title', max_length=50)
    author = models.CharField(verbose_name='Author', max_length=80)
    price = models.DecimalField(verbose_name='Price', max_digits=8, decimal_places=2)
    cover = models.CharField(verbose_name='Cover', max_length=250, null=True, blank=True)
    date_of_issue = models.DateField(verbose_name='Date of Issue', default=timezone.now)
    in_stock = models.PositiveIntegerField(verbose_name='In stock', null=True, blank=True)
    description = models.TextField(verbose_name='Description', max_length=900, null=True, blank=True)
    average_rate = models.FloatField(verbose_name='Average rate', null=True, blank=True, max_length=3)
    is_in_favorite = models.BooleanField()

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

    def __str__(self):
        return self.title


class Comment(models.Model):
    date = models.DateTimeField(verbose_name='Comment date', default=timezone.now)
    text = models.TextField(verbose_name='Comment', max_length=900, default='Test')
    bookId = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comments',
                               verbose_name='book id', null=True, blank=True)
    userId = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='comment',
                               verbose_name='user id', null=True, blank=True)

    def __str__(self):
        return self.text


class Rating(models.Model):
    bookId = models.ForeignKey(Book, on_delete=models.CASCADE)
    name = models.FloatField(verbose_name='Rating', max_length=3)

    def __str__(self):
        return str(self.name)


class Reporter(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


class Article(models.Model):
    headline = models.CharField(max_length=100)
    pub_date = models.DateField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

    def __str__(self):
        return self.headline

    class Meta:
        ordering = ['headline']
