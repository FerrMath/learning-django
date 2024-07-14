from django.test import TestCase
from django.urls import resolve, reverse

from recipes import views

class RecipeViewTest(TestCase):
    
    def test_recipe_home_view_function_is_correct(self):
        view = resolve(reverse('recipes:home'))
        print(f'View Function: {view.func.__name__}')
        self.assertIs(view.func, views.home_view, msg='Home view function is incorrect')

    def test_recipe_category_view_function_is_correct(self):
        view = resolve(reverse('recipes:category', kwargs={'category_id': 1}))
        print(f'View Function: {view.func.__name__}')
        self.assertIs(view.func, views.category_view, msg='Home view function is incorrect')

    def test_recipe_recipe_view_function_is_correct(self):
        view = resolve(reverse('recipes:recipe', kwargs={'id': 1}))
        print(f'View Function: {view.func.__name__}')
        self.assertIs(view.func, views.recipe_view, msg='Home view function is incorrect')
    
    def test_recipe_home_view_returns_status_code_200(self):
        response = self.client.get(reverse('recipes:home'))
        print(f'Status Code: {response.status_code}')
        self.assertEqual(response.status_code, 200, msg='Home view status code is not 200')
    
    def test_recipe_home_view_template_is_correct(self):
        response = self.client.get(reverse('recipes:home'))
        print(f'Template Used: {response.templates[0].name}')
        self.assertTemplateUsed(response, 'recipes/pages/home.html')