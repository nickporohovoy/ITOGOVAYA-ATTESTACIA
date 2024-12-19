from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Recipe
from .forms import RecipeForm

# Главная страница с 5 случайными рецептами
def home(request):
    random_recipes = Recipe.objects.order_by('?')[:5]
    context = {'random_recipes': random_recipes}
    return render(request, 'home.html', context)

# Подробная информация о рецепте
class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipe_detail.html'
    context_object_name = 'recipe'

# Добавление нового рецепта
class AddRecipeView(LoginRequiredMixin, CreateView):
    form_class = RecipeForm
    template_name = 'add_recipe.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# Редактирование рецепта
class EditRecipeView(LoginRequiredMixin, UpdateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'edit_recipe.html'
    success_url = reverse_lazy('home')

# Удаление рецепта
class DeleteRecipeView(LoginRequiredMixin, DeleteView):
    model = Recipe
    template_name = 'delete_recipe.html'
    success_url = reverse_lazy('home')