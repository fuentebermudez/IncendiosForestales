import datetime
import pandas as pd
import numpy as np
from math import radians, sin, cos, sqrt, asin
import os

from datetime import date

def substract_days(i_date,n_days=5):
    try:
        i_date=str(i_date)
        datea=datetime.datetime.strptime(i_date, "%Y-%m-%d")
    except:
        print("Date fromat error.")
    atras=datetime.timedelta(days=n_days)
    return (str((datea-atras)).split(' ')[0])

def set_numeric_values(datos):
    for column in datos.columns:
        try:
            datos[column]=datos[column].str.replace(",",".")
            datos[column]=datos[column].astype(float)
        except:
            datos[column]=datos[column]
    return datos


def haversine(lat1, lon1, lat2, lon2):
    R = 6372.8  # Earth radius in kilometers

    dLat = radians(lat2 - lat1)
    dLon = radians(lon2 - lon1)
    lat1 = radians(lat1)
    lat2 = radians(lat2)

    a = sin(dLat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dLon / 2) ** 2
    c = 2 * asin(sqrt(a))

    return R * c

def get_meteo_station(lat,lon):
    lat=float(lat)
    lon=float(lon)
    os.chdir("./rec/")
    meteo_stations=pd.read_csv('estaciones_meteorologicas_normalizada.txt')
    distance_station=10000
    id_station=""
    for meteo_station in meteo_stations.iterrows():
        id_station_item=meteo_station[1][2]
        lat_meteo_station=float(meteo_station[1][10])
        lon_meteo_station=float(meteo_station[1][11])
        d=haversine(lat,lon,lat_meteo_station,lon_meteo_station)
        if d<distance_station:
            distance_station=d
            id_station=id_station_item
    return (id_station)
