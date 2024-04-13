from django.urls import path, include
from catalog.views import home, contacts
from django.contrib import admin
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
]
