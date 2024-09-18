from django.urls import path
from .views import ( AboutFriendView, CurrentTimeView,
                    BookListView, BookDetailView, BookCreateView,
                    BookUpdateView, BookDeleteView)
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
]
