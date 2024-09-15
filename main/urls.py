from django.contrib import admin
from django.urls import path, include
from books import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about-me/', views.about_me, name='about_me'),
    path('about-friend/', views.about_friend, name='about_friend'),
    path('current-time/', views.current_time, name='current_time'),
    path('books/', include('books.urls')),

]
