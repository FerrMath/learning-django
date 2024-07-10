from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, get_list_or_404
from .models import Recipe

# Create your views here.
def home_view(request):
    recipes = get_list_or_404(Recipe)
    recipes = [recipe for recipe in recipes if recipe.is_published]
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