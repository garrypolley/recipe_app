from django.contrib import admin

from .models import Recipe, Ingredient, RecipeStep


class IngredientAdmin(admin.StackedInline):
    model = Ingredient
    extra = 1


class RecipeStepsAdmin(admin.StackedInline):
    model = RecipeStep
    extra = 1


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
   inlines = [IngredientAdmin, RecipeStepsAdmin]
   list_display = ['name', 'uuid', 'description']
