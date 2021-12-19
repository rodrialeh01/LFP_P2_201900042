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

contenido = ''
def ObtenerRuta():
    ruta = filedialog.askopenfilename(title='Cargar Archivo', filetypes = (("Text files", "*.lfp*"), ("all files", "*.*")))
    return ruta

def CargarArchivo():
    global contenido
    global cuadro1
    ruta = ObtenerRuta()
    if ruta != "":
        archivo = open(ruta,'r')   
        contenido = archivo.read()
        if cuadro1.get(1.0, END) != "":
            cuadro1.delete(1.0,END)
            cuadro1.insert(tk.INSERT, contenido)
        messagebox.showinfo("Success","Archivo cargado")
    else:
        messagebox.showinfo("Warning","No se cargó ningun archivo")

def AnalizarArchivo():
    global contenido
    a = AnalizadorLexico()
    a.analisis(contenido)
    a.imprimir()

#BOTON DE CARGAR ARCHIVO
botonca = Button(ventana,text='Cargar Archivo', font='arial 12 bold', bg="white", command=CargarArchivo)
botonca.place(x=550,y=20)

#BOTON DE ANALIZAR ARCHIVO
botonca = Button(ventana,text='Analizar Texto', font='arial 12 bold', bg="white", command=AnalizarArchivo)
botonca.place(x=700,y=20)

#COMBOBOX DE OPCIONES
copciones = ttk.Combobox()
copciones.place(x=850,y=20)
copciones['values']=['Tokens','Errores','Árbol']
copciones.config(font='arial 12')

#BOTON DE GENERAR REPORTE
botonca = Button(ventana,text='Generar Reporte', font='arial 12 bold', bg="white")
botonca.place(x=1070,y=20)

#CUADRO DE TEXTO 2 (DERECHO)
cuadroconsola = scrolledtext.ScrolledText(ventana,bg='#222225',fg='green',width=70,height=35,font=('COURIER',10),state='disabled')
cuadroconsola.place(x=650,y=70)

#LABEL DE DATOS
labeld = Label(ventana,text='Proyecto 2 - 201900042', font='arial 15', fg='white', bg='#00144F')
labeld.place(x=1010, y=640)

#LABEL DE DATOS 2
labeld2 = Label(ventana,text='Lenguajes Formales y de Programación', font='arial 15', fg='white', bg='#00144F')
labeld2.place(x=30, y=640)

ventana.mainloop()