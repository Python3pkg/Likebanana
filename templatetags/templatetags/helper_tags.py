from django import template
register = template.Library()

@register.filter
def split(str):
    if not str: return []
    return [x for x in str.split('\n') if x]
