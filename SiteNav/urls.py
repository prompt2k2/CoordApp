from django.urls import path

from . import views

app_name = "SiteNav"

urlpatterns = [
    path('', views.index, name='index'),
]