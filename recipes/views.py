from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, render, get_list_or_404
from .models import Category, Recipe

# Create your views here.
def home_view(request):
    recipes = Recipe.objects.filter(is_published=True)
    content = {
        "title": "Recipes",
        "content": 'Welcome to the home page of the Recipes',
        'recipes': recipes,
    }
    return render(request, 'recipes/pages/home.html', context=content) # Add the namespace to prevent conflicts with other templates
    
def recipe_view(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    if not recipe.is_published:
        return render(request, 'global/pages/404.html', status=404, context={'message':'Recipe not found or is not published.'})
    
    context = {
        "id": id,
        "is_detail_page": True,
        "recipe": recipe,
    }
    return render (request, 'recipes/pages/recipe.html', context=context)

def category_view(request, category_id):
    try:
        category = get_object_or_404(Category, id=category_id)
    except Http404:
        return render(request, 'global/pages/404.html', status=404, context={'message':'Category not found'})
    
    recipes = Recipe.objects.filter(category=category, is_published=True)

    context = {
        "title": "Recipes",
        "content": 'Welcome to the home page of the Recipes',
        'recipes': recipes,
    }
    return render(request, 'recipes/pages/home.html', context=context)