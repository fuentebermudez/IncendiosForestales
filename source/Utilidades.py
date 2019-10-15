import datetime
from datetime import date

def substract_days(i_date,n_days=5):
    try:
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