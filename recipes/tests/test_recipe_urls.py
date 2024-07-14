from django.test import TestCase
from django.urls import reverse

# Create your tests here.
class RecipeUrlsTest(TestCase):
    def test_recipe_home_url_is_correct(self):
        home_reverse_url = reverse('recipes:home')
        print(f'Home URL: {home_reverse_url}')
        self.assertEqual(home_reverse_url, '/')
    
    def test_category_view_url_is_correct(self):
        # Can also use just args, but it has to be in the order of the URL
        category_reverse_url = reverse('recipes:category', kwargs={'category_id': 1}) 
        print(f'Category URL: {category_reverse_url}')
        self.assertEqual(category_reverse_url, '/recipes/categories/1/', msg='Category URL is incorrect')

    def test_recipe_detail_view_url_is_correct(self):
        recipe_reverse_url = reverse('recipes:recipe', kwargs={'id': 1})
        print(f'Recipe URL: {recipe_reverse_url}')
        self.assertEqual(recipe_reverse_url, '/recipes/1/', msg='Recipe URL is incorrect')
