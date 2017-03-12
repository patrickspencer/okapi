"""okapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
import os
import sys
from django.conf import settings
from django.contrib import admin
from django.conf.urls import url
from django.conf.urls.static import static

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# APPS_DIR = os.path.abspath(os.path.join(BASE_DIR, "okapi", "apps"))
# sys.path.insert(1, APPS_DIR)
from okapi.apps.stockwalk import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
]
