from django.shortcuts import render
from .texts import intro
from .models import Buyer, Game

# Create your views here.
PAGES_LIST = [['Главная страница', '/'], ['Каталог', '/catalog'], ['Корзина', '/shopping_cart'], ['Регистрация', '/sign_up']]

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
    games = Game.objects.all()
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
    users = [buyer.name.title() for buyer in Buyer.objects.all()]
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

        if password == repeat_password and username.title() not in users and int(age) >= 18:
            Buyer.objects.create(name=username, balance=1000, age=age)
            info['error'] = f'Поздравляем с регистрацией. Добро пожаловать {username}'
            return render(request, 'sign_up.html', context=info)
        else:
            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            if username.title() in users:
                info['error'] = f'Пользователь {username} уже существует'
            if int(age) < 18:
                info['error'] = 'Вы должны быть старше 18'
    return render(request, 'sign_up.html', context=info)


# get users
def get_users(request):
    users = [(buyer.name.title(), buyer.age, float(buyer.balance)) for buyer in Buyer.objects.all()]
    context = {
        'users': users
    }
    return render(request, 'get_users.html', context)