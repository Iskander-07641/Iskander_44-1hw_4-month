from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import BookForm


def about_me(request):
    return HttpResponse("Привет, я Искандер.")


def about_friend(request):
    return HttpResponse("Мой друг - Атила.")


def current_time(request):
    now = datetime.now()
    current__time = now.strftime("%Y-%m-%d %H:%M:%S")
    return HttpResponse(f"Текущее время: {current__time}")


def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'books/book_detail.html', {'book': book})


def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'books/book_form.html', {'form': form})


def book__create(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'books/book_form.html', {'form': form})


def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'books/book_form.html', {'form': form})


def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'books/book_confirm_delete.html', {'book': book})
