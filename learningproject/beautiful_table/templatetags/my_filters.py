from django import template

register = template.Library()


@register.filter(name='times')
def times(value):
    return range(value)


@register.filter(name='filter_range')
def filter_range(value, n=0):
    return range(value, n)
