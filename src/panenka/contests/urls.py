"""panenka URL Configuration

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
from django.conf.urls import include, url
from django.contrib.auth import views as auth_views

from .views import (
    contests_list,
    contests_create,
    contests_show
)

urlpatterns = [
    url(r'^$', contests_list, name='list'),
    url(r'^create/$', contests_create, name='create'),
    url(r'^contests(?P<contest_id>[0-9]+)/$', contests_show, name='create'),
]
