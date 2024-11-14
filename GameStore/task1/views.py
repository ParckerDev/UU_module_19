from django.shortcuts import render
from .forms import UserRegister
from .texts import intro, games
from django.http import HttpResponse

# Create your views here.
PAGES_LIST = [['Главная страница', '/'], ['Каталог', '/catalog'], ['Корзина', '/shopping_cart'], ['Регистрация', '/sign_up']]
USERS = ['Ira', 'nikita', 'Kolya', 'Masha']


# Главная страница
def main(request):
    context = {
        'title': 'Главная страница',
        'pages_list': PAGES_LIST,
        'text': intro
    }

    return render(request, 'main.html', context)

# Страница купить игру
def catalog(request):
    context = {
        'title': 'Каталог игр',
        'pages_list': PAGES_LIST,
        'games': games,
    }

    return render(request, 'catalog.html', context)

# Страница с корзиной покупок
def shopping_cart(request):
    context = {
        'title': 'Корзина покупок',
        'pages_list': PAGES_LIST,

    }
    return render(request, 'shopping_cart.html', context)

# Форма регистрации
def sign_up(request):
    info = {
        'title': 'Регистрация пользователя',
        'pages_list': PAGES_LIST,
    }
    if request.method == 'POST':
        # Get data
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get("repeat_password")
        age = request.POST.get('age')

        print(f'Username: {username}')
        print(f'Passsword: {password}')
        print(f'Repeat_password: {repeat_password}')
        print(f'Age: {age}')

        if password == repeat_password and username not in USERS and int(age) >= 18:
            USERS.append(username)
            info['error'] = f'Поздравляем с регистрацией. Добро пожаловать {username}'
            return render(request, 'sign_up.html', context=info)
        else:
            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            if username in USERS:
                info['error'] = f'Пользователь {username} уже существует'
            if int(age) < 18:
                info['error'] = 'Вы должны быть старше 18'
    return render(request, 'sign_up.html', context=info)