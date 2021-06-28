from django.urls import path

from . import views

app_name = "SiteCoord"

urlpatterns = [
    path('', views.coordindex, name='coordindex'),
    path('export-csv/', views.export, name='export'),
]