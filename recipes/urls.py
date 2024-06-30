# Import the views from the recipes app
from django.urls import path
from recipes.views import *

urlpatterns = [
    path('', home_view, name='home'),
]