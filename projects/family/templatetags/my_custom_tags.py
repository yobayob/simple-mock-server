from django.forms import CheckboxInput
from django import template

register = template.Library()

def is_checkbox(field):
	return field.field.widget.__class__.__name__ == CheckboxInput().__class__.__name__

register.filter('is_checkbox', is_checkbox)