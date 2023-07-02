from django.contrib import admin

from .models.page import Page
from .models.element import Element
from .models.images import Image


# Create Admin Classes
class PageAdmin(admin.ModelAdmin):
  def get_changeform_initial_data(self, request):
    get_data = super(PageAdmin, self).get_changeform_initial_data(request)
    get_data['user'] = request.user.pk
    return get_data

class ElementAdmin(admin.ModelAdmin):
  def get_changeform_initial_data(self, request):
    get_data = super(ElementAdmin, self).get_changeform_initial_data(request)
    get_data['user'] = request.user.pk
    return get_data

class ImageAdmin(admin.ModelAdmin):
  prepopulated_fields = {'description': ('source',)}
  
  def get_changeform_initial_data(self, request):
    get_data = super(ImageAdmin, self).get_changeform_initial_data(request)
    get_data['user'] = request.user.pk
    return get_data


# Register your models here.
admin.site.register(Page, PageAdmin)
admin.site.register(Element, ElementAdmin)
admin.site.register(Image, ImageAdmin)