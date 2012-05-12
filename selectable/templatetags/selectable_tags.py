# -*- encoding: utf-8 -*-
from django import template
from django.conf import settings


register = template.Library()


@register.inclusion_tag('selectable/jquery-js.html')
def include_jquery_libs(version='1.7.2', ui='1.8.18'):    
    return {'version': version, 'ui': ui}
