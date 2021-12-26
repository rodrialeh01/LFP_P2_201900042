#------------------------------IMPORTANDO LIBRERIAS------------------------------------
#tkinter
import tkinter as tk
from tkinter import Button, scrolledtext, filedialog, messagebox
from tkinter import ttk
from tkinter import *
#PILLOW
from PIL import ImageTk, Image

#------------------------------- LLAMANDO CLASES ---------------------------------------
from AnalizadorLexico import AnalizadorLexico
from AnalizadorSintactico import AnalizadorSintactico
from Expresiones import *
from ReporteErrores import generararchivoE
from ReporteTokens import generararchivoT
from Instrucciones import *

#--------------------------------VARIABLES GLOBALES-------------------------------------
escaner = AnalizadorLexico()

#VENTANA
ventana = tk.Tk()
ventana.title('MyCareer-USAC')
ventana.geometry('1250x680')
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

#CUADRO DE TEXTO 1 (IZQUIERDO)
cuadro1 = scrolledtext.ScrolledText(ventana,bg='white',fg='black',width=70,height=35,font=('COURIER',10))
cuadro1.place(x=30, y=70)

#FUNCION PARA OBTENER LA RUTA DEL ARCHIVO
def ObtenerRuta():
    ruta = filedialog.askopenfilename(title='Cargar Archivo', filetypes = (("Text files", "*.lfp*"), ("all files", "*.*")))
    return ruta

#FUNCION PARA CARGAR EL ARCHIVO A LA INTERFZ GRAFICA
def CargarArchivo():
    global cuadro1
    ruta = ObtenerRuta()
    if ruta != "":
        archivo = open(ruta,'r')   
        contenidoa = archivo.read()
        if cuadro1.get(1.0, END) != "":
            cuadro1.delete(1.0,END)
            cuadro1.insert(tk.INSERT, contenidoa)
        messagebox.showinfo("Success","Archivo cargado")
    else:
        messagebox.showinfo("Warning","No se cargó ningun archivo")

#FUNCION PARA ANALIZAR EL ARCHIVO LFP
def AnalizarArchivo():
    global cuadro1
    global escaner
    global cuadroconsola
    contenido = cuadro1.get(1.0, END)    
    escaner.analisis(contenido)
    #print(contenido)
    AnalizadorSintactico().analizar(escaner.listaTokens,escaner.listaErrores)
    if cuadroconsola.get(1.0, END) != "":
        cuadroconsola.config(state='normal')
        cuadroconsola.delete(1.0,END)
        cuadroconsola.insert(tk.INSERT, texto())
        cuadroconsola.config(state='disabled')

#BOTON DE CARGAR ARCHIVO
botonca = Button(ventana,text='Cargar Archivo', font='arial 12 bold', bg="white", command=CargarArchivo)
botonca.place(x=550,y=20)

#BOTON DE ANALIZAR ARCHIVO
botonca = Button(ventana,text='Analizar Texto', font='arial 12 bold', bg="white", command=AnalizarArchivo)
botonca.place(x=700,y=20)

#COMBOBOX DE OPCIONES
copciones = ttk.Combobox()
copciones.place(x=850,y=20)
copciones['values']=['Tokens','Errores','Arbol de derivacion']
copciones.config(font='arial 12')

#FUNCION PARA GENERAR LOS REPORTES
def generarReporte():
    global copciones
    global escaner
    global dot
    if (copciones.get()=="Tokens"):
        print('REPORTE DE TOKENS')
        messagebox.showinfo("Success","Reporte de Tokens generado exitosamente.")
        generararchivoT(escaner.listaTokens)
    elif (copciones.get()=="Errores"):
        print('REPORTE DE ERRORES')
        messagebox.showinfo("Success","Reporte de Errores generado exitosamente.")
        generararchivoE(escaner.listaErrores)
    elif (copciones.get()=="Arbol de derivacion"):
        print('REPORTE DE ARBOL DE DERIVACION')
        verarbol()
        messagebox.showinfo("Success","Árbol de derivación generado exitosamente.")
    else:
        messagebox.showinfo("Warning","No ha seleccionado nada valido.")

#BOTON DE GENERAR REPORTE
botonca = Button(ventana,text='Generar Reporte', font='arial 12 bold', bg="white", command=generarReporte)
botonca.place(x=1070,y=20)

#CUADRO DE TEXTO 2 (DERECHO)
cuadroconsola = scrolledtext.ScrolledText(ventana,bg='#222225',fg='white',width=70,height=35,font=('COURIER',10),state='disabled')
cuadroconsola.place(x=650,y=70)

#LABEL DE DATOS
labeld = Label(ventana,text='Proyecto 2 - 201900042', font='arial 15', fg='white', bg='#00144F')
labeld.place(x=1010, y=640)

#LABEL DE DATOS 2
labeld2 = Label(ventana,text='Lenguajes Formales y de Programación', font='arial 15', fg='white', bg='#00144F')
labeld2.place(x=30, y=640)

ventana.mainloop()