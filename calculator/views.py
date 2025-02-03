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
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }


def calculate(request, rname):
    if rname not in DATA:
        return HttpResponse(f'Recipe {rname} not found')
    recipe = DATA[rname].copy()
    servings = request.GET.get("servings")

    if servings is not None:
        try:
            servings_int = int(servings)
            for i, k in recipe.items():
                recipe[i] = k * servings_int
        except ValueError:
            pass

    context = {
        'recipe': recipe
    }
    return render(request, 'calculator/index.html', context)
