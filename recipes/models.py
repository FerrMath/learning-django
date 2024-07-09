from django.db import models
# Import user model
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100)
    preparation_time = models.IntegerField()
    preparation_unit = models.CharField(max_length=50)
    servings_count = models.IntegerField()
    servings_unit = models.CharField(max_length=50)
    preparations_steps = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    is_published = models.BooleanField(default=False)
    preparations_steps_is_html = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='recipes/covers/%Y/%m/%d/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.title