from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView

from .models import Recipe


class RecipeListView(ListView):
    queryset = Recipe.objects.all().prefetch_related('ingredient_set', 'recipestep_set')
    paginate_by = 10


class RecipeDetailView(DetailView):
    model = Recipe
    context_object_name = 'recipe'
