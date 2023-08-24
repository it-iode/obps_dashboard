"""obps_dashboard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  re_path(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  re_path(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import re_path, include
    2. Add a URL to urlpatterns:  re_path(r'^blog/', include('blog.urls'))
"""
from django.urls import re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from obps_dashboard.apps import views

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^$', views.start, name='home'),
    re_path(r'^dspacemetrics/$', views.dspace_metrics, name='dspacemetrics'),
    re_path(r'^obpsrt/$', views.obps_realtime, name='obpsrt'),
    re_path(r'^obpshistory/$', views.obps_history, name='obpshistory'),
    re_path(r'^obpshistory-mainlanding/$', views.obps_history_mainlanding, name='obpshistory_mainlanding'),
    re_path(r'^newsletter/$', views.newsletter, name='newsletter'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
