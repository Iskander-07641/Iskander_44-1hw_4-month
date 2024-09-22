from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from datetime import datetime

from .forms import BookForm
from .models import Book


class AboutMeView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Привет, я Искандер.")


class AboutFriendView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Мой друг - Атила.")


class CurrentTimeView(View):
    def get(self, request, *args, **kwargs):
        now = datetime.now()
        current_time = now.strftime("%Y-%m-%d %H:%M:%S")
        return HttpResponse(f"Текущее время: {current_time}")


class BookListView(ListView):
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'books'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Book.objects.filter(title__icontains=query)
        return Book.objects.all()


class BookDetailView(DetailView):
    model = Book
    template_name = 'books/book_detail.html'
    context_object_name = 'book'


class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'books/book_form.html'
    success_url = reverse_lazy('book_list')


class BookUpdateView(UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'books/book_form.html'
    success_url = reverse_lazy('book_list')


class BookDeleteView(DeleteView):
    model = Book
    template_name = 'books/book_confirm_delete.html'
    success_url = reverse_lazy('book_list')


def book_search(request):
    query = request.GET.get('q')
    results = []
    if query:
        results = Book.objects.filter(title__icontains=query)
    return render(request, 'books/book_search_results.html', {'results': results, 'query': query})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log in the user after registration
            return redirect('employee_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('employee_list')
    return render(request, 'registration/login.html')


@login_required
def employee_list(request):
    employees = User.objects.all()
    return render(request, 'employees/employee_list.html', {'employees': employees})
