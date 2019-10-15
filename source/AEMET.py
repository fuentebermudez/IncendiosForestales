import json
import requests
import pandas as pd
import Utilidades

token="eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJGdWVudGViZXJtdWRlekBnbWFpbC5jb20iLCJqdGkiOiI3MjMzMDA5Yi0zYmUwLTQzMTgtYWIxZC0yMzJmM2Y4YWQxNTYiLCJpc3MiOiJBRU1FVCIsImlhdCI6MTU2MDgwMTczMCwidXNlcklkIjoiNzIzMzAwOWItM2JlMC00MzE4LWFiMWQtMjMyZjNmOGFkMTU2Iiwicm9sZSI6IiJ9.N02GVYXuX9u-FIG5ljUktrDus4elnM-iVG7jthW-eg8"

def get_json_response(response_AEMET):

    datos_url=response_AEMET['datos']
    datos=requests.request("GET",datos_url)
    return pd.DataFrame(eval(datos.text))

def get_data_AEMET(url,token):
    querystring = {"api_key": token}
    headers = {'cache-control': "no-cache"}

    response = requests.request("GET", url, headers=headers, params=querystring)
    json_data = json.loads(response.content)
    datos = get_json_response(json_data)
    datos=Utilidades.set_numeric_values(datos)
    return datos

def get_estaciones_meteorologicas(token):
    url="https://opendata.aemet.es/opendata/api/valores/climatologicos/inventarioestaciones/todasestaciones"
    #url = "https://opendata.aemet.es/opendata/api/valores/climatologicos/diarios/datos/fechaini/2017-01-01T12%3A01%3A01UTC/fechafin/2017-02-01T12%3A01%3A01UTC/todasestaciones"
    datos=get_data_AEMET(url,token)
    return datos

def get_datos_meteorologicos(token,initial_date,final_date,id_estacion):
    url = "https://opendata.aemet.es/opendata/api/valores/climatologicos/diarios/datos/fechaini/" + \
          initial_date + \
          "T12%3A01%3A01UTC/fechafin/" + \
          final_date + \
          "T12%3A01%3A01UTC/estacion/" + \
          id_estacion
    datos = get_data_AEMET(url, token)
    return datos

def get_datos_meteorologicos_todas(token,initial_date,final_date):
    url = "https://opendata.aemet.es/opendata/api/valores/climatologicos/diarios/datos/fechaini/" + \
          initial_date + \
          "T12%3A01%3A01UTC/fechafin/" + \
          final_date + \
          "T12%3A01%3A01UTC/todasestaciones/"
    datos = get_data_AEMET(url, token)
    return datos



