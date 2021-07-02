from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sites/', views.AllSite, name='AllSite'),
    #path('export-csv', include('SiteCoord.urls'), name='export'),
]
