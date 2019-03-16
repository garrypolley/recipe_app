from django.shortcuts import render
from django.views.generic import ListView

from .models import Recipe


class RecipeListView(ListView):
    queryset = Recipe.objects.all().prefetch_related('ingredient_set', 'recipestep_set')
    paginate_by = 10
