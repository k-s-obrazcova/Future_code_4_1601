from django import template

register = template.Library()

@register.simple_tag()
def multiply(val1, val2):
    return val1 * val2

@register.simple_tag()
def hello_user(user):
    return f"Привет {user}! Добро пожаловать на сайт)"