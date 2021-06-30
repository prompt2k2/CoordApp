from django.urls import path
from . import views
from django.conf.urls import url

#app_name = "SiteCoord"

urlpatterns = [
    path('siteloc/', views.siteloc, name='siteloc'),
    path('export-json/', views.exportjson, name='exportjson'),
    path('export-csv', views.export, name='export')
]