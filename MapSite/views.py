from django.shortcuts import render, redirect
from django.http import HttpResponse
import folium
from SiteCoord.resources import SitesResource

def home(request):
    sites_resource = SitesResource()
    dataset = sites_resource.export()
    response = HttpResponse(dataset.json, headers={'Content-Type':'text/json',
    'Content-Disposition': 'inline; filename="download"'})
    
    payload = dataset.export('df')
  
    m = folium.Map(location=[9.3626764,8.8612849], zoom_start=8, tiles="OpenStreetMap")
    
    
   
    for code, name, mgr, eng, long, lat in zip(payload.SiteID, payload.SiteName, payload.SiteManager, payload.SiteEngineer, payload.Longitude, payload.Latitude):
        tooltip = code, name, eng
        label ='{},{},{}'.format(code, mgr, eng)
        label = folium.Popup(label, perse_html=True)
        folium.Marker(
            [lat,long], radius=5, popup=label, tooltip=tooltip, perse_html=False).add_to(m)
 
    m = m._repr_html_()
    context = {'SiteMap': m}
    
    
    print (type(payload))
    print (payload)
    
    return render(request, 'Mapsite/home.html', context)

    
    

