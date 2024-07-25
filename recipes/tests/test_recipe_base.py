from django.test import TestCase
from django.urls import resolve, reverse

from recipes import views
from recipes.models import Category, Recipe, User

class RecipeTestBase(TestCase):
    
    def create_category(self, name='Test Category'):
        return Category.objects.create(name=name)
    

    def create_author(self, first_name='Test',last_name='User',username='testuser',password='12345',email='testuser@email.com'):
        return User.objects.create_user(
            first_name= first_name,
            last_name= last_name,
            username= username,
            password= password,
            email= email
        )
    

    def create_recipe(self, title='Test Recipe', description='Test Description', slug='test-recipe', preparation_time=10, preparation_unit='minutes', servings_count=4, servings_unit='people', preparation_steps='Test Preparation Steps', author_data=None, category_data=None):
        
        if author_data is None:
            author_data = {}
        
        if category_data is None:
            category_data = {}
        
        return Recipe.objects.create(
            title=title,
            description= description,
            slug= slug,
            preparation_time= preparation_time,
            preparation_unit= preparation_unit,
            servings_count= servings_count,
            servings_unit= servings_unit,
            preparation_steps= preparation_steps,
            user= self.create_author(**author_data),
            category= self.create_category(**category_data),
            is_published= True
        )