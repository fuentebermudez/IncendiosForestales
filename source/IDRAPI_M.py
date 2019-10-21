import Utilidades
from APIs import AEMET as aemet
from APIs import MODIS as modis
import datetime

token="eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJGdWVudGViZXJtdWRlekBnbWFpbC5jb20iLCJqdGkiOiI3MjMzMDA5Yi0zYmUwLTQzMTgtYWIxZC0yMzJmM2Y4YWQxNTYiLCJpc3MiOiJBRU1FVCIsImlhdCI6MTU2MDgwMTczMCwidXNlcklkIjoiNzIzMzAwOWItM2JlMC00MzE4LWFiMWQtMjMyZjNmOGFkMTU2Iiwicm9sZSI6IiJ9.N02GVYXuX9u-FIG5ljUktrDus4elnM-iVG7jthW-eg8"

def get_meteo_data(token,initial_date,final_date,id_estacion):
    date=datetime.date
    datos_meteorologicos=aemet.get_datos_meteorologicos(token,initial_date,final_date,id_estacion)
    return datos_meteorologicos

def get_modis(lat,long):
    fecha = datetime.date.today()
    fechas=get_date_actual()
    

def get_date_actual():
    fecha=datetime.date.today()
    fecha_anterior=Utilidades.substract_days(fecha)
    return {'fecha_final':str(fecha),'fecha_inicial':fecha_anterior}

fechas=get_date_actual()
fecha_inicial=fechas['fecha_inicial']
fecha_final=fechas['fecha_final']

meteo_data=get_meteo_data(token,fecha_inicial,fecha_final,'1475X')


