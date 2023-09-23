from django import template
from contact.models import Social, About


register = template.Library()


@register.simple_tag()
def get_social_links():
    """Displaying social network links"""
    return Social.objects.all()


@register.simple_tag()
def get_about():
    """Displaying about"""
    return About.objects.last()

