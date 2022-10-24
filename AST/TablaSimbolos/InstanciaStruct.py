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


    def Obtener3D(self, controlador, ts):
        struct = ts.ObtenerSimbolo(self.identificador)
        declaraciones  = struct.valor.declaraciones
        diccionario = {}
        codigo = "/*Declaracion vector*/\n"

        listatemporales = []

        for y in self.asignaciones:
            name = y.identificador
            data = y.expresion.Obtener3D(controlador, ts)
            agregar = data

            for x in declaraciones:
                nombre = x.identificador
                tipo = x.expresion

                if name == nombre:
                    listatemporales.append(agregar.temporal)
                    codigo += agregar.codigo
                    diccionario[name] = copy.deepcopy(copy.copy(agregar))
                    break
        codigo += "/*Declaracion especifica*/\n"
        temp1 = controlador.Generador3D.obtenerTemporal()
        codigo += f'\t{temp1} = HP;\n'
        codigo += f'\tHeap[(int)HP] = {len(self.asignaciones)};\n'
        codigo += f'\tHP = HP + 1;\n'

        for x in listatemporales:
            codigo += f'\tHeap[(int)HP] = {x};\n'
            codigo += f'\tHP = HP + 1;\n'

        self.diccionario = diccionario

        retorno = RetornoType(copy.deepcopy(copy.copy(self)),t.STRUCT)
        retorno.temporal = temp1
        retorno.codigo = codigo
        retorno.diccionario = diccionario
        return retorno

    def SetValor(self):
        print("Ni idea")


    def ObtenerValor_var(self):
        print("Saber")