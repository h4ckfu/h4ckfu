"""h4ckfu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
import home.views

urlpatterns = [
    path('', home.views.home, name='home'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
