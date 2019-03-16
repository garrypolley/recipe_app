from django.core.serializers.json import DjangoJSONEncoder
from django.core.serializers import serialize
from django import template

register = template.Library()


@register.filter(name='to_json', is_safe=True)
def to_json(value):
    to_serial = value if hasattr(value, '__iter__') else [value]
    return serialize('json', to_serial)
