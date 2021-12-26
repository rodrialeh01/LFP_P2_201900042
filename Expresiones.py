#----------------------------------IMPORTANDO LIBRERIA GRAPHVIZ----------------------------
from graphviz import Graph

#---------------------------------CREANDO EL ARBOL DE DERIVACION---------------------------
dot= Graph('Arbol de Derivacion','png')
dot.format= 'png'
dot.attr(splines='false')
dot.node_attr.update(shape='circle')
dot.node_attr.update(fillcolor='darkblue')
dot.node_attr.update(fontcolor='white')
dot.node_attr.update(style='filled')
dot.node_attr.update(color='blue')
#FUNCION PARA CONTADOR
i = 0
def indice():
    global i
    i += 1
    return i

def getNumNodo():
    global i
    return i

#CLASE PARA LAS EXPRESIONES LITERALES COMO LA CADENA, ENTERO Y ARREGLO
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
        id = str(indice())
        dot.node(id, "Expresion")

        idlit = str(indice())
        dot.node(idlit, "Literal")

        idlex = str(indice())
        dot.node(idlex, str(self.valor))

        dot.edge(id,idlit)
        dot.edge(idlit, idlex)

        return id

#CLASE DE EXPRESION ARREGLO QUE ES UTIL PARA RECONOCER LOS ARREGLOS
class ExpresionArreglo:
    def __init__(self, arreglo):
        self.arreglo = arreglo

    def getValor(self, entorno):
        return self.arreglo.getValor(entorno)

    def getNodos(self):
        global dot

        id = str(indice())
        dot.node(id,"Arreglo")

        idca = str(indice())
        dot.node(idca, "[")

        idlistacadenas = self.arreglo.getNodos()

        idcc = str(indice())
        dot.node(idcc, "]")

        dot.edge(id, idca)
        dot.edge(id, idlistacadenas)
        dot.edge(id, idcc)

        return id

#CLASE DE EXPRESION DE LA LISTA DE ENTEROS CUANDO HAY 0 O 1
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
            id = str(indice())
            dot.node(id, 'ListaEnteros')
            
            idlit = str(indice())
            dot.node(idlit, 'Literal')

            idlex = str(indice())
            dot.node(idlex, self.entero.getValor(None))

            idlistaenteros2 = self.listaenteros2.getNodos()

            dot.edge(id, idlit)
            dot.edge(idlit, idlex)
            dot.edge(id,idlistaenteros2)

            return id
        else:
            id = str(indice())
            dot.node(id, "Epsilon")
            return id

#CLASE DE LA EXPRESION DE LA LISTA DE ENTEROS 2 DE MINIMO 1 ENTERO
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
            id = str(indice())
            dot.node(id,'ListaEnteros2')

            idcoma = str(indice())
            dot.node(idcoma, ',')

            idlit = str(indice())
            dot.node(idlit, 'Literal')

            idlex = str(indice())
            dot.node(idlex, self.entero.getValor(None))

            idlistaenteros2 = self.listaenteros2.getNodos()

            dot.edge(id, idcoma)
            dot.edge(id, idlit)
            dot.edge(idlit, idlex)
            dot.edge(id, idlistaenteros2)
            
            return id
        else:
            id = str(indice())
            dot.node(id, "Epsilon")
            return id