import sys
sys.path.insert(0, 'C:\\Users\\Miguel\\PycharmProjects\\AEMET\\source\\APIs')

import IDRAPI_M
import Utilidades
from tkinter import *
from tkinter.ttk import *
from tkinter import scrolledtext

def main():
    def clicked():
        conf = IDRAPI_M.load_conf()
        txt.insert(END, "\nObteniendo parametros.\n","a")

        AemetToken = conf['AEMET_TOKEN'][0]
        path_modelo=conf['path_modelo'][0]
        #id_estacion_meteorologica=combo.get()
        latitud=lat.get()
        longitud=lng.get()
        id_estacion_meteorologica = Utilidades.get_meteo_station(latitud, longitud)
        txt.insert(END, "Estación meteorológica de referencia:" + id_estacion_meteorologica, "b")

        parametros=IDRAPI_M.get_superficie_quemada(AemetToken, latitud, longitud, id_estacion_meteorologica,path_modelo)

        resultado="\nSuperficie quemada:" + str(parametros['sup_quemada'][0])
        txt.insert(END,  resultado,"n")
        print(parametros)

        IDRAPI_M.open_url_map(latitud,longitud)
        window.focus_set()

    window = Tk()
    window.title("IDRAPI")

    window.geometry('350x200')

    txt = Label(window, text="")
    txt.grid(column=0, row=0)

    lat_lbl=Label(window, text="Lat")
    lat_lbl.grid(sticky=E)
    lat = Entry(window,width=10)
    lat.insert(0, "42.954656")
    lat.grid(column=1, row=1)

    lng_lbl=Label(window, text="Lng")
    lng_lbl.grid(sticky=E)
    lng = Entry(window,width=10)
    lng.insert(0, "-2.325719")
    lng.grid(column=1, row=2)

    btn = Button(window, text="Estima sup quemada", command=clicked)

    btn.grid(column=1,rowspan=5)

    txt = scrolledtext.ScrolledText(window, width=40, height=5)
    txt.tag_config("n", foreground="red")
    txt.tag_config("a", foreground="blue")
    txt.tag_config("b", foreground="green")
    txt.grid(columnspan=3, row=10,padx=5)

    window.mainloop()

if __name__=="__main__":
    main()