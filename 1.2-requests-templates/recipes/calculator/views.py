from django.http import HttpResponse
from django.shortcuts import render

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
}


def home(request):
    return HttpResponse('Hello! It is Home Page of HomeTask_1.2.')


def recipes_calculator(request, recipe_link):
    servings = int(request.GET.get('servings', 1))
    if servings > 1:
        for meal in DATA:
            for component, quantity in DATA[meal].items():
                if type(quantity) == float:
                    DATA[meal][component] = round(quantity * servings, 1)
                else:
                    DATA[meal][component] = quantity * servings
    if recipe_link == 'omlet':
        context = {'recipe': DATA['omlet']}
    elif recipe_link == 'pasta':
        context = {'recipe': DATA['pasta']}
    elif recipe_link == 'buter':
        context = {'recipe': DATA['buter']}
    else:
        context = {}
    return render(request, 'calculator/index.html', context)
