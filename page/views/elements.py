from typing import Any, Dict
from django.db.models.query import QuerySet
from django.views.generic import ListView
#from django.contrib.sites.managers import CurrentSiteManager
from django.contrib.sites.models import Site

from ..models.element import Element
from ..models.page import Page

class DefaultElementsView(ListView):
  model = Element
  def get_queryset(self) -> QuerySet[Any]:
    elements = Element.objects.filter(page__site=Site.objects.get_current())
    elements = elements.filter(page__is_default=True)
    elements = elements.filter(status=5)
    elements = elements.order_by("order", "date_published")
    return elements
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['page'] = Page.objects.filter(site=Site.objects.get_current()).filter(is_default=True).first()
    return context