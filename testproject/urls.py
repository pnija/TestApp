from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from testapp.views import *
from testapp import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', LocationCreate.as_view(), name='home'),
    url(r'^listlocations/$', LocationList.as_view(), name='listloc'),
    url(r'^fluctuations/$', FluctuationView.as_view(), name='fluctuations'),
]
