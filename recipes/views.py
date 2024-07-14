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
    try:
        recipe = get_object_or_404(Recipe, id=id)
        if not recipe.is_published:
            raise Http404
    except Http404 as e:
        return render(request, 'global/pages/404.html', status=404, context={'message':'Recipe not found or is not published.'})
    
    context = {
        "id": id,
        "is_detail_page": True,
        "recipe": recipe,
    }
    return render (request, 'recipes/pages/recipe.html', context=context)

def category_view(request, category_id):
    category = Category.objects.filter(id=category_id).first()
    recipes = Recipe.objects.filter(category=category, is_published=True)

    context = {
        "title": "Recipes",
        "content": 'Welcome to the home page of the Recipes',
        'recipes': recipes,
        'category': category,
    }
    return render(request, 'recipes/pages/category.html', context=context)