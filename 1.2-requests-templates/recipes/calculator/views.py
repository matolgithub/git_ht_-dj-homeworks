from django.http import HttpResponse
from django.shortcuts import render

import copy

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
    'blood_Mary': {
        'томатный сок, г': 150,
        'водка, мл': 75,
    },
}


def home(request):
    context = {
        'string': 'Hello! It is Home Page of HomeTask_1.2.'
    }
    return render(request, 'calculator/home_page.html', context)


def recipes_calculator(request, recipe_link):
    servings = int(request.GET.get('servings', 1))
    data_copy = copy.deepcopy(DATA)
    if servings > 1:
        for meal in data_copy:
            for component, quantity in data_copy[meal].items():
                if type(quantity) == float:
                    data_copy[meal][component] = round(quantity * servings, 1)
                else:
                    data_copy[meal][component] = quantity * servings
    try:
        context = {'recipe': data_copy[recipe_link]}
    except:
        context = {}
    return render(request, 'calculator/index.html', context)
