from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render, get_object_or_404
from .models import Book

from django.shortcuts import render


def about_me(request):
    return HttpResponse("Привет, я Искандер.")


def about_friend(request):
    return HttpResponse("Мой друг - Атила.")


def current_time(request):
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    return HttpResponse(f"Текущее время: {current_time}")


def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'books/book_detail.html', {'book': book})





