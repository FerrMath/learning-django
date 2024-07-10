from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Recipe

# Create your views here.
def home_view(request):
    recipes = Recipe.objects.all()
    content = {
        "title": "Recipes",
        "content": 'Welcome to the home page of the Recipes',
        'recipes': recipes,
    }
    return render(request, 'recipes/pages/home.html', context=content) # Add the namespace to prevent conflicts with other templates
    
def recipe_view(request, id):

    context = {
        "id": id,
        "is_detail_page": True,
        "recipe": get_object_or_404(Recipe, id=id)
    }
    return render (request, 'recipes/pages/recipe.html', context=context)