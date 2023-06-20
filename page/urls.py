from django.urls import path
from . import views

urlpatterns = [
  path('', views.DefaultElementsView.as_view(), name='home'),
]