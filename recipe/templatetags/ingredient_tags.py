import datetime
from django import template
from django.utils.html import format_html

register = template.Library()

@register.simple_tag()
def format_step_number(recipe_steps, recipe_step, step_number):
    output_step_number = step_number

    if recipe_step.order in recipe_steps:
        output_step_number = 'X'

    output = '<p class="bg-white text-black h2 m-0 p-0 ingredient-step">{}</p>'

    return format_html(output, output_step_number)


@register.simple_tag()
def format_step_description(recipe_steps, recipe_step, step_number):
    step_class = ''

    if recipe_step.order in recipe_steps:
        step_class = 'text-strike'

    output = '<p class="text-white col m-0 p-0 {}">{}</p>'

    return format_html(output, step_class, recipe_step.description)
