from django.template import Library

register = Library()

@register.filter
def get_lastvalue(value):
    if value:
        return str(value).split("/")[-1]