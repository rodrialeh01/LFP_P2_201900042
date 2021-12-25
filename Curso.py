class Curso:
    def __init__(self, semestre, codigo, nombre, prerrequisitos):
        self.semestre = semestre
        self.codigo = codigo
        self.nombre = nombre
        self.prerrequisitos = prerrequisitos

    def getSemestre(self):
        return self.semestre

    def getCodigo(self):
        return self.codigo

    def getNombre(self):
        return self.nombre

    def getPrerrequisitos(self):
        return self.prerrequisitos