from uuid import uuid4

from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth import get_user_model


MEASUREMENT_CHOICES = (
    ('g', _('gram')),
    ('mg', _('milligram')),
    ('l', _('liter')),
    ('ml', _('milliliter')),
    ('oz', _('ounce')),
    ('floz', _('fluid oz')),
    ('cup', _('cup')),
    ('lb', _('lb')),
    ('tsp', _('teaspoon')),
    ('tbs', _('tablespoon')),
    ('qrt', _('quart')),
    ('pt', _('pint')),
)


class TimeTrackedModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


User = get_user_model()


class Recipe(TimeTrackedModel):
    uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=500)
    description = models.TextField()
    final_product_photo = models.FileField(blank=True, null=True)
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)


class RecipeStep(TimeTrackedModel):
    description = models.TextField()
    order = models.IntegerField()
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    class Meta:
        ordering = ('order', )


class Ingredient(TimeTrackedModel):
    uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=300)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    # The goal is to only store as g or ml
    unit = models.CharField(max_length=200, choices=MEASUREMENT_CHOICES)

    class Meta:
        ordering = ('name', )
