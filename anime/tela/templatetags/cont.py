from django import template
register = template.Library()

cont = 0
""" @register.assignmet_tag """
@register.simple_tag
def cont():
    global cont
    return cont 
""" @register.assignmet_tag """
@register.simple_tag
def increment():
    global cont
    cont = cont + 1 
    return cont

""" @register.assignmet_tag """
@register.simple_tag
def set_to_zero():
    global cont
    cont = 0 
    return cont

