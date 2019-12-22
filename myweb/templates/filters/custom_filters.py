from django import template

register  = template.Library()
@register.filter(name='cut')
def cut(value,arg):
    '''
    this cuts the given argument from the string
    '''
    return value.replace(arg,'')

@register.filter(name='uppercase')
def uppercase(value,arg):
    '''
    this function will convert a given string into its uppercase quivalent
    '''
    return value.uppercase()
