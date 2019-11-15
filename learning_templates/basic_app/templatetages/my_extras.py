from django import template

register = template.Library()

def cut(value,arg):
    # this cuts out all values of "arg" the string!
    return value.replace(arg,'')

register.filter('cut',cut)    
