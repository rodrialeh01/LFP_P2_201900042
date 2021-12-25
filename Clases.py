#CLASE TOKEN
class Token:
    def __init__(self,lexema,tipo,linea,columna):
        self.lexema = lexema
        self.tipo = tipo
        self.linea = linea
        self.columna = columna

#CLASE ERROR
class Error:
    def __init__(self,caracter, descripcion, tipo, linea, columna):
        self.caracter = caracter
        self.descripcion = descripcion
        self.tipo = tipo
        self.linea = linea
        self.columna = columna
