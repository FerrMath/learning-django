from django.test import TestCase
from django.urls import resolve, reverse

from recipes import views
from recipes.models import Category, Recipe, User
from .test_recipe_base import RecipeTestBase

class RecipeViewTest(RecipeTestBase):
    # ################### #
    # View function tests #
    # ################### #

    def test_recipe_home_view_function_is_correct(self):
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func, views.home_view, msg='Home view function is incorrect')

    def test_recipe_category_view_function_is_correct(self):
        view = resolve(reverse('recipes:category', kwargs={'category_id': 1}))
        self.assertIs(view.func, views.category_view, msg='Home view function is incorrect')

    def test_recipe_recipe_view_function_is_correct(self):
        view = resolve(reverse('recipes:recipe', kwargs={'id': 1}))
        self.assertIs(view.func, views.recipe_view, msg='Home view function is incorrect')
    
    # ##################### #
    # View status 404 tests #
    # ##################### #

    def test_recipe_category_view_returns_status_code_404(self):
        response = self.client.get(reverse('recipes:category', kwargs={'category_id': 10000}))
        self.assertEqual(response.status_code, 404, msg='Category view status code is not 200')

    def test_recipe_details_view_returns_status_code_404(self):
        response = self.client.get(reverse('recipes:recipe', kwargs={'id': 100000}))
        self.assertEqual(response.status_code, 404, msg='Recipe details view status code is not 200')

    def test_recipe_details_view_returns_status_code_404_if_recipe_not_published(self):
        recipe = self.create_recipe()
        recipe.is_published = False
        recipe.save()
        response = self.client.get(reverse('recipes:recipe', kwargs={'id': 1}))
        self.assertEqual(response.status_code, 404, msg='Recipe not found status code is not 404')

    # ##################### #
    # View status 200 tests #
    # ##################### #

    def test_recipe_home_view_returns_status_code_200(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertEqual(response.status_code, 200, msg='Home view status code is not 200')


    def test_recipe_category_view_returns_status_code_200(self):
        self.create_category()
        response = self.client.get(reverse('recipes:category', kwargs={'category_id': 1}))
        self.assertEqual(response.status_code, 200, msg='Category view status code is not 200')

    def test_recipe_details_view_returns_status_code_200(self):
        self.create_recipe()
        response = self.client.get(reverse('recipes:recipe', kwargs={'id': 1}))
        self.assertEqual(response.status_code, 200, msg='Recipe details view status code is not 200')

    # ####################### #
    # View load content tests #
    # ####################### #

    def test_recipe_home_view_loads_recipes_on_context(self):
        self.create_recipe()
        recipe = Recipe.objects.all().first()
        response = self.client.get(reverse('recipes:home'))
        self.assertIn(recipe, response.context['recipes'], msg='Recipe not found in context')
    
    def test_recipe_category_view_loads_recipes_on_context(self):
        self.create_recipe()
        recipe = Recipe.objects.all().first()
        response = self.client.get(reverse('recipes:category', kwargs={'category_id': 1}))
        self.assertIn(recipe, response.context['recipes'], msg='Recipe not found in context')
    
    def test_recipe_details_view_loads_recipe_on_context(self):
        self.create_recipe()
        recipe = Recipe.objects.all().first()
        response = self.client.get(reverse('recipes:recipe', kwargs={'id': 1}))
        self.assertEqual(recipe, response.context['recipe'], msg='Recipe not found in context')


    # ############################## #
    # View successful template tests #
    # ############################## #
    
    def test_recipe_home_view_template_is_correct(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertTemplateUsed(response, 'recipes/pages/home.html')

    def test_recipe_category_view_template_is_correct(self):
        self.create_category()
        response = self.client.get(reverse('recipes:category', kwargs={'category_id': 1}))
        self.assertTemplateUsed(response, 'recipes/pages/category.html')

    def test_recipe_details_view_template_is_correct(self):
        self.create_recipe()
        response = self.client.get(reverse('recipes:recipe', kwargs={'id': 1}))
        self.assertTemplateUsed(response, 'recipes/pages/recipe.html')
        ...

    # ################################ #
    # View unsuccessful template tests #
    # ################################ #

    def test_recipe_home_view_template_shows_no_recipes_found_if_no_recipes(self):
        response = self.client.get(reverse('recipes:home'))
        content = response.content.decode('utf-8').lower()
        self.assertIn('No recipes Found'.lower(), content, msg='No recipes found message not found in content')

    def test_recipe_category_view_template_shows_no_recipes_found_if_no_recipes(self):
        self.create_category()
        response = self.client.get(reverse('recipes:category', kwargs={'category_id': 1}))
        content = response.content.decode('utf-8').lower()
        self.assertIn('No recipes Found'.lower(), content, msg='"No recipes found" message not found in content')

    def test_recipe_details_view_template_shows_no_recipes_found_or_not_published_if_no_recipes(self):
        recipe = self.create_recipe()
        recipe.is_published = False
        recipe.save()
        response = self.client.get(reverse('recipes:recipe', kwargs={'id': 1}))
        self.assertEqual(response.status_code, 404, msg='Recipe not found status code is not 404')