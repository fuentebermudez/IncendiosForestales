import pandas as pd
import numpy as np
import json
import datetime
import requests as rq
import time
import Utilidades

def format_modis_date(yymmdd):
    str_time = time.strptime(yymmdd, "%Y-%m-%d")
    year=str(str_time.tm_year)
    year_day=str(str_time.tm_yday)
    if len(str(year_day))==2:
        year_day="0"+str(year_day)
    if len(str(year_day))==1:
        year_day="00"+str(year_day)
    modis_date="A" + year + year_day
    return modis_date

def get_ndvi_serie(lat,lon,initial_date,final_date):
    header = {'Accept': 'application/json'}

    response = rq.get(
    'https://modis.ornl.gov/rst/api/v1/MOD13Q1/subset?latitude=' +lat +
    '&longitude=' +lon +
    '&startDate=' + initial_date +
    '&endDate=' + final_date +
    '&band=250m_16_days_NDVI&kmAboveBelow=5&kmLeftRight=5', headers=header)
    try:
        json_response=response.json()
        ndvi_serie=json_response['subset'][0]['data']
        ndvi=np.mean(ndvi_serie)/10000
    except:
        ndvi=np.nan
    return ndvi

def get_evapotranspiration(lat,lon,initial_date,final_date):
    header = {'Accept': 'application/json'}

    response = rq.get(
        'https://modis.ornl.gov/rst/api/v1/MOD16A2/subset?latitude=' + lat +
        '&longitude=' + lon +
        '&startDate=' + initial_date +
        '&endDate=' + final_date +
        '&band=ET_500m&kmAboveBelow=5&kmLeftRight=5', headers=header)
    try:
        json_response = response.json()
        ndvi_serie = json_response['subset'][0]['data']
        ndvi = np.mean(ndvi_serie) / 10
    except:
        ndvi = np.nan
    return ndvi


#fecha_inicial = format_modis_date(Utilidades.substract_days("2002-01-01"))
#fecha_final = format_modis_date("2002-01-01")
#a=get_evapotranspiration("42.5521829999999","-2.640673",fecha_inicial,fecha_final)
#print(a)

