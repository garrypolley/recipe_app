from django.conf import settings
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

    def get_context_data(self, *args, **kwargs):
        context = super(RecipeDetailView, self).get_context_data(*args, **kwargs)
        context['chosen_steps'] = [int(x) for x in self.request.GET.getlist('rst')]
        context['site_url'] = settings.SITE_URL

        return context
