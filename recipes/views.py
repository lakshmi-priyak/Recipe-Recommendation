# recipes/views.py
from django.shortcuts import render
from .models import Recipe, Rating
from django.db.models import Q

def recommend_recipes(request):
    recommendations = []
    if request.method == "POST":
        ingredients = request.POST.get("ingredients", "").split(",")
        if ingredients:
            recipes = Recipe.objects.all()

            for ingredient in ingredients:
                recipes = recipes.filter(ingredients__icontains=ingredient.strip())

            recommendations = recipes.order_by('-average_rating')[:10]
    
    return render(request, 'recipes/recommendations.html', {'recommendations': recommendations})
