from django.urls import path
from .views import (
    home,
    RecipeDetailView,
    AddRecipeView,
    EditRecipeView,
    DeleteRecipeView
)

urlpatterns = [
    path('', home, name='home'),
    path('recipe/<int:pk>/', RecipeDetailView.as_view(), name='recipe-detail'),
    path('add-recipe/', AddRecipeView.as_view(), name='add-recipe'),
    path('edit-recipe/<int:pk>/', EditRecipeView.as_view(), name='edit-recipe'),
    path('delete-recipe/<int:pk>/', DeleteRecipeView.as_view(), name='delete-recipe'),
]