
from django.http import HttpResponse
from .resources import SitesResource


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

