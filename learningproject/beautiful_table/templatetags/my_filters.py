from django import template

register = template.Library()


@register.filter(name='times')
def times(value, n=0):
    return ' ' * n
