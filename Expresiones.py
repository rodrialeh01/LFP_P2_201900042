from graphviz import Graph

dot= Graph('Arbol de Derivacion','png')
dot.format= 'png'
dot.attr(splines='false')
dot.node_attr.update(shape='circle')
dot.node_attr.update(color='blue')

i = 0
def inc():
    global i
    i += 1
    return i

def getNumNodo():
    global i
    return i

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

    def getNodos(self):
        global dot
        id = str(inc())
        dot.node(id, "Expresion")

        idlit = str(inc())
        dot.node(idlit, "Literal")

        idlex = str(inc())
        dot.node(idlex, str(self.valor))

        dot.edge(id,idlit)
        dot.edge(idlit, idlex)

        return id

class ExpresionArreglo:
    def __init__(self, arreglo):
        self.arreglo = arreglo

    def getValor(self, entorno):
        return self.arreglo.getValor(entorno)

    def getNodos(self):
        global dot

        id = str(inc())
        dot.node(id,"Arreglo")

        idca = str(inc())
        dot.node(idca, "[")

        idlistacadenas = self.arreglo.getNodos()

        idcc = str(inc())
        dot.node(idcc, "]")

        dot.edge(id, idca)
        dot.edge(id, idlistacadenas)
        dot.edge(id, idcc)

        return id

class ExpresionListaEnteros:
    def __init__(self, entero, listaenteros2):
        self.entero = entero
        self.listaenteros2 = listaenteros2

    def getValor(self,entorno):
        if self.entero and self.listaenteros2:
            valor = self.entero.getValor(entorno)
            lista = self.listaenteros2.getValor(entorno)
            lista.append(valor)
            return lista
        else:
            return []

    def getNodos(self):
        global dot
        if self.entero and self.listaenteros2:
            id = str(inc())
            dot.node(id, 'ListaEnteros')
            
            idlit = str(inc())
            dot.node(idlit, 'Literal')

            idlex = str(inc())
            dot.node(idlex, self.entero.getValor(None))

            idlistaenteros2 = self.listaenteros2.getNodos()

            dot.edge(id, idlit)
            dot.edge(idlit, idlex)
            dot.edge(id,idlistaenteros2)

            return id
        else:
            id = str(inc())
            dot.node(id, "Epsilon")
            return id

class ExpresionListaEnteros2:
    def __init__(self, entero, listaenteros2):
        self.entero = entero
        self.listaenteros2 = listaenteros2

    def getValor(self, entorno):
        if self.entero and self.listaenteros2:
            valor = self.entero.getValor(entorno)
            lista = self.listaenteros2.getValor(entorno)
            lista.append(valor)
            return lista
        else:
            return []

    def getNodos(self):
        global dot
        if self.entero and self.listaenteros2:
            id = str(inc())
            dot.node(id,'ListaEnteros2')

            idcoma = str(inc())
            dot.node(idcoma, ',')

            idlit = str(inc())
            dot.node(idlit, 'Literal')

            idlex = str(inc())
            dot.node(idlex, self.entero.getValor(None))

            idlistaenteros2 = self.listaenteros2.getNodos()

            dot.edge(id, idcoma)
            dot.edge(id, idlit)
            dot.edge(idlit, idlex)
            dot.edge(id, idlistaenteros2)
            
            return id
        else:
            id = str(inc())
            dot.node(id, "Epsilon")
            return id