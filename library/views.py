from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status
from rest_framework import generics
from django.contrib.auth import authenticate

from .models import *
from .serializers import *

# Create your views here.


def welcome_page(request):
    return render(request, 'library/index.html')


class UsersList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserCreate(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer


class LoginView(APIView):
    permission_classes = ()

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            return Response({'token': user.auth_token.key})
        else:
            return Response({'error': 'Wrong credentials'}, status=status.HTTP_400_BAD_REQUEST)


class UsersBook(generics.ListAPIView):
    def get_queryset(self):
        queryset = Book.objects.filter(users=self.kwargs['pk'])
        return queryset
    serializer_class = BookSerializer

    # def get(self, request, *args, **kwargs):
    #     user = User.objects.get(pk=self.kwargs['pk'])
    #     if not request.user == user.username:
    #         raise PermissionError('You can not see books of this user.')
    #     return super().get(request, *args, **kwargs)


class UserDetail(generics.RetrieveDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class AuthorList(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorDetail(generics.RetrieveDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class BooksList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BooksOfAuthor(generics.ListAPIView):
    def get_queryset(self):
        queryset = Book.objects.filter(author__id=self.kwargs['pk'])
        return queryset
    serializer_class = BookSerializer


class BooksOfCategory(generics.ListAPIView):
    def get_queryset(self):
        queryset = Book.objects.filter(categories__id=self.kwargs['pk'])
        return queryset
    serializer_class = BookSerializer


class BookDetail(generics.RetrieveDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

