"""akyltai URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from akyltai import views as book_views

urlpatterns = [
    url(r'^$',book_views.index , name='home'),
    url(r'^info/',book_views.info, name="info"),
    url(r'^admin/', admin.site.urls),
    url(r'^kabyl_aluu/',book_views.kabyl_aluu, name="kabyl_aluu"),
    url(r'^daty/',book_views.daty, name="daty"),
    url(r'^obrazovanie/',book_views.obrazovanie, name="obrazovanie"),
    url(r'^rasp/',book_views.rasp, name="rasp"),
    url(r'^metod/',book_views.metod, name="metod"),
    url(r'^kitepkana/',book_views.kitepkana, name="kitepkana"),
    url(r'^sostav/',book_views.sostav, name="sostav"),
    url(r'^krujok/',book_views.krujok, name="krujok"),
    url(r'^menyu/',book_views.menyu, name="menyu"),
    url(r'^gallery/',book_views.gallery, name="gallery"),
]
