"""obps_dashboard URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from obps_dashboard.apps import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.start, name='home'),
    url(r'^dspacemetrics/$', views.dspace_metrics, name='dspacemetrics'),
    url(r'^obpsrt/$', views.obps_realtime, name='obpsrt'),
    url(r'^obpshistory/$', views.obps_history, name='obpshistory'),
    url(r'^obpshistory-mainlanding/$', views.obps_history_mainlanding, name='obpshistory_mainlanding'),
    url(r'^conferences/$', views.conferences, name='conferences'),
    url(r'^publications/$', views.publications, name='publications'),
    url(r'^newsletter/$', views.newsletter, name='newsletter'),
    url(r'^community_engagement/$', views.community_engagement, name='community_engagement'),
    url(r'^obps_workshops/$', views.obps_workshops, name='obps_workshops'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
