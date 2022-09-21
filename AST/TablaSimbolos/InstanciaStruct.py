from AST.TablaSimbolos.Simbolos import Simbolos
from AST.Abstracto.Expresion import Expresion
from AST.Instruccion.Declaracion import Declaracion
from AST.TablaSimbolos.Tipos import RetornoType
from AST.TablaSimbolos.Tipos import tipo as t
from AST.Expresion.Identificador import Identificador
from AST.Expresion.Repeticiones import Repeticiones
import copy

class InstanciaStruct(Expresion):
    def __init__(self, id, asignaciones):
        self.identificador = id
        self.asignaciones = asignaciones
        self.diccionario = 0

    def ObtenerValor(self, controlador, ts):
        struct = ts.ObtenerSimbolo(self.identificador)
        declaraciones  = struct.valor.declaraciones
        diccionario = {}

        for x  in declaraciones:
            nombre = x.identificador
            tipo = x.expresion
            if isinstance(tipo,Identificador):
                tipo =  ts.ObtenerSimbolo(tipo.id)
                tipo = tipo.valor.identificador

            for y in self.asignaciones:
                name = y.identificador
                data = y.expresion.ObtenerValor(controlador,ts)
                agregar = data
                if isinstance(y.expresion, Identificador):
                    data = ts.ObtenerSimbolo(y.expresion.id)
                    if isinstance(data.valor,InstanciaStruct):
                        agregar = data
                        data = data.valor.identificador
                    else:
                        agregar = data
                        data = data.tipo
                elif isinstance(data,RetornoType):
                    if isinstance(data.valor,InstanciaStruct):
                        agregar = data
                        data = data.valor.identificador
                    else:
                        agregar = data
                        data = data.tipo


                if name == nombre:
                    if isinstance(tipo,Repeticiones):
                        tipo = t.ARRAY
                    if data == tipo:
                        diccionario[name] = copy.deepcopy(copy.copy(agregar))
                        break
        self.diccionario = diccionario


        return RetornoType(copy.deepcopy(copy.copy(self)),t.STRUCT)

    def SetValor(self):
        print("Ni idea")


    def ObtenerValor_var(self):
        print("Saber")