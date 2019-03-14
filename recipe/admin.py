from django.contrib import admin

from .models import Recipe, Ingredient, RecipeStep

class IngredientAdmin(admin.StackedInline):
    model = Ingredient


class RecipeStepsAdmin(admin.StackedInline):
    model = RecipeStep


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
   inlines = [RecipeStepsAdmin, IngredientAdmin]
