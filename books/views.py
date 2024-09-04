from django.http import HttpResponse
from datetime import datetime

from django.shortcuts import render


def about_me(request):
    return HttpResponse("Привет, я Искандер.")


def about_friend(request):
    return HttpResponse("Мой друг - Атила.")


def current_time(request):
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    return HttpResponse(f"Текущее время: {current_time}")





