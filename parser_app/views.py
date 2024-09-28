from django.shortcuts import render
from .forms import ParseForm
from .models import ParserRezka


def parse_view(request):
    if request.method == 'POST':
        form = ParseForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            return render(request, 'parser_app/result.html', {'movies': movies})
    else:
        form = ParseForm()
    return render(request, 'parser_app/parse.html', {'form': form})


def result_view(request):
    movies = ParserRezka.objects.all()
    return render(request, 'parser_app/result.html', {'movies': movies})
