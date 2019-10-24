from joblib import dump, load
import IDRAPI_M
from tkinter import *
from tkinter.ttk import *
from tkinter import scrolledtext

def clicked():
    conf = IDRAPI_M.load_conf()
    txt.insert(END, "Obteniendo parametros.\n","a")

    AemetToken = conf['AEMET_TOKEN'][0]
    id_estacion_meteorologica=combo.get()
    latitud=lat.get()
    longitud=lng.get()

    parametros=IDRAPI_M.get_superficie_quemada(AemetToken, latitud, longitud, id_estacion_meteorologica)
    txt.insert(END,  parametros,"n")
    print(parametros)


AemetToken=""

window = Tk()
#window.bind( '<Enter>',onFormEvent )
window.title("IDRAPI")

window.geometry('350x200')

txt = Label(window, text="Hello")
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

btn = Button(window, text="Click Me", command=clicked)

btn.grid(column=1,rowspan=5)

combo_lbl=Label(window, text="Estacion meteórologica.")
combo_lbl.grid(column=2, row=1)
combo = Combobox(window)

combo['values'] = ("1387E","1475X","8177A")


combo.current(1)  # set the selected item
combo.grid(column=2, row=2)

txt = scrolledtext.ScrolledText(window, width=40, height=5)
txt.tag_config("n", background="yellow", foreground="red")
txt.tag_config("a", foreground="blue")
txt.grid(columnspan=3, row=10,padx=5)

window.mainloop()