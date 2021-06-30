from django.contrib.admin.options import ModelAdmin
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .resources import SitesResource
import pandas as pd


def export(request):
    sites_resource = SitesResource()
    dataset = sites_resource.export()
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="sitesinfo.csv"'
   
    return response


def exportjson(request):
    sites_resource = SitesResource()
    dataset = sites_resource.export()
    response = HttpResponse(dataset.json, content_type='application/json')
    response['Content-Disposition'] = 'attachment; filename="sites.json"'
    return response


def siteloc(request):
    sites_resource = SitesResource()
    dataset = sites_resource.export()
    response = HttpResponse(dataset.json, content_type='text/json')
    response['Content-Disposition'] = 'inline; filename=""'
    #sites_resource = sites_resource
    #dataset = {'SiteData': sites_resource}
    #return render(request, 'SiteCoord/siteloc.html', dataset)
    df = pd.read_json(response, lines=True)
    return df