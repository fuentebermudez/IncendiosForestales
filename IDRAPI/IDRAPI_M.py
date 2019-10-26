
from joblib import load
import os
import datetime
import pandas as pd
import numpy as np
import webbrowser

import Utilidades
from APIs import AEMET
from APIs import MODIS
from APIs import IGN

def get_meteo_data(token,id_estacion):
    fechas = get_date_actual(5)
    fecha_inicial = fechas['fecha_inicial']
    fecha_final = fechas['fecha_final']

    datos_meteorologicos= AEMET.get_datos_meteorologicos(token, fecha_inicial, fecha_final, id_estacion)
    return datos_meteorologicos

def get_modis_data(lat,lon):
    lat=str(lat)
    lon=str(lon)
    fechas=get_date_actual(20)
    fecha_inicial_modis_format= MODIS.format_modis_date(fechas['fecha_inicial'])
    fecha_final_modis_format = MODIS.format_modis_date(fechas['fecha_final'])
    ndvi= MODIS.get_ndvi_serie(lat, lon, fecha_inicial_modis_format, fecha_final_modis_format)
    eto= MODIS.get_evapotranspiration(lat, lon, fecha_inicial_modis_format, fecha_final_modis_format)

    return {'ndvi':ndvi,'eto':eto}

def get_date_actual(n_days):
    fecha=datetime.date.today()
    fecha_final=Utilidades.substract_days(fecha,n_days)
    fecha_inicial=Utilidades.substract_days(fecha_final,n_days)
    return {'fecha_final':fecha_final,'fecha_inicial':fecha_inicial}

def get_ign_data(lat,lng):
    pendiente= IGN.get_slope(lat, lng)
    return {'pendiente':float(pendiente)}

def get_data_modelo(AemetToken,lat,lng,id_estacion_meteorologica):
    meteo_data = get_meteo_data(AemetToken, id_estacion_meteorologica)
    meteo_data = meteo_data.mean()
    modis_data = get_modis_data(lat, lng)
    ign_data = get_ign_data(lat, lng)

    altitud=meteo_data['altitud']
    latitud =lat
    longitud =lng
    tmax =meteo_data['tmax']
    tmin =meteo_data['tmin']
    racha =meteo_data['racha']
    velmedia =meteo_data['velmedia']
    ndvi =modis_data['ndvi']
    eto = modis_data['eto']
    pendiente =ign_data['pendiente']

    parametros=np.asarray([altitud,latitud,longitud,tmax,tmin,racha,velmedia,ndvi,eto,pendiente]).reshape(1,-1)
    return(parametros)

def load_conf():
    '''os.chdir("..")
    path=os.path.realpath(os.curdir)
    path_conf=str(path + "\conf\conf.json")
    os.chdir(os.curdir)
    conf=pd.read_json(path_conf)'''
    conf = pd.read_json("C:\\Users\\Miguel\\PycharmProjects\\AEMET\\conf\\conf.json")
    return dict(conf)

def load_model(path_model):
    model=load(path_model)
    return model

def get_superficie_quemada(AemetToken,lat,lng,id_estacion_meteorologica,path_modelo="..\output\models\clf.joblib"):
    model=load_model(path_modelo)
    parametros=get_data_modelo(AemetToken,lat,lng,id_estacion_meteorologica)
    sup_quemada=model.predict(parametros)
    return {"sup_quemada":sup_quemada,"parametros":parametros}

def open_url_map(lat,lng):
    webbrowser.open_new_tab("https://www.google.com/maps/@?api=1&map_action=map&center=" + lat + "," + lng+"&zoom=15&basemap=terrain")

