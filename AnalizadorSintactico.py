#-----------------------------------IMPORTANDO CLASES----------------------------------
from Clases import Token,Error
from Expresiones import *
from Instrucciones import *

#-----------------------------------VARIABLES GLOBALES---------------------------------
raizarbol = ''

class AnalizadorSintactico:
    def __init__(self):
        self.listaTokens = []
        self.listaErrores = []
        self.i = 0

    #FUNCION DEL ORDEN DE LISTADEENTEROS2
    def listaenteros2(self):
        if self.listaTokens[self.i].tipo == 'tk_coma':
            self.i += 1
            if self.listaTokens[self.i].tipo == 'tk_entero':
                lexema = self.listaTokens[self.i].lexema
                entero = ExpresionLiteral('entero',lexema)
                self.i += 1
                lista = self.listaenteros2()
                return ExpresionListaEnteros2(entero,lista)
        elif self.listaTokens[self.i].tipo == 'tk_corchetec':
            return ExpresionListaEnteros2(None,None)

    #FUNCION DEL ORDEN DE LISTADEENTEROS
    def listaenteros(self):
        if self.listaTokens[self.i].tipo == 'tk_entero':
            lex = self.listaTokens[self.i].lexema
            entero = ExpresionLiteral('entero',lex)
            self.i += 1
            lista = self.listaenteros2()
            return ExpresionListaEnteros(entero,lista)
        elif self.listaTokens[self.i].tipo == 'tk_corchetec':
            return ExpresionListaEnteros2(None,None)

    #FUNCION DE ORDEN DE ARREGLO
    def arreglo(self):
        if self.listaTokens[self.i].tipo == 'tk_corchetea':
            self.i += 1
            lista = self.listaenteros()
            if self.listaTokens[self.i].tipo == 'tk_corchetec':
                self.i += 1
                return ExpresionArreglo(lista)

    #FUNCION DE ORDEN DE GENERARRED
    def generarred(self):
        if self.listaTokens[self.i].tipo == 'tk_generarRed':
            self.i += 1
            if self.listaTokens[self.i].tipo == 'tk_parentesisa':
                self.i += 1
                if self.listaTokens[self.i].tipo == 'tk_cadena':
                    cadena = self.listaTokens[self.i].lexema
                    excadena = ExpresionLiteral('cadena',cadena)
                    self.i += 1
                    if self.listaTokens[self.i].tipo == 'tk_parentesisc':
                        self.i += 1
                        if self.listaTokens[self.i].tipo == 'tk_puntoycoma':
                            self.i += 1
                            return InstruccionGenerarred(excadena)

    #FUNCION DE ORDEN DE CURSOSPOSTRREQUITOS
    def cursospostrrequisitos(self):
        if self.listaTokens[self.i].tipo == 'tk_cursosPostrrequisitos':
            self.i += 1
            if self.listaTokens[self.i].tipo == 'tk_parentesisa':
                self.i += 1
                if self.listaTokens[self.i].tipo == 'tk_entero':
                    entero = self.listaTokens[self.i].lexema
                    expentero = ExpresionLiteral('entero',entero)
                    self.i += 1
                    if self.listaTokens[self.i].tipo == 'tk_parentesisc':
                        self.i += 1
                        if self.listaTokens[self.i].tipo == 'tk_puntoycoma':
                            self.i += 1
                            return InstruccionCursospostrrequisitos(expentero)

    #FUNCION DE ORDEN DE CURSOSPRERREQUISITOS
    def cursosprerrequisitos(self):
        if self.listaTokens[self.i].tipo == 'tk_cursosPrerrequisitos':
            self.i += 1
            if self.listaTokens[self.i].tipo == 'tk_parentesisa':
                self.i += 1
                if self.listaTokens[self.i].tipo == 'tk_entero':
                    entero = self.listaTokens[self.i].lexema
                    expentero = ExpresionLiteral('entero',entero)
                    self.i += 1
                    if self.listaTokens[self.i].tipo == 'tk_parentesisc':
                        self.i += 1
                        if self.listaTokens[self.i].tipo == 'tk_puntoycoma':
                            self.i += 1
                            return InstruccionCursosprerrequisitos(expentero)

    #FUNCION DE ORDEN DE CURSOPORNOMBRE
    def cursopornombre(self):
        if self.listaTokens[self.i].tipo == 'tk_cursoPorNombre':
            self.i += 1
            if self.listaTokens[self.i].tipo == 'tk_parentesisa':
                self.i += 1
                if self.listaTokens[self.i].tipo == 'tk_cadena':
                    cadena = self.listaTokens[self.i].lexema
                    excadena = ExpresionLiteral('cadena',cadena)
                    self.i += 1
                    if self.listaTokens[self.i].tipo == 'tk_parentesisc':
                        self.i += 1
                        if self.listaTokens[self.i].tipo == 'tk_puntoycoma':
                            self.i += 1
                            return InstruccionCursopornombre(excadena)

    #FUNCION DE ORDEN DE CURSOPORCODIGO
    def cursoporcodigo(self):
        if self.listaTokens[self.i].tipo == 'tk_cursoPorCodigo':
            self.i += 1
            if self.listaTokens[self.i].tipo == 'tk_parentesisa':
                self.i += 1
                if self.listaTokens[self.i].tipo == 'tk_entero':
                    entero = self.listaTokens[self.i].lexema
                    expentero = ExpresionLiteral('entero',entero)
                    self.i += 1
                    if self.listaTokens[self.i].tipo == 'tk_parentesisc':
                        self.i += 1
                        if self.listaTokens[self.i].tipo == 'tk_puntoycoma':
                            self.i += 1
                            return InstruccionCursoporcodigo(expentero)

    #FUNCION DE ORDEN DE CURSOSPORSEMESTRE
    def cursosporsemestre(self):
        if self.listaTokens[self.i].tipo == 'tk_cursosporsemestre':
            self.i += 1
            if self.listaTokens[self.i].tipo == 'tk_parentesisa':
                self.i += 1
                if self.listaTokens[self.i].tipo == 'tk_entero':
                    entero = self.listaTokens[self.i].lexema
                    expentero = ExpresionLiteral('entero',entero)
                    self.i += 1
                    if self.listaTokens[self.i].tipo == 'tk_parentesisc':
                        self.i += 1
                        if self.listaTokens[self.i].tipo == 'tk_puntoycoma':
                            self.i += 1
                            return InstruccionCursosporsemestre(expentero)

    #FUNCION DE ORDEN DE IMPRIMIRCONSALTO
    def imprimirconsalto(self):
        if self.listaTokens[self.i].tipo == 'tk_consolaln':
            self.i += 1
            if self.listaTokens[self.i].tipo == 'tk_parentesisa':
                self.i += 1
                if self.listaTokens[self.i].tipo == 'tk_cadena':
                    lex = self.listaTokens[self.i].lexema
                    explex = ExpresionLiteral('cadena',lex)
                    self.i += 1
                    if self.listaTokens[self.i].tipo == 'tk_parentesisc':
                        self.i += 1
                        if self.listaTokens[self.i].tipo == 'tk_puntoycoma':
                            self.i += 1
                            return InstruccionImprimirconsalto(explex)

    #FUNCION DE ORDEN DE IMPRIMIRSINSALTO
    def imprimirsinsalto(self):
        if self.listaTokens[self.i].tipo == 'tk_consola':
            self.i += 1
            if self.listaTokens[self.i].tipo == 'tk_parentesisa':
                self.i += 1
                if self.listaTokens[self.i].tipo == 'tk_cadena':
                    cadena = self.listaTokens[self.i].lexema
                    expcadena = ExpresionLiteral('cadena',cadena)
                    self.i += 1
                    if self.listaTokens[self.i].tipo == 'tk_parentesisc':
                        self.i += 1
                        if self.listaTokens[self.i].tipo == 'tk_puntoycoma':
                            self.i += 1
                            return InstruccionImprimirsinsalto(expcadena)

    #FUNCION DE ORDEN DE CREARCURSO
    def crearcurso(self):
        if self.listaTokens[self.i].tipo == 'tk_crearcurso':
            self.i += 1
            if self.listaTokens[self.i].tipo == 'tk_parentesisa':
                self.i += 1
                if self.listaTokens[self.i].tipo == 'tk_entero':
                    lexe1 = self.listaTokens[self.i].lexema
                    expe1 = ExpresionLiteral('entero',lexe1)
                    self.i += 1
                    if self.listaTokens[self.i].tipo == 'tk_coma':
                        self.i += 1
                        if self.listaTokens[self.i].tipo == 'tk_entero':
                            lexe2 = self.listaTokens[self.i].lexema
                            expe2 = ExpresionLiteral('entero',lexe2)
                            self.i += 1
                            if self.listaTokens[self.i].tipo == 'tk_coma':
                                self.i += 1
                                if self.listaTokens[self.i].tipo == 'tk_cadena':
                                    lexc = self.listaTokens[self.i].lexema
                                    expc = ExpresionLiteral('cadena',lexc)
                                    self.i += 1
                                    if self.listaTokens[self.i].tipo == 'tk_coma':
                                        self.i += 1
                                        if self.listaTokens[self.i].tipo == 'tk_corchetea':
                                            arr = self.arreglo()
                                            if self.listaTokens[self.i].tipo == 'tk_parentesisc':
                                                self.i += 1
                                                if self.listaTokens[self.i].tipo == 'tk_puntoycoma':
                                                    self.i += 1
                                                    return InstruccionCrearcurso(expe1,expe2,expc,arr)

    #FUNCION DE ORDEN DE NOMBRARRED
    def nombrarred(self):
        if self.listaTokens[self.i].tipo == 'tk_nombre_de_red':
            self.i += 1
            if self.listaTokens[self.i].tipo == 'tk_parentesisa':
                self.i += 1
                if self.listaTokens[self.i].tipo == 'tk_cadena':
                    cadena = self.listaTokens[self.i].lexema
                    expcadena = ExpresionLiteral('cadena',cadena)
                    self.i += 1
                    if self.listaTokens[self.i].tipo == 'tk_parentesisc':
                        self.i += 1
                        if self.listaTokens[self.i].tipo == 'tk_puntoycoma':
                            self.i += 1
                            return InstruccionNombrarred(expcadena)

    #FUNCION DE ORDEN DE INSTRUCCION
    def instruccion(self):
        if self.listaTokens[self.i].tipo == 'tk_nombre_de_red':
            ins = self.nombrarred()
            return InstruccionInstruccion(ins)
        elif self.listaTokens[self.i].tipo == 'tk_crearcurso':
            ins = self.crearcurso()
            return InstruccionInstruccion(ins)
        elif self.listaTokens[self.i].tipo == 'tk_consola':
            ins = self.imprimirsinsalto()
            return InstruccionInstruccion(ins)
        elif self.listaTokens[self.i].tipo == 'tk_consolaln':
            ins = self.imprimirconsalto()
            return InstruccionInstruccion(ins)
        elif self.listaTokens[self.i].tipo == 'tk_cursosporsemestre':
            ins = self.cursosporsemestre()
            return InstruccionInstruccion(ins)
        elif self.listaTokens[self.i].tipo == 'tk_cursoPorCodigo':
            ins = self.cursoporcodigo()
            return InstruccionInstruccion(ins)
        elif self.listaTokens[self.i].tipo == 'tk_cursoPorNombre':
            ins = self.cursopornombre()
            return InstruccionInstruccion(ins)
        elif self.listaTokens[self.i].tipo == 'tk_cursosPrerrequisitos':
            ins = self.cursosprerrequisitos()
            return InstruccionInstruccion(ins)
        elif self.listaTokens[self.i].tipo == 'tk_cursosPostrrequisitos':
            ins = self.cursospostrrequisitos()
            return InstruccionInstruccion(ins)
        elif self.listaTokens[self.i].tipo == 'tk_generarRed':
            ins = self.generarred()
            return InstruccionInstruccion(ins)
        else:
            pass

    #FUNCION DE ORDEN DE INSTRUCCIONES2
    def instrucciones2(self):
        if self.listaTokens[self.i].tipo == '<< EOF >>':
            print('Analisis Sintáctico realizado con éxito')
            return InstruccionInstrucciones2(None, None)
        else:
            ins = self.instruccion()
            ins2 = self.instrucciones2()
            return InstruccionInstrucciones2(ins,ins2)

    #FUNCION DE ORDEN DE INSTRUCCIONES
    def instrucciones(self):
        ins = self.instruccion()
        ins2 = self.instrucciones2()
        return InstruccionInstrucciones(ins,ins2)

    #FUNCION DE ORDEN DE INICIO
    def inicio(self):
        ins = self.instrucciones()
        return InstruccionInicio(ins)
    
    #FUNCION DE REALIZAR EL ANALISIS SINTACTICO
    def analizar(self, listaT, listaE):
        global raizarbol
        self.listaTokens = listaT
        self.listaErrores = listaE

        raizarbol = self.inicio()
        raizarbol.ejecutar({})
        raizarbol.getNodos()
