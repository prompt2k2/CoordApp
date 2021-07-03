from django.shortcuts import render, redirect
from django.http import HttpResponse
import folium, pandas as pd, json
from SiteCoord.resources import SitesResource
from SiteCoord.models import Sites
from SiteCoord.forms import FormSite
from django.views.generic.detail import DetailView


def home(request):
    sites_resource = SitesResource()
    dataset = sites_resource.export()
    response = HttpResponse(dataset.json, headers={'Content-Type':'text/json',
    'Content-Disposition': 'inline; filename="download"'})
    
    payload = dataset.export('df')
  
    m = folium.Map(location=[9.3626764,8.8612849], zoom_start=8, tiles="OpenStreetMap")
    
    
   
    for code, name, mgr, eng, lat, long in zip(payload.SiteID, payload.SiteName, payload.SiteManager, payload.SiteEngineer, payload.Longitude, payload.Latitude):
        tooltip = code, name, eng
        label ='{},{},{}'.format(code, mgr, eng)
        label = folium.Popup(label, perse_html=True)
        folium.Marker(
            [lat,long], radius=5, popup=label, tooltip=tooltip, perse_html=False).add_to(m)
 
    m = m._repr_html_()
    context = {'SiteMap': m}
    
    return render(request, 'Mapsite/home.html', context)

#Displays Sites Record to /home/sites    
def AllSite(request): 
    sites_resource = SitesResource()
    dataset = sites_resource.export()
    
    payload = dataset.export('df')
    datajson = payload.reset_index().to_json(orient='records')
    data = []
    data = json.loads(datajson)
    context = {'data': data}    
    
    return render(request, "Mapsite/sitelist.html", context)

#References the SiteCoord.forms function for iterable site list
def SiteList(request, id=0):
    if request.method == 'POST':
        if id == 0:
            form = FormSite(request.POST)
        else:
            site = Sites.objects.get(pk=id)
            form = FormSite(request.POST, instance=site)
        if form.is_valid():
            form.save()
            return redirect('/home/sites')#points to the URL path
    else:
        if id == 0:
            form = FormSite()
        else:
            site = Sites.objects.get(pk=id)
            form = FormSite(instance=site)
        print()    
        return render(request, "Mapsite/siteform.html", {'form':form})
            
    
def SiteDetail(request, id):
    context = {'data': Sites.objects.get(id = id)}
    print(context)
    return render(request, "Mapsite/siteup.html", {'context':context})