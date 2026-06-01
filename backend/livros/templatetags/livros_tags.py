from django import template

register = template.Library()

@register.filter
def estrelas_cheias(value):
    try:
        return range(int(value))
    except (ValueError, TypeError):
        return range(0)

@register.filter
def estrelas_vazias(value):
    try:
        return range(5 - int(value))
    except (ValueError, TypeError):
        return range(5)
