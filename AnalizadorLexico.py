#--------------------------------IMPORTANDO CLASES-----------------------------
from Clases import Token,Error

class AnalizadorLexico:
    def __init__(self):
        self.listaTokens = []
        self.listaErrores = []

    def analisis(self,contenido):
        self.listaTokens = []
        self.listaErrores = []

        contenido += '$'
        indice = 0
        linea = 1
        columna = 1
        buffer = ""
        estado = 'A'

        while indice < len(contenido):
            caracter = contenido[indice]
            if estado == 'A':
                if caracter == '(':
                    buffer = caracter
                    columna += 1
                    self.listaTokens.append(Token(buffer, 'tk_parentesisa',linea,columna))
                    buffer = ''
                    estado = 'A'
                elif caracter == ')':
                    buffer = caracter
                    columna += 1
                    self.listaTokens.append(Token(buffer, 'tk_parentesisc',linea,columna))
                    buffer = ''
                    estado = 'A'
                elif caracter == ';':
                    buffer = caracter
                    columna += 1
                    self.listaTokens.append(Token(buffer, 'tk_puntoycoma',linea,columna))
                    buffer = ''
                    estado = 'A'
                elif caracter == ",":
                    buffer = caracter
                    columna += 1
                    self.listaTokens.append(Token(buffer, 'tk_coma',linea,columna))
                    buffer = ''
                    estado = 'A'
                elif caracter == '[':
                    buffer = caracter
                    columna += 1
                    self.listaTokens.append(Token(buffer, 'tk_corchetea',linea,columna))
                    buffer = ''
                    estado = 'A'
                elif caracter == ']':
                    buffer = caracter
                    columna += 1
                    self.listaTokens.append(Token(buffer, 'tk_corchetec',linea,columna))
                    buffer = ''
                    estado = 'A'
                elif caracter.isalpha() and (not caracter.isdigit()):
                    buffer = caracter
                    columna += 1
                    estado = 'B'
                elif caracter == ' ':
                    columna += 1
                elif caracter == '\n':
                    linea += 1
                    columna = 1
                elif caracter == '\t':
                    columna +=1
                elif caracter == "'":
                    buffer = caracter
                    columna +=1
                    estado = 'C'
                elif caracter.isdigit():
                    buffer = caracter
                    columna += 1
                    estado = 'D'
                elif caracter == '$':
                    buffer = caracter
                    columna += 1
                    self.listaTokens.append(Token(buffer, '<< EOF >>' , linea, columna))
                    buffer = ''
                    estado = 'A'
                else:
                    self.listaErrores.append(Error(caracter,caracter + " no reconocido como token.", 'Léxico', linea, columna)) 
                    buffer = ''
                    columna += 1
            elif estado == 'B':
                if caracter.isalpha() and (not caracter.isdigit()) or caracter == '_':
                    buffer += caracter
                    columna += 1
                    estado = 'B'
                else:
                    if buffer == 'nombre_de_red':
                        self.listaTokens.append(Token(buffer, 'tk_nombre_de_red', linea,columna))
                    elif buffer == 'crearcurso':
                        self.listaTokens.append(Token(buffer, 'tk_crearcurso', linea,columna))
                    elif buffer == 'consola':
                        self.listaTokens.append(Token(buffer, 'tk_consola', linea,columna))
                    elif buffer == 'consolaln':
                        self.listaTokens.append(Token(buffer, 'tk_consolaln', linea,columna))
                    elif buffer == 'cursosporsemestre':
                        self.listaTokens.append(Token(buffer, 'tk_cursosporsemestre', linea,columna))
                    elif buffer == 'cursoPorCodigo':
                        self.listaTokens.append(Token(buffer, 'tk_cursoPorCodigo', linea,columna))
                    elif buffer == 'cursoPorNombre':
                        self.listaTokens.append(Token(buffer, 'tk_cursoPorNombre', linea,columna))
                    elif buffer == 'cursosPrerrequisitos':
                        self.listaTokens.append(Token(buffer, 'tk_cursosPrerrequisitos', linea,columna))
                    elif buffer == 'cursosPostrrequisitos':
                        self.listaTokens.append(Token(buffer, 'tk_cursosPostrrequisitos', linea,columna))
                    elif buffer == 'generarRed':
                        self.listaTokens.append(Token(buffer, 'tk_generarRed', linea,columna))
                    else:
                        self.listaErrores.append(Error(buffer,buffer + " no esta reconocido como token.", 'Léxico',linea,columna))
                    buffer = ''
                    estado = 'A'
                    indice -= 1
            elif estado == 'C':
                if caracter == "'":
                    buffer += caracter
                    columna +=1
                    self.listaTokens.append(Token(buffer, 'tk_cadena',linea,columna))
                    buffer = ''
                    estado = 'A'
                elif caracter == '\n':
                    columna = 1
                    linea += 1
                elif caracter == '"':
                    buffer += caracter
                    columna +=1
                    self.listaErrores.append(Error(buffer,"La forma de escritura de la cadena es incorrecta.", ' Léxico',linea,columna))
                    buffer = ''
                    estado = 'A'
                else:
                    buffer += caracter
                    columna += 1
                    estado = 'C'
            elif estado == 'D':
                if caracter.isdigit():
                    buffer += caracter
                    columna +=1
                    estado = 'D'
                else:
                    self.listaTokens.append(Token(buffer,'tk_entero', linea,columna))
                    buffer = ''
                    indice -=1
                    estado = 'A'
            indice += 1

    def imprimir(self):
        print('Tokens')
        for token in self.listaTokens:
            token.getInfo()
        print()
        print('Errores')
        for token in self.listaErrores:
            token.getInfo()
        print()
        print("Cantidad de tokens: " + str(len(self.listaTokens)))
        print("Cantidad de errores: " + str(len(self.listaErrores)))