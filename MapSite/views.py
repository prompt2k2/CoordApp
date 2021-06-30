from django.shortcuts import render, redirect
import folium
import os
from SiteCoord.views import siteloc

def home(request):
    
    shp_dir = os.path.join(os.getcwd(), 'media', 'shp')
    m = folium.Map(location=[9.3626764,8.8612849], zoom_start=8)
    #style_basin = {'fillcolor':'#228B22', 'color':'#228B22'}
    #style_rivers = {'color':'blue'}
    
    #folium.GeoJson(os.path.join(shp_dir, 'rivers.geojson'), name='rivers', style_function=lambda x:style_rivers).add_to(m)
    #folium.GeoJson(os.path.join(shp_dir, 'basin.geojson'), name='basin', style_function=lambda x:style_basin).add_to(m)
    
    #folium.LayerControl().add_to(m)
    for code, name, mgr, eng, long, lat in zip(siteloc[1],siteloc.SiteName, siteloc.SiteManager, siteloc.SiteEngineer, siteloc.Longitude, siteloc.Latitude):
        label ='{},{},{}'.format(code, mgr, eng)
        label = folium.Popup(label, perse_html=True)
        folium.CircleMaker(
            [lat,long], radius=5, popup=label, color='red', fill=True, fill_color='green', fill_opacity=0.6, perse_html=False).add_to(m)
    
    m = m._repr_html_()
    context = {'SiteMap': m}
    return render(request, 'Mapsite/home.html', context)

'''
def Maker(request):
    Nigeria = folium.Map(location=[19.3626764,18.8612849], zoom_start=8)
    for code, name, mgr, eng, long, lat in zip(siteloc.SiteID,siteloc.SiteName, siteloc.SiteManager, siteloc.SiteEngineer, siteloc.Longitude, siteloc.Latitude):
        label ='{},{},{}'.format(code, mgr, eng)
        label = folium.Popup(label, perse_html=True)
        folium.CircleMaker(
            [lat,long], radius=5, popup=label, color='red', fill=True, fill_color='green', fill_opacity=0.6, perse_html=False).add_to(Nigeria)
    
    Nigeria = Nigeria._repr_html_()
    context = {'MapMaker': Nigeria}
    return render(request, 'Mapsite/home.html', context)
    
    '''