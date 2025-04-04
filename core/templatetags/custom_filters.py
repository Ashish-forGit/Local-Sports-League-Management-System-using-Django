from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    """Retrieve value from a dictionary using a key"""
    return dictionary.get(key, "N/A")  # Returns "N/A" if the key is missing
