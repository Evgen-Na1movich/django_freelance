from django import template

import freelance.views as views

register = template.Library()


@register.simple_tag()
def get_menu():
    return views.menu
