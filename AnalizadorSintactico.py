from Clases import Token,Error

class AnalizadorSintactico:
    def __init__(self):
        self.listaTokens = []
        self.listaErrores = []
        self.i = 0

    def listaenteros2(self):
        if self.listaTokens[self.i].tipo == 'tk_coma':
            self.i = self.i +1
            if self.listaTokens[self.i].tipo == 'tk_entero':
                self.i = self.i +1
                self.listaenteros2()
        elif self.listaTokens[self.i].tipo == 'corchetec':
            return

    def listaenteros(self):
        if self.listaTokens[self.i].tipo == 'tk_entero':
            self.i = self.i +1
            self.listaenteros2()
        elif self.listaTokens[self.i].tipo == 'tk_corchetec':
            return

    def arreglo(self):
        if self.listaTokens[self.i].tipo == 'tk_corchetea':
            self.i = self.i +1
            self.listaenteros()
            if self.listaTokens[self.i].tipo == 'tk_corchetec':
                self.i +=1

    def generarred(self):
        if self.listaTokens[self.i].tipo == 'tk_generarRed':
            self.i = self.i +1
            if self.listaTokens[self.i].tipo == 'tk_parentesisa':
                self.i = self.i +1
                if self.listaTokens[self.i].tipo == 'tk_cadena':
                    self.i = self.i +1
                    if self.listaTokens[self.i].tipo == 'tk_parentesisc':
                        self.i = self.i +1
                        if self.listaTokens[self.i].tipo == 'tk_puntoycoma':
                            self.i = self.i +1

    def cursospostrrequisitos(self):
        if self.listaTokens[self.i].tipo == 'tk_cursosPostrrequisitos':
            self.i = self.i +1
            if self.listaTokens[self.i].tipo == 'tk_parentesisa':
                self.i = self.i +1
                if self.listaTokens[self.i].tipo == 'tk_entero':
                    self.i = self.i +1
                    if self.listaTokens[self.i].tipo == 'tk_parentesisc':
                        self.i = self.i +1
                        if self.listaTokens[self.i].tipo == 'tk_puntoycoma':
                            self.i = self.i +1

    def cursosprerrequisitos(self):
        if self.listaTokens[self.i].tipo == 'tk_cursosPrerrequisitos':
            self.i = self.i +1
            if self.listaTokens[self.i].tipo == 'tk_parentesisa':
                self.i = self.i +1
                if self.listaTokens[self.i].tipo == 'tk_entero':
                    self.i = self.i +1
                    if self.listaTokens[self.i].tipo == 'tk_parentesisc':
                        self.i = self.i +1
                        if self.listaTokens[self.i].tipo == 'tk_puntoycoma':
                            self.i = self.i +1

    def cursopornombre(self):
        if self.listaTokens[self.i].tipo == 'tk_cursoPorNombre':
            self.i = self.i +1
            if self.listaTokens[self.i].tipo == 'tk_parentesisa':
                self.i = self.i +1
                if self.listaTokens[self.i].tipo == 'tk_cadena':
                    self.i = self.i +1
                    if self.listaTokens[self.i].tipo == 'tk_parentesisc':
                        self.i = self.i +1
                        if self.listaTokens[self.i].tipo == 'tk_puntoycoma':
                            self.i = self.i +1

    def cursoporcodigo(self):
        if self.listaTokens[self.i].tipo == 'tk_cursoPorCodigo':
            self.i = self.i +1
            if self.listaTokens[self.i].tipo == 'tk_parentesisa':
                self.i = self.i +1
                if self.listaTokens[self.i].tipo == 'tk_entero':
                    self.i = self.i +1
                    if self.listaTokens[self.i].tipo == 'tk_parentesisc':
                        self.i = self.i +1
                        if self.listaTokens[self.i].tipo == 'tk_puntoycoma':
                            self.i = self.i +1

    def cursosporsemestre(self):
        if self.listaTokens[self.i].tipo == 'tk_cursosporsemestre':
            self.i = self.i +1
            if self.listaTokens[self.i].tipo == 'tk_parentesisa':
                self.i = self.i +1
                if self.listaTokens[self.i].tipo == 'tk_entero':
                    self.i = self.i +1
                    if self.listaTokens[self.i].tipo == 'tk_parentesisc':
                        self.i = self.i +1
                        if self.listaTokens[self.i].tipo == 'tk_puntoycoma':
                            self.i = self.i +1

    def imprimirconsalto(self):
        if self.listaTokens[self.i].tipo == 'tk_consolaln':
            self.i = self.i +1
            if self.listaTokens[self.i].tipo == 'tk_parentesisa':
                self.i = self.i +1
                if self.listaTokens[self.i].tipo == 'tk_cadena':
                    self.i = self.i +1
                    if self.listaTokens[self.i].tipo == 'tk_parentesisc':
                        self.i = self.i +1
                        if self.listaTokens[self.i].tipo == 'tk_puntoycoma':
                            self.i = self.i +1

    def imprimirsinsalto(self):
        if self.listaTokens[self.i].tipo == 'tk_consola':
            self.i = self.i +1
            if self.listaTokens[self.i].tipo == 'tk_parentesisa':
                self.i = self.i +1
                if self.listaTokens[self.i].tipo == 'tk_cadena':
                    self.i = self.i +1
                    if self.listaTokens[self.i].tipo == 'tk_parentesisc':
                        self.i = self.i +1
                        if self.listaTokens[self.i].tipo == 'tk_puntoycoma':
                            self.i = self.i +1

    def crearcurso(self):
        if self.listaTokens[self.i].tipo == 'tk_crearcurso':
            self.i = self.i +1
            if self.listaTokens[self.i].tipo == 'tk_parentesisa':
                self.i = self.i +1
                if self.listaTokens[self.i].tipo == 'tk_entero':
                    self.i = self.i +1
                    if self.listaTokens[self.i].tipo == 'tk_coma':
                        self.i = self.i +1
                        if self.listaTokens[self.i].tipo == 'tk_entero':
                            self.i = self.i +1
                            if self.listaTokens[self.i].tipo == 'tk_coma':
                                self.i = self.i +1
                                if self.listaTokens[self.i].tipo == 'tk_cadena':
                                    self.i = self.i +1
                                    if self.listaTokens[self.i].tipo == 'tk_coma':
                                        self.i = self.i +1
                                        if self.listaTokens[self.i].tipo == 'tk_corchetea':
                                            self.arreglo()
                                            if self.listaTokens[self.i].tipo == 'tk_parentesisc':
                                                self.i = self.i +1
                                                if self.listaTokens[self.i].tipo == 'tk_puntoycoma':
                                                    self.i = self.i +1



    def nombrarred(self):
        if self.listaTokens[self.i].tipo == 'tk_nombre_de_red':
            self.i = self.i +1
            if self.listaTokens[self.i].tipo == 'tk_parentesisa':
                self.i = self.i +1
                if self.listaTokens[self.i].tipo == 'tk_cadena':
                    self.i = self.i +1
                    if self.listaTokens[self.i].tipo == 'tk_parentesisc':
                        self.i = self.i +1
                        if self.listaTokens[self.i].tipo == 'tk_puntoycoma':
                            self.i = self.i +1

    def instruccion(self):
        if self.listaTokens[self.i].tipo == 'tk_nombre_de_red':
            self.nombrarred()
        elif self.listaTokens[self.i].tipo == 'tk_crearcurso':
            self.crearcurso()
        elif self.listaTokens[self.i].tipo == 'tk_consola':
            self.imprimirsinsalto()
        elif self.listaTokens[self.i].tipo == 'tk_consolaln':
            self.imprimirconsalto()
        elif self.listaTokens[self.i].tipo == 'tk_cursosporsemestre':
            self.cursosporsemestre()
        elif self.listaTokens[self.i].tipo == 'tk_cursoPorCodigo':
            self.cursoporcodigo()
        elif self.listaTokens[self.i].tipo == 'tk_cursoPorNombre':
            self.cursopornombre()
        elif self.listaTokens[self.i].tipo == 'tk_cursosPrerrequisitos':
            self.cursosprerrequisitos()
        elif self.listaTokens[self.i].tipo == 'tk_cursosPostrrequisitos':
            self.cursospostrrequisitos()
        elif self.listaTokens[self.i].tipo == 'tk_generarRed':
            self.generarred()
        else:
            pass

    def instrucciones2(self):
        if self.listaTokens[self.i].tipo == '<< EOF >>':
            print('Analisis Sintáctico realizado con éxito')
        else:
            self.instruccion()
            self.instrucciones2()

    def instrucciones(self):
        self.instruccion()
        self.instrucciones2()

    def inicio(self):
        self.instrucciones()

    def analizar(self, listaT, listaE):
        self.listaTokens = listaT
        self.listaErrores = listaE
        self.inicio()
