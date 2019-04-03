from django.urls import path
from .views import *

urlpatterns = [
    path('api/users/<int:pk>/books/', UsersBook.as_view(), name='users_book_url'),
    path('api/users/<int:pk>/', UserDetail.as_view(), name='user_detail_url'),
    path('api/users/create/', UserCreate.as_view(), name='user_create_url'),
    path('api/users/', UsersList.as_view(), name='users_list_url'),
    path('login/', LoginView.as_view(), name='login_url'),
    path('api/authors/<int:pk>/books/', BooksOfAuthor.as_view(), name='books_of_author_url'),
    path('api/authors/<int:pk>/', AuthorDetail.as_view(), name='author_detail_url'),
    path('api/authors/', AuthorList.as_view(), name='authors_list_url'),
    path('api/category/<int:pk>/books/', BooksOfCategory.as_view(), name='books_of_category_url'),
    path('api/books/<int:pk>/', BookDetail.as_view(), name='book_detail_url'),
    path('api/books/', BooksList.as_view(), name='books_list_url'),
    path('', welcome_page, name='library_url')
]
