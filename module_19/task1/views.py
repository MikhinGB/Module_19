from django.http import HttpResponse
from django.shortcuts import render
from .forms import UserRegister
from .models import *

# Create your views here.

def home(request):
    title = 'магазин Дом Игрушки'
    page_title = 'Главная страница'
    link1 = 'Главная'
    link2 = 'Магазин'
    link3 = 'Корзина'
    context = {
        'title': title,
        'page_title': page_title,
        'link1': link1,
        'link2': link2,
        'link3': link3,
    }
    return render(request, 'home.html', context)


def store(request):
    title = 'магазин Дом Игрушки'
    page_title = 'Игры'
    link1 = 'Главная'
    link2 = 'Магазин'
    link3 = 'Корзина'
    games = Game.objects.all()
    context = {
        'title': title,
        'page_title': page_title,
        'games': games,
        'link1': link1,
        'link2': link2,
        'link3': link3,
    }
    return render(request, 'store.html', context)


def basket(request):
    title = 'Дом Игрушки'
    page_title = 'Корзина'
    link1 = 'Главная'
    link2 = 'Магазин'
    link3 = 'Корзина'
    context = {
        'title': title,
        'page_title': page_title,
        'link1': link1,
        'link2': link2,
        'link3': link3,
    }
    return render(request, 'basket.html', context)

def sign_up_by_html(request):
    users = Buyer.objects.all()
    users_names = []
    for user in users:
        user_name = user.name
        users_names.append(user_name)
    context = {
        "users": users,
    }
    info = {}
    if request.method == 'POST':
        # Получаем данные
        username = request.POST.get('username')
        if username in users_names:
            info["error"] = 'Пользователь уже существует'
            return HttpResponse(info["error"])
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        if password != repeat_password:
            info["error"] = 'Пароли не совпадают'
            return HttpResponse(info["error"])
        age = request.POST.get('age')

        Buyer.objects.create(name=username, balance='0', age=age)

        return HttpResponse(f'Приветствуем, {username}!')

    return render(request, 'registration_page.html', context)

