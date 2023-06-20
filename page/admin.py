from django.contrib import admin

from .models.page import Page
from .models.element import Element
from .models.images import Image

# Register your models here.
admin.site.register(Page)
admin.site.register(Element)
admin.site.register(Image)