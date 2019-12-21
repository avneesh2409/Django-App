from django import template

register  = template.Library()
@register.filter(name='cut')
def cut(value,arg):
    '''
    this cuts the given argument from the string
    '''
    return value.replace(arg,'')

