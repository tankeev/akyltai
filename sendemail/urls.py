from django.contrib import admin
from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^contact/', views.emailView, name='contact'),
    url('success/', views.successView, name='success'),
]