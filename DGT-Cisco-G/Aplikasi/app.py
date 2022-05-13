from flask import Flask, render_template
import folium
import geopandas as gpd
import os
from folium.plugins import MousePosition
from folium.plugins import MeasureControl
from folium.plugins import Draw
from folium.plugins import MiniMap
from folium.plugins import MarkerCluster

from matplotlib.pyplot import draw
from sklearn import cluster

app = Flask(__name__)

@app.route("/")

def indeks():
    basemaps = {
        'Google Maps': folium.TileLayer(
            tiles= 'https://mt1.google.com/vt/lyrs=m&x={x}&y={y}&z={z}',
            attr= 'Google',
            name ='Google Maps',
            overlay = True,
            control = True
        ),
        'Google Satellite': folium.TileLayer(
            tiles= 'https://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}',
            attr= 'Google',
            name ='Google Satellite',
            overlay = True,
            control = True
        ),
        'Google Terrain': folium.TileLayer(
            tiles= 'https://mt1.google.com/vt/lyrs=p&x={x}&y={y}&z={z}',
            attr= 'Google',
            name ='Google Terrain',
            overlay = True,
            control = True
        ),
        'Google Satellite Hybrid': folium.TileLayer(
            tiles= 'https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}',
            attr= 'Google',
            name ='Google Satellite Hybrid',
            overlay = True,
            control = True
        ),
        'Esri Satellite': folium.TileLayer(
            tiles= 'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
            attr= 'Esri',
            name ='Esri Satellite',
            overlay = True,
            control = True
        ),
        'Stamen Terrain' : folium.TileLayer(
            tiles= 'Stamen Terrain',
            attr= 'Stamen Terrain',
            name ='Stamen Terrain',
            overlay = True,
            control = True
        ),
        'Stamen Toner' : folium.TileLayer(
            tiles= 'Stamen Toner',
            attr= 'Stamen Toner',
            name ='Stamen Toner',
            overlay = True,
            control = True
        ),
        'CartoDB Positron' : folium.TileLayer(
            tiles= 'CartoDB Positron',
            attr= 'CartoDB Positron',
            name ='CartoDB Positron',
            overlay = True,
            control = True
        ),
        'OpenStreetMap' : folium.TileLayer(
            tiles= 'OpenStreetMap',
            attr= 'OpenStreetMap',
            name ='OpenStreetMap',
            overlay = True,
            control = True
        )
    }
    
    # Directory Path
    r = os.path.dirname(os.path.abspath(__file__))
    
    # Baca Data Konversi shapefile ke json
    batas_desa = gpd.read_file(r+'/assets/Desa.shp')
    batas_desa.to_file(r+'/assets/Desa.json', driver='GeoJSON')
    
    batas_kecamatan = gpd.read_file(r+'/assets/Kecamatan.shp')
    batas_kecamatan.to_file(r+'/assets/Kecamatan.json', driver='GeoJSON')
    
    toko_modern_point = gpd.read_file(r+'/assets/Toko_Modern_Centroids.shp')
    toko_modern_point.to_file(r+'/assets/Toko_Modern_Centroids.json', driver='GeoJSON')
    
    
    # Membaca data DBF
    valuesdesa = gpd.read_file(r+'/assets/Desa.dbf')
    
    start_coord = [-6.1950, 106.5528]
    map = folium.Map(location=start_coord, zoom_start=11, control_scale=True, height=650, width="100%")
    

    # Chloroplet 
    # batas_kecamatan = folium.Choropleth(
    #     geo_data = batas_kecamatan,                                           #data geojson
    #     name = 'Kepadatan Penduduk Kecamatan',                                #nama
    #     data = valueskecamatan,                                               #data tabel  
    #     columns =['KECAMATAN', 'KEP_PEND'],                                   #colom dari tabel
    #     key_on ="properties.KECAMATAN",                                       #kunci
    #     fill_color = 'Spectral_r',                                            #pallete
    #     fill_opacity = 0.75,                                                  #transparansi fill
    #     line_opacity = 0.3,                                                   #transparansi outline
    #     legend_name = f"Kepadatan Penduduk per kecamatan Kabupaten Tangerang Tahun 2015",   #legenda
    #     smooth_factor= 0.05,
    # ).add_to(map)
    
    batas_desa = folium.Choropleth(
        geo_data = batas_desa,                                                #data geojson
        name = 'Kepadatan Penduduk Desa & Kelurahan',                         #nama
        data = valuesdesa,                                                    #data tabel  
        columns =['DESA_KEL', 'KEP_PEND'],                                    #colom dari tabel
        key_on ="properties.DESA_KEL",                                        #kunci
        fill_color = 'Spectral_r',                                            #pallete
        fill_opacity = 0.75,                                                  #transparansi fill
        line_opacity = 0.3,                                                   #transparansi outline
        legend_name = f"Kepadatan Penduduk per desa/kel Kabupaten Tangerang Tahun 2015",   #legenda
        smooth_factor= 0.05
    ).add_to(map)
     
    # Toolkit and Pop Up
    style_function = "font-size: 10px; font-weight: bold"
    
    # batas_kecamatan.geojson.add_child(folium.features.GeoJsonTooltip(['KECAMATAN','KEP_PEND'], style=style_function, labels=True))
    
    batas_desa.geojson.add_child(folium.features.GeoJsonTooltip(['DESA_KEL','KECAMATAN','KEP_PEND'], style=style_function, labels=True))
    
    
    # Cluster Marker
    toko_modern_point["x"] = toko_modern_point["geometry"].x
    toko_modern_point["y"] = toko_modern_point["geometry"].y
    
    locations = list(zip(toko_modern_point["y"], toko_modern_point["x"], toko_modern_point['N_Alfamart']))
    
    marker_cluster = MarkerCluster().add_to(map)
    
    for  POINT_Y, POINT_X, NAMAOBJ in locations :
        folium.Marker(location=[POINT_Y, POINT_X],popup= NAMAOBJ, icons="darkblue", clustered_Marker= True, style=style_function, name = "Toko Modern").add_to(marker_cluster)

    
    # Basemap
    for basemap, TileLayer in basemaps.items():
        basemaps[basemap].add_to(map)
    
    folium.LayerControl().add_to(map)
    
    #mouse position
    fmtr = "function(num) {return L.Util.formatNum(num,3) + ' degres';};"
    
    
    # Plugins
    Draw (
        export=False, 
        filename='/assets/test.geojson', 
        position="topleft", 
        draw_options = None, 
        edit_options = None
        ).add_to(map)
    
    MousePosition (
        position='bottomright', 
        Separator = "|", 
        prefix="Mouse:", 
        lat_formatter=fmtr, 
        lng_formatter=fmtr
        ).add_to(map)
    
    MeasureControl (
        position='topright',
        primary_length_unit='meters',
        secondary_length_unit='kilometers',
        primary_area_unit='sqmeters',
        secondary_area_unit='acres'
        ).add_to(map)
    
    minimap = MiniMap()
    map.add_child(minimap)
    
    map.save(r+'/templates/map.php')
    return render_template('index.php',)
    # return map._repr_html_()


if __name__ == "__main__":
    app.run(debug=True) 