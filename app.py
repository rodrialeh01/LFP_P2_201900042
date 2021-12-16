#------------------------------IMPORTANDO LIBRERIAS------------------------------------
#tkinter
import tkinter as tk
from tkinter import Button, scrolledtext, filedialog, messagebox
from tkinter import ttk
from tkinter import *
#PILLOW
from PIL import ImageTk, Image

#VENTANA
ventana = tk.Tk()
ventana.title('MyCareer-USAC')
ventana.geometry('1250x650')
ventana.config(bg='#00144F')
ventana.iconbitmap('logoU.ico')
ventana.resizable(0,0)

#Label de Titulo
lbltitulo = Label(ventana,text='MyCareer-USAC', font='arial 20', fg='white', bg='#00144F')
lbltitulo.place(x=90, y=12)

#IMAGEN DE LOGO
imagen = ImageTk.PhotoImage(Image.open('ImagenU.png').resize((50,50)))
ilabel = Label(image=imagen, bg='#00144F')
ilabel.place(x=30, y=5)

#BOTON DE CARGAR ARCHIVO
botonca = Button(ventana,text='Cargar Archivo', font='arial 12 bold', bg="white")
botonca.place(x=550,y=20)

#BOTON DE ANALIZAR ARCHIVO
botonca = Button(ventana,text='Analizar Archivo', font='arial 12 bold', bg="white")
botonca.place(x=700,y=20)

#COMBOBOX DE OPCIONES
copciones = ttk.Combobox()
copciones.place(x=850,y=20)
copciones['values']=['Tokens','Errores','Árbol']
copciones.config(font='arial 12')

#BOTON DE GENERAR REPORTE
botonca = Button(ventana,text='Generar Reporte', font='arial 12 bold', bg="white")
botonca.place(x=1070,y=20)

#CUADRO DE TEXTO 1 (IZQUIERDO)
cuadro1 = scrolledtext.ScrolledText(ventana,bg='white',fg='black',width=70,height=35,font=('COURIER',10))
cuadro1.place(x=30, y=70)

#CUADRO DE TEXTO 2 (DERECHO)
cuadroconsola = scrolledtext.ScrolledText(ventana,bg='#222225',fg='green',width=70,height=35,font=('COURIER',10),state='disabled')
cuadroconsola.place(x=650,y=70)

ventana.mainloop()