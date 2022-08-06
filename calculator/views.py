from django.shortcuts import render, reverse
from pprint import pprint

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


def home_view(request):
    pages = {
        # 'Главная страница': reverse('home'),
        'omlet': reverse('omlet'),
        'pasta': reverse('pasta'),
        'buter': reverse('buter'),
    }

    context = {
        'pages': pages
    }

    return render(request, 'calculator/home.html', context)


# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }

def recipes(request, recipe):
    # name = request.GET.get('name', 'omlet')
    qtt = int(request.GET.get('servings', 1))

    # context = {
    #   'recipe': {
    #     'ингредиент1': количество1,
    #     'ингредиент2': количество2,
    #   }

    context = {}
    tmp_dict = {}

    for key, val in DATA[name].items():
        tmp_dict.setdefault(key, val * qtt)
    context.setdefault('recipe', tmp_dict)

    return render(request, 'calculator/index.html', context)


def omlet(request):
    qtt = int(request.GET.get('servings', 1))

    context = {}
    tmp_dict = {}

    for key, val in DATA['omlet'].items():
        tmp_dict.setdefault(key, val * qtt)
    context.setdefault('recipe', tmp_dict)

    return render(request, 'calculator/index.html', context)


def pasta(request):
    qtt = int(request.GET.get('servings', 1))

    context = {}
    tmp_dict = {}

    for key, val in DATA['pasta'].items():
        tmp_dict.setdefault(key, val * qtt)
    context.setdefault('recipe', tmp_dict)

    return render(request, 'calculator/index.html', context)


def buter(request):
    qtt = int(request.GET.get('servings', 1))

    context = {}
    tmp_dict = {}

    for key, val in DATA['buter'].items():
        tmp_dict.setdefault(key, val * qtt)
    context.setdefault('recipe', tmp_dict)

    return render(request, 'calculator/index.html', context)
