class ExpresionLiteral:
    def __init__(self, tipo, valor):
        self.tipo = tipo
        self.valor = valor

    def getValor(self, entorno):
        if self.tipo == 'cadena':
            return self.valor.replace("'", "")
        elif self.tipo == 'entero':
            return self.valor
        elif self.valor == 'arreglo':
            return self.valor.getValor(entorno)

class ExpresionArreglo:
    def __init__(self, arreglo):
        self.arreglo = arreglo

    def getValor(self, entorno):
        return self.arreglo.getValor(entorno)

class ExpresionListaEnteros:
    def __init__(self, entero, listaenteros2):
        self.entero = entero
        self.listaenteros2 = listaenteros2

    def getValor(self,entorno):
        if self.entero and self.listaenteros2:
            valor = self.entero.getValor(entorno)
            lista = self.listaenteros2.getValor(entorno)
            lista.insert(0, valor)
            return lista
        else:
            return []

class ExpresionListaEnteros2:
    def __init__(self, entero, listaenteros2):
        self.entero = entero
        self.listaenteros2 = listaenteros2

    def getValor(self, entorno):
        if self.entero and self.listaenteros2:
            valor = self.entero.getValor(entorno)
            lista = self.listaenteros2.getValor(entorno)
            lista.insert(0, valor)
            return lista
        else:
            return []