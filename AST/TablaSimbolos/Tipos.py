from enum import Enum


class tipo(Enum):
    ENTERO = 0,
    DECIMAL = 1,
    BOOLEANO = 2,
    CARACTER = 3,
    STRING = 4,
    DIRSTRING = 5,
    UNDEFINED = 6,
    RETURN = 7,
    BREAK = 8,
    CONTINUE = 9,
    ARRAY = 10,
    OBJETO = 11,
    USIZE = 12,
    VECTOR = 13,
    STRUCT = 14,
    ERROR = 15

class RetornoType():
    def __init__(self,  valor = None , tipo = tipo.UNDEFINED , final = tipo.UNDEFINED):
        self.tipo = tipo
        self.valor = valor
        self.final = final

        self.codigo = ""
        self.etiqueta = ""
        self.temporal = ""
        self.etiquetaV = ""
        self.etiquetaF = ""

        self.codigotemp= ""
        self.codigotempOtros = ""
        self.dimensiones = []

        self.diccionario = None

        self.Objeto = None
        self.valoresObjeto = []

        self.NombreStruck = None

    def iniciarRetorno(self,codigo, etiqueta, temporal,tipo):
        self.codigo = codigo
        self.etiqueta = etiqueta
        self.temporal = temporal
        self.tipo = tipo

    def iniciarRetornoArreglo(self,codigo,codigotemp, etiqueta, temporal,tipo, codigotempOtros,dimensiones):
        self.codigo = codigo
        self.codigotemp =codigotemp
        self.etiqueta = etiqueta
        self.temporal = temporal
        self.tipo = tipo
        self.codigotempOtros = codigotempOtros
        self.dimensiones = dimensiones



class Tipos():
    def __init__(self, nombre):
        self.nombre = nombre
        self.tipo = self.ObtenerTipo()

    def ObtenerTipo(self):
        if self.nombre == 'ENTERO':
            print("Se dectecto un entero")
            return tipo.ENTERO

        elif self.nombre == 'DECIMAL':
            print("Se dectecto un decimal")
            return tipo.DECIMAL

        elif self.nombre == 'DIRSTRING':
            print("Se dectecto una DIRSTRING")
            return tipo.DIRSTRING

        elif self.nombre == 'STRING':
            print("Se dectecto una STRING")
            return tipo.STRING

        elif self.nombre == 'CARACTER':
            print("Se dectecto una CARACTER")
            return tipo.CARACTER

        elif self.nombre == 'BOOLEANO':
            print("Se dectecto un booleano")
            return tipo.BOOLEANO

        elif self.nombre == 'USIZE':
            print("Se dectecto un USIZE")
            return tipo.USIZE


        else:
            return tipo.ERROR
