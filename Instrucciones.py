from Expresiones import *
import tkinter as tk
from Curso import Curso

class InstruccionInicio:
    def __init__(self, instrucciones):
        self.instrucciones = instrucciones

    def ejecutar(self, entorno):
        self.instrucciones.ejecutar(entorno)

class InstruccionInstrucciones:
    def __init__(self, instruccion, instrucciones2):
        self.instruccion = instruccion
        self.instrucciones2 = instrucciones2

    def ejecutar(self, entorno):
        self.instruccion.ejecutar(entorno)
        self.instrucciones2.ejecutar(entorno)

class InstruccionInstruccion:
    def __init__(self, instruccion):
        self.instruccion = instruccion

    def ejecutar(self, entorno):
        self.instruccion.ejecutar(entorno)

class InstruccionInstrucciones2:
    def __init__(self, instruccion, instrucciones2):
        self.instruccion = instruccion
        self.instrucciones2 = instrucciones2

    def ejecutar(self, entorno):
        if self.instruccion and self.instrucciones2:
            self.instruccion.ejecutar(entorno)
            self.instrucciones2.ejecutar(entorno)

nombrered = ''

class InstruccionNombrarred:
    def __init__(self, exp):
        self.exp = exp

    def ejecutar(self, entorno):
        #from app import cuadroconsola
        global nombrered
        valor = self.exp.getValor(entorno)
        nombrered = valor
        mensaje = 'Agregó el nombre de red como: ' + str(valor)
        #cuadroconsola.config(state='normal')
        #cuadroconsola.insert(tk.INSERT, mensaje)
        #cuadroconsola.config(state='disabled')
        print(mensaje)

#LISTA DE CURSOS
cursos = []
class InstruccionCrearcurso:
    def __init__(self, entero1, entero2, cadena, arreglo):
        self.entero1 = entero1
        self.entero2 = entero2
        self.cadena = cadena
        self.arreglo = arreglo

    def ejecutar(self, entorno):
        #from app import cuadroconsola
        global cursos
        valor1 = self.entero1.getValor(entorno)
        valor2 = self.entero2.getValor(entorno)
        valor3 = self.cadena.getValor(entorno)
        arreglo = self.arreglo.getValor(entorno)
        print(arreglo)
        cursos.append(Curso(valor1,valor2,valor3,arreglo))
        mensaje = 'Se agregó el curso ' + str(valor3)
        #cuadroconsola.config(state='normal')
        #cuadroconsola.insert(tk.INSERT, mensaje)
        #cuadroconsola.config(state='disabled')
        print(mensaje)

class InstruccionImprimirsinsalto:
    def __init__(self, exp):
        self.exp = exp

    def ejecutar(self, entorno):
        #from app import cuadroconsola
        valor = self.exp.getValor(entorno)
        #cuadroconsola.config(state='normal')
        #cuadroconsola.insert(tk.INSERT, valor)
        #cuadroconsola.config(state='disabled')
        print(valor, end=" ")

class InstruccionImprimirconsalto:
    def __init__(self, exp):
        self.exp = exp

    def ejecutar(self, entorno):
        #from app import cuadroconsola
        valor = self.exp.getValor(entorno)
        #resultado = str(valor) + '\n'
        #cuadroconsola.config(state='normal')
        #cuadroconsola.insert(tk.INSERT, resultado)
        #cuadroconsola.config(state='disabled')
        print(valor)

class InstruccionCursosporsemestre:
    def __init__(self, cod):
        self.cod = cod

    def ejecutar(self, entorno):
        global cursos
        #from app import cuadroconsola
        contenido = ''
        valor = self.cod.getValor(entorno)
        #cuadroconsola.config(state='normal')
        contenido += '\n************ SEMESTRE: ' + str(valor) + ' ************\n'
        for c in cursos:
            if int(valor) == int(c.getSemestre()):
                contenido += 'Código: ' + str(c.getCodigo()) + '\nCurso: ' + str(c.getNombre()) + '\nRequisitos:' + str(c.getPrerrequisitos()) + '\n\n'
        contenido += '************************************'
        #cuadroconsola.insert(tk.INSERT, contenido)
        #cuadroconsola.config(state='disabled')
        print(contenido)

class InstruccionCursoporcodigo:
    def __init__(self):
        pass

    def ejecutar(self, entorno):
        pass

class InstruccionCursopornombre:
    def __init__(self):
        pass

    def ejecutar(self, entorno):
        pass

class InstruccionCursosprerrequisitos:
    def __init__(self):
        pass

    def ejecutar(self, entorno):
        pass

class InstruccionCursospostrrequisitos:
    def __init__(self):
        pass

    def ejecutar(self, entorno):
        pass

class InstruccionGenerarred:
    def __init__(self):
        pass

    def ejecutar(self, entorno):
        pass

class InstruccionArreglo:
    def __init__(self):
        pass

    def ejecutar(self, entorno):
        pass

class InstruccionListaenteros:
    def __init__(self):
        pass

    def ejecutar(self, entorno):
        pass

class InstruccionListaenteros2:
    def __init__(self):
        pass

    def ejecutar(self, entorno):
        pass