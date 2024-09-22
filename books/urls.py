from django.urls import path

from . import views
from .views import (AboutFriendView, CurrentTimeView,
                    BookListView, BookDetailView, BookCreateView,
                    BookUpdateView, BookDeleteView, register, user_login, employee_list)
from books.views import AboutMeView

urlpatterns = [
    path('about-me/', AboutMeView.as_view(), name='about_me'),
    path('about-friend/', AboutFriendView.as_view(), name='about_friend'),
    path('current-time/', CurrentTimeView.as_view(), name='current_time'),
    path('', BookListView.as_view(), name='book_list'),
    path('<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('create/', BookCreateView.as_view(), name='book_create'),
    path('update/<int:pk>/', BookUpdateView.as_view(), name='book_update'),
    path('delete/<int:pk>/', BookDeleteView.as_view(), name='book_delete'),
    path('search/', views.book_search, name='book_search'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('employees/', employee_list, name='employee_list'),
]
