from django import template
register = template.Library()

@register.filter
def format_space_capital(string):
    string = string.replace('_', ' ')
    return string.title()