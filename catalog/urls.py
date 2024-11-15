from django.urls import path
from catalog.apps import CatalogConfig
from catalog import views
from catalog.views import index

app_name = CatalogConfig.name

urlpatterns = [
    path("", views.home, name="index"),
    path("contacts/", views.contacts, name="contacts"),
    path('', index),
]
