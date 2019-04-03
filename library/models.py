from django.db import models
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
# Create your models here.


# class CustomUser(models.Model):
#     username = models.CharField(verbose_name='Login', max_length=16)
#     password = models.CharField(verbose_name='Password', max_length=16)
#     books = models.ManyToManyField('Book', verbose_name='Books', blank=True, related_name='users')
#     is_librarian = models.BooleanField(verbose_name='is_librarian', default=False)
#
#     def __str__(self):
#         return self.username

class User(User):
    books = models.ManyToManyField('Book', verbose_name='Books', blank=True, related_name='users')

    # def create(self, validated_data):
    #     user = User(
    #         email=validated_data['email'],
    #         username=validated_data['username']
    #     )
    #     user.set_password(validated_data['password'])
    #     user.save()
    #     Token.objects.create(user=user)
    #     return user

    def __str__(self):
        return self.username


class Author(models.Model):
    name = models.CharField(verbose_name='Author', max_length=64)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(verbose_name='Category', max_length=64)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(verbose_name='Title', max_length=256)
    author = models.ForeignKey('Author', verbose_name='Author', on_delete=models.CASCADE)
    categories = models.ManyToManyField('Category', verbose_name='Categories', related_name='books')
    quantity = models.PositiveIntegerField(verbose_name='Quantity', default=10)
    date_pub = models.PositiveSmallIntegerField(verbose_name='Date of publication')

    def __str__(self):
        return self.title
