import pandas as pd
import numpy as np
import time
import AEMET
import time
import csv
import Utilidades
import sys

token = token = "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJGdWVudGViZXJtdWRlekBnbWFpbC5jb20iLCJqdGkiOiI3MjMzMDA5Yi0zYmUwLTQzMTgtYWIxZC0yMzJmM2Y4YWQxNTYiLCJpc3MiOiJBRU1FVCIsImlhdCI6MTU2MDgwMTczMCwidXNlcklkIjoiNzIzMzAwOWItM2JlMC00MzE4LWFiMWQtMjMyZjNmOGFkMTU2Iiwicm9sZSI6IiJ9.N02GVYXuX9u-FIG5ljUktrDus4elnM-iVG7jthW-eg8"

def extract_meteo_data(observaciones,output,n=0):
    fires_meteo_test = observaciones

    for fire in fires_meteo_test.iterrows():
        id_fire = str(fire[1]['id'])
        fecha_inicial = Utilidades.substract_days(fire[1]['fecha'])
        fecha_final = fire[1]['fecha']
        id_estacion = fire[1]['ID_ESTACIO']
        try:
            # time.sleep(0.5)
            if n%100==0:
                print (n)
            if n % 20 == 0:
                time.sleep(5)
            datos = AEMET.get_datos_meteorologicos(token, fecha_inicial, fecha_final, id_estacion)
        except:
            time.sleep(1)
            if n % 10 == 0:
                time.sleep(5)

            datos = []
            n = n + 1

        if len(datos) > 0:
            datos = datos.mean()
            try:
                altitud = datos.altitud
            except AttributeError:
                altitud = np.nan
            try:
                tmax = datos.tmax
            except:
                tmax = np.nan
            try:
                tmin = datos.tmin
            except:
                tmin = np.nan
            try:
                prec = datos.prec
            except AttributeError:
                prec = np.nan
            try:
                velmedia = datos.velmedia
            except:
                velmedia = np.nan
            try:
                racha = datos.racha
            except:
                racha = np.nan

            valores = [n, altitud, tmax, tmin, prec, velmedia, racha]
            valores.append(id_fire)

            with open(output, 'a', newline='') as myfile:
                wr = csv.writer(myfile, quoting=csv.QUOTE_NONNUMERIC)
                wr.writerow(valores)


            n = n + 1

def main(output,n_inicio,n_final,fires_path):
    fires_meteo = pd.read_excel(fires_path, encoding='latin-1')
    observaciones = fires_meteo[n_inicio:n_final]

    extract_meteo_data(observaciones,output,n_inicio)

if __name__== "__main__":

    inicio = 0
    final=1000
    fires_path="../data/fires_join_metEstation.xlsx"
    output = 'D:\\borrar\\meteo_' + str(final) + '.txt'
    #main(sys.argv[0],sys.argv[1],sys.argv[2])
    main(output,inicio,final,fires_path)