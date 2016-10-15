from django import template

from dicadm_django.dictionary.models import Category

register = template.Library()

@register.inclusion_tag('dictionary/cats.html')
def get_category_list():
	return {'cats' : Category.objects.all()}
