from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Avg

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    ingredients = models.TextField()
    instructions = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    average_rating = models.FloatField(default=0.0)

    def __str__(self):
        return self.title

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    rating = models.IntegerField()

    class Meta:
        unique_together = ('user', 'recipe')

    def __str__(self):
        return f'{self.user} - {self.recipe} - {self.rating}'

@receiver(post_save, sender=Rating)
def update_recipe_average_rating(sender, instance, **kwargs):
    recipe = instance.recipe
    average_rating = Rating.objects.filter(recipe=recipe).aggregate(Avg('rating'))['rating__avg']
    recipe.average_rating = average_rating or 0.0
    recipe.save()
