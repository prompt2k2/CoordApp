from django.urls import path
from . import views
from django.conf.urls import url

#app_name = "SiteCoord"

urlpatterns = [
    
    path('json/', views.exportjson, name='exportjson'),
    path('', views.export, name='export')
]