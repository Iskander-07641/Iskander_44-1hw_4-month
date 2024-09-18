from django.http import HttpResponse
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
