from django.shortcuts import render, redirect
import folium
import os

def home(request):
    
    shp_dir = os.path.join(os.getcwd(), 'media', 'shp')
    m = folium.Map(location=[9.3626764,8.8612849], zoom_start=8)
    style_basin = {'fillcolor':'#228B22', 'color':'#228B22'}
    style_rivers = {'color':'blue'}
    
    #folium.GeoJson(os.path.join(shp_dir, 'rivers.geojson'), name='rivers', style_function=lambda x:style_rivers).add_to(m)
    #folium.GeoJson(os.path.join(shp_dir, 'basin.geojson'), name='basin', style_function=lambda x:style_basin).add_to(m)
    
    folium.LayerControl().add_to(m)
    
    m = m._repr_html_()
    context = {'SiteMap': m}
    return render(request, 'Mapsite/home.html', context)


