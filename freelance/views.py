from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'users:login'}
        ]


def index(request):
    data = {
        'title': 'Freelance',
        'menu': menu,
    }
    return render(request, 'freelance/index.html', context=data)


def about(request):
    return render(request, 'freelance/about.html', {'title': 'О сайте', 'menu': menu})


def contact(request):
    return HttpResponse("Контакты")


def page_not_found(request, exception):
    return HttpResponseNotFound("Page not found")
