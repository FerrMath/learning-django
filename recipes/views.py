from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request):
    content = {
        "title": "Recipes",
        "content": 'Welcome to the home page of the Recipes'
    }
    return render(request, 'recipes/pages/home.html', context=content) # Add the namespace to prevent conflicts with other templates