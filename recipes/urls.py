# Import the views from the recipes app
from django.urls import path
from recipes.views import *

app_name = 'recipes'

urlpatterns = [
    path('', home_view, name='home'),
    path('recipes/<int:id>/', recipe_view, name='recipe')
]