# Add this path to your urls.py
# recipes/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('recommendations/', views.recommend_recipes, name='recommendations'),
    path('recommendations/search/', views.recommend_recipes, name='recommendations_search'),
]