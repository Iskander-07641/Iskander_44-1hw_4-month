from django.urls import path
from . import views

urlpatterns = [
    path('about-me/', views.about_me, name='about_me'),
    path('about-friend/', views.about_friend, name='about_friend'),
    path('current-time/', views.current_time, name='current_time'),
    path('create/', views.book_create, name='book_create'),
    path('update/<int:pk>/', views.book_update, name='book_update'),
    path('delete/<int:pk>/', views.book_delete, name='book_delete'),
    path('', views.book_list, name='book_list'),
    path('<int:pk>/', views.book_detail, name='book_detail'),
]
