from django.urls import path
from .views import *

urlpatterns = [
    path('', bookList, name='book-list'),
    path('book/<str:pk>/', bookDetail, name='book'),
    path('eng/', EngbookList, name='eng-book'),
    path('update-book/<str:pk>/', bookUpdate, name='update-book'),
    path('new-books/', newBooks, name='new-books'),
    path('latest-books/', lastBooks, name='last-books'),
    path('feedback/', feedBack, name='feedback'),
    path('frameworks/', frameworks, name='frameworks'),
    path('about-us/', aboutUs, name='about-us'),
]