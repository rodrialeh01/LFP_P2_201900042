#---------------------------------LLAMANDO LIBRERIA GRAPHVIZ-----------------------------
from graphviz import Graph, Digraph
#---------------------------------LLAMANDO CLASES----------------------------------------
from Expresiones import *
from Curso import Curso

#-----------------------------------VARIABLES GLOBALES-----------------------------------
textconsola = ''
cursos = []
nombrered = ''

#CLASE DE ERROR
class InstruccionError():
    def __init__(self, linea):
        self.linea = linea

    def ejecutar(self, entorno):
        global textconsola
        mensaje = 'Se encontró un ERROR en la linea ' + str(self.linea) + '\n'
        textconsola += mensaje

    def getNodos(self):
        global dot
        id = str(indice())
        dot.node(id, 'ERROR')

        return id

#CLASE DE INICIO
class InstruccionInicio:
    def __init__(self, instrucciones):
        self.instrucciones = instrucciones

    def ejecutar(self, entorno):
        self.instrucciones.ejecutar(entorno)

    def getNodos(self):
        global dot
        id = str(indice())
        dot.node(id, 'INICIO')

        idinstrucciones= self.instrucciones.getNodos()

        dot.edge(id, idinstrucciones)
        return id

#CLASE DE INSTRUCCIONES
class InstruccionInstrucciones:
    def __init__(self, instruccion, instrucciones2):
        self.instruccion = instruccion
        self.instrucciones2 = instrucciones2

    def ejecutar(self, entorno):
        self.instruccion.ejecutar(entorno)
        self.instrucciones2.ejecutar(entorno)

    def getNodos(self):
        global dot
        id = str(indice())
        dot.node(id, 'INSTRUCCIONES')

        idinstruccion= self.instruccion.getNodos()
        idinstrucciones2= self.instrucciones2.getNodos()

        dot.edge(id, idinstruccion)
        dot.edge(id, idinstrucciones2)

        return id

#CLASE INSTRUCCION
class InstruccionInstruccion:
    def __init__(self, instruccion):
        self.instruccion = instruccion

    def ejecutar(self, entorno):
        self.instruccion.ejecutar(entorno)

    def getNodos(self):
        global dot
        id = str(indice())
        dot.node(id, 'INSTRUCCION')

        idinstruccion= self.instruccion.getNodos()

        dot.edge(id, idinstruccion)

        return id

#CLASE INSTRUCCIONES2
class InstruccionInstrucciones2:
    def __init__(self, instruccion, instrucciones2):
        self.instruccion = instruccion
        self.instrucciones2 = instrucciones2

    def ejecutar(self, entorno):
        if self.instruccion:
            self.instruccion.ejecutar(entorno)
        if self.instrucciones2:
            self.instrucciones2.ejecutar(entorno)

    def getNodos(self):
        global dot
        if self.instruccion and self.instrucciones2:
            id = str(indice())
            dot.node(id, 'INSTRUCCIONES2')

            idinstruccion= self.instruccion.getNodos()
            idinstrucciones2= self.instrucciones2.getNodos()

            dot.edge(id, idinstruccion)
            dot.edge(id, idinstrucciones2)

            return id
        else:
            id = str(indice())
            dot.node(id, "Epsilon")
            return id

#CLASE NOMBRAR RED PARA GUARDAR EL NOMBRE DE LA RED
class InstruccionNombrarred:
    def __init__(self, exp):
        self.exp = exp

    def ejecutar(self, entorno):
        global nombrered
        global textconsola
        valor = self.exp.getValor(entorno)
        nombrered = valor
        mensaje = '\nAgregó el nombre de red como: ' + str(valor) + '\n'
        #print(mensaje)
        textconsola += mensaje

    def getNodos(self):
        global dot
        id = str(indice())
        dot.node(id, 'NOMBRARRED')

        nr = str(indice())
        dot.node(nr, 'nombre_de_red')

        para = str(indice())
        dot.node(para, '(')

        idexp = self.exp.getNodos()

        parc = str(indice())
        dot.node(parc, ')')

        pyc = str(indice())
        dot.node(pyc, ';')

        dot.edge(id, nr)
        dot.edge(id, para)
        dot.edge(id, idexp)
        dot.edge(id, parc)
        dot.edge(id,pyc)

        return id

#CLASE CREARCURSO PARA CREAR EL CURSO Y GUARDAR SUS OBJETOS
class InstruccionCrearcurso:
    def __init__(self, entero1, entero2, cadena, arreglo):
        self.entero1 = entero1
        self.entero2 = entero2
        self.cadena = cadena
        self.arreglo = arreglo

    def ejecutar(self, entorno):
        global cursos
        global textconsola
        valor1 = self.entero1.getValor(entorno)
        valor2 = self.entero2.getValor(entorno)
        valor3 = self.cadena.getValor(entorno)
        arreglo = self.arreglo.getValor(entorno)
        cursos.append(Curso(valor1,valor2,valor3,arreglo))
        mensaje = 'Se agregó el curso ' + str(valor3) + '\n'
        #print(mensaje)
        textconsola += mensaje

    def getNodos(self):
        global dot
        id = str(indice())
        dot.node(id, 'CREARCURSO')

        cc = str(indice())
        dot.node(cc, 'crearcurso')

        para = str(indice())
        dot.node(para, '(')

        e1 = self.entero1.getNodos()
        c1 = str(indice())
        dot.node(c1, ',')
        e2 = self.entero2.getNodos()
        c2 = str(indice())
        dot.node(c2, ',')
        c = self.cadena.getNodos()
        c3 = str(indice())
        dot.node(c3, ',')
        a = self.arreglo.getNodos()

        parc = str(indice())
        dot.node(parc, ')')

        pyc = str(indice())
        dot.node(pyc, ';')

        dot.edge(id,cc)
        dot.edge(id,para)
        dot.edge(id,e1)
        dot.edge(id,c1)
        dot.edge(id,e2)
        dot.edge(id,c2)
        dot.edge(id,c)
        dot.edge(id,c3)
        dot.edge(id,a)
        dot.edge(id,parc)
        dot.edge(id, pyc)

        return id

#CLASE IMPRIMIRSINSALTO PARA MOSTRAR EL TEXTO SIN SALTO DE LINEA
class InstruccionImprimirsinsalto:
    def __init__(self, exp):
        self.exp = exp

    def ejecutar(self, entorno):
        global textconsola
        valor = self.exp.getValor(entorno)
        #print(valor, end=" ")
        textconsola+=valor

    def getNodos(self):
        global dot
        id = str(indice())
        dot.node(id, 'IMPRIMIRSINSALTO')

        cons = str(indice())
        dot.node(cons, 'consola')

        para = str(indice())
        dot.node(para, '(')

        idexp = self.exp.getNodos()

        parc = str(indice())
        dot.node(parc, ')')

        pyc = str(indice())
        dot.node(pyc, ';')

        dot.edge(id, cons)
        dot.edge(id, para)
        dot.edge(id, idexp)
        dot.edge(id, parc)
        dot.edge(id,pyc)

        return id

#CLASE IMPRIMIRCONSALTO PARA MOSTRAR EL TEXTO Y LUEGO EJECUTAR EL SALTO DE LINEA
class InstruccionImprimirconsalto:
    def __init__(self, exp):
        self.exp = exp

    def ejecutar(self, entorno):
        global textconsola
        valor = self.exp.getValor(entorno)
        valorl = valor + '\n'
        #print(valor)
        textconsola += valorl

    def getNodos(self):
        global dot
        id = str(indice())
        dot.node(id, 'IMPRIMIRCONSALTO')

        cons = str(indice())
        dot.node(cons, 'consolaln')

        para = str(indice())
        dot.node(para, '(')

        idexp = self.exp.getNodos()

        parc = str(indice())
        dot.node(parc, ')')

        pyc = str(indice())
        dot.node(pyc, ';')

        dot.edge(id, cons)
        dot.edge(id, para)
        dot.edge(id, idexp)
        dot.edge(id, parc)
        dot.edge(id,pyc)

        return id

#CLASE CURSOSPORSEMESTRE DONDE MUESTRA TODOS LOS CURSOS DEL SEMESTRE SELECCIONADO
class InstruccionCursosporsemestre:
    def __init__(self, cod):
        self.cod = cod

    def ejecutar(self, entorno):
        global cursos
        global textconsola
        contenido = ''
        valor = self.cod.getValor(entorno)
        contenido += '\n************ SEMESTRE: ' + str(valor) + ' ************\n'
        for c in cursos:
            if int(valor) == int(c.getSemestre()):
                contenido += 'Código: ' + str(c.getCodigo()) + '\nCurso: ' + str(c.getNombre()) + '\nRequisitos:' + str(c.getPrerrequisitos()) + '\n\n'
        contenido += '************************************\n'
        #print(contenido)
        textconsola += contenido

    def getNodos(self):
        global dot
        id = str(indice())
        dot.node(id, 'CURSOSPORSEMESTRE')

        cons = str(indice())
        dot.node(cons, 'cursosporsemestre')

        para = str(indice())
        dot.node(para, '(')

        idcod = self.cod.getNodos()

        parc = str(indice())
        dot.node(parc, ')')

        pyc = str(indice())
        dot.node(pyc, ';')

        dot.edge(id, cons)
        dot.edge(id, para)
        dot.edge(id, idcod)
        dot.edge(id, parc)
        dot.edge(id,pyc)

        return id

#CLASE CURSOPORCODIGO PARA MOSTRAR EL CURSO CON EL CODIGO INGRESADO EN LA CONSOLA DE TEXTO
class InstruccionCursoporcodigo:
    def __init__(self, codigo):
        self.codigo = codigo

    def ejecutar(self, entorno):
        global cursos
        global textconsola
        contenido = ''
        valor = self.codigo.getValor(entorno)
        contenido += '\n************************************\n'
        for c in cursos:
            if int(valor) == int(c.getCodigo()):
                contenido += 'Curso: ' + str(c.getNombre()) + '\nSemestre: ' + str(c.getSemestre()) + '\nCódigo: ' + str(c.getCodigo()) + '\nPrerrequisitos: ' + str(c.getPrerrequisitos())
        contenido += '\n************************************\n'
        #print(contenido)
        textconsola += contenido

    def getNodos(self):
        global dot
        id = str(indice())
        dot.node(id, 'CURSOPORCODIGO')

        cons = str(indice())
        dot.node(cons, 'cursoPorCodigo')

        para = str(indice())
        dot.node(para, '(')

        idcodigo = self.codigo.getNodos()

        parc = str(indice())
        dot.node(parc, ')')

        pyc = str(indice())
        dot.node(pyc, ';')

        dot.edge(id, cons)
        dot.edge(id, para)
        dot.edge(id, idcodigo)
        dot.edge(id, parc)
        dot.edge(id,pyc)

        return id

#CLASE CURSOPORNOMBRE DONDE SE MUESTRA EL CURSO POR MEDIO DEL NOMBRE INGRESADO
class InstruccionCursopornombre:
    def __init__(self, nombre):
        self.nombre = nombre

    def ejecutar(self, entorno):
        global cursos
        global textconsola
        contenido = ''
        valor = self.nombre.getValor(entorno)
        contenido += '\n************************************\n'
        for c in cursos:
            if str(valor) == str(c.getNombre()):
                contenido += 'Curso: ' + str(c.getNombre()) + '\nSemestre: ' + str(c.getSemestre()) + '\nCódigo: ' + str(c.getCodigo()) + '\nPrerrequisitos: ' + str(c.getPrerrequisitos())
        contenido += '\n************************************\n'
        #print(contenido)
        textconsola += contenido

    def getNodos(self):
        global dot
        id = str(indice())
        dot.node(id, 'CURSOPORNOMBRE')

        cons = str(indice())
        dot.node(cons, 'cursoPorNombre')

        para = str(indice())
        dot.node(para, '(')

        idnombre = self.nombre.getNodos()

        parc = str(indice())
        dot.node(parc, ')')

        pyc = str(indice())
        dot.node(pyc, ';')

        dot.edge(id, cons)
        dot.edge(id, para)
        dot.edge(id, idnombre)
        dot.edge(id, parc)
        dot.edge(id,pyc)

        return id

#CURSO CURSOSPRERREQUISITOS DONDE SE MUESTRAN TODOS LOS PRERREQUISITOS DEL CODIGO DEL CURSO INGRESADO
class InstruccionCursosprerrequisitos:
    def __init__(self, codigo):
        self.codigo = codigo

    def ejecutar(self, entorno):
        global cursos
        global textconsola
        contenido = ''
        valor = self.codigo.getValor(entorno)
        contenido += '\n************************************\n'
        for c in cursos:
            if int(valor) == int(c.getCodigo()):
                contenido += 'Curso: ' + str(c.getNombre()) + '\nPrerrequisitos: ' + self.obtenernombres(c.getPrerrequisitos())
        contenido += '\n************************************\n'
        #print(contenido)
        textconsola += contenido

    def obtenernombres(self,arreglop):
        content = ''
        global cursos
        for c in cursos:
            for p in arreglop:
                if int(p) == int(c.getCodigo()):
                    content += c.getNombre() + '\n                '
        if content == '':
            content = 'Ninguno'
        return content

    def getNodos(self):
        global dot
        id = str(indice())
        dot.node(id, 'CURSOSPRERREQUISITOS')

        cons = str(indice())
        dot.node(cons, 'cursosPrerrequisitos')

        para = str(indice())
        dot.node(para, '(')

        idcodigo = self.codigo.getNodos()

        parc = str(indice())
        dot.node(parc, ')')

        pyc = str(indice())
        dot.node(pyc, ';')

        dot.edge(id, cons)
        dot.edge(id, para)
        dot.edge(id, idcodigo)
        dot.edge(id, parc)
        dot.edge(id,pyc)

        return id

#CLASE CURSOSPOSTRREQUISITOS PARA MOSTRAR TODOS LOS CURSOS POSTRREQUISITOS POR MEDIO DEL CURSO INGRESADO
class InstruccionCursospostrrequisitos:
    def __init__(self, codigo):
        self.codigo = codigo

    def ejecutar(self, entorno):
        global cursos
        global textconsola
        contenido = ''
        valor = self.codigo.getValor(entorno)
        contenido += '\n************************************\n'
        for c in cursos:
            if int(valor) == int(c.getCodigo()):
                contenido += 'Curso: ' + str(c.getNombre()) + '\nPostrrequisitos: ' + self.obtenerpost(valor)
        contenido += '\n************************************\n'
        #print(contenido)
        textconsola += contenido

    def obtenerpost(self,codigo):
        texto = ''
        global cursos
        for c in cursos:
            for p in c.getPrerrequisitos():
                if int(codigo) == int(p):
                    texto += str(c.getNombre()) + '\n                 '
        if texto == '':
            texto = 'Ninguno'
        return texto

    def getNodos(self):
        global dot
        id = str(indice())
        dot.node(id, 'CURSOSPOSTRREQUISITOS')

        cons = str(indice())
        dot.node(cons, 'cursosPostrrequisitos')

        para = str(indice())
        dot.node(para, '(')

        idcodigo = self.codigo.getNodos()

        parc = str(indice())
        dot.node(parc, ')')

        pyc = str(indice())
        dot.node(pyc, ';')

        dot.edge(id, cons)
        dot.edge(id, para)
        dot.edge(id, idcodigo)
        dot.edge(id, parc)
        dot.edge(id,pyc)

        return id

#CLASE GENERARRED PARA GENERAR UN ARBOL DE LA RED CURRICULAR GUARDADO CON EL NOMBRE INGRESADO
class InstruccionGenerarred:
    def __init__(self, nombre):
        self.nombre = nombre

    def ejecutar(self, entorno):
        global textconsola
        global cursos
        global nombrered
        valor = self.nombre.getValor(entorno)
        red = Digraph(valor, 'png')
        red.format = 'png'
        red.attr(splines='false')
        red.node_attr.update(shape='record')
        red.node_attr.update(fillcolor='orangered')
        red.node_attr.update(fontcolor='white')
        red.node_attr.update(style='filled')
        titulo = '<<B>'+str(nombrered)+'</B>>'
        red.attr(label= str(titulo))
        for c in cursos:
            red.node(str(c.getCodigo()),'Cod. '+str(c.getCodigo()) + '|' +str(c.getNombre()))
            for p in c.getPrerrequisitos():
                red.edge(str(p),str(c.getCodigo()))                              

        red.view()
        #print('Red de ' + str(nombrered) + ' generada con éxito')

        textconsola += '\nRed de ' + str(nombrered) + ' generada con éxito'

    def getNodos(self):
        global dot
        id = str(indice())
        dot.node(id, 'GENERARRED')

        cons = str(indice())
        dot.node(cons, 'generarRed')

        para = str(indice())
        dot.node(para, '(')

        idnombre = self.nombre.getNodos()

        parc = str(indice())
        dot.node(parc, ')')

        pyc = str(indice())
        dot.node(pyc, ';')

        dot.edge(id, cons)
        dot.edge(id, para)
        dot.edge(id, idnombre)
        dot.edge(id, parc)
        dot.edge(id,pyc)

        return id
#FUNCION PARA PODER VER Y GENERAR EL ARBOL DE DERIVACION
def verarbol():
    global dot
    dot.view()

#FUNCION PARA RETORNAR LAS CADENAS GENERADAS DE LAS INSTRUCCIONES
def texto():
    global textconsola
    return textconsola
