from AST.TablaSimbolos.Simbolos import Simbolos
from AST.Abstracto.Expresion import Expresion
from AST.Instruccion.Declaracion import Declaracion
from AST.TablaSimbolos.Tipos import RetornoType
from AST.TablaSimbolos.Tipos import tipo as t
from AST.Expresion.Identificador import Identificador
from AST.Expresion.Repeticiones import Repeticiones
import copy
from AST.Expresion.Repeticiones import Repeticiones

class InstanciaStruct(Expresion):
    def __init__(self, id, asignaciones):
        self.identificador = id
        self.asignaciones = asignaciones
        #self.diccionario = 0


    def Obtener3D(self, controlador, ts):
        struct = ts.ObtenerSimbolo(self.identificador)
        declaraciones  = struct.valor.declaraciones
        codigo = "/*Declaracion Strcuk*/\n"

        listatemporales = []
        diccionario = []
        buscando = False
        name = ""
        agregar = ""
        for x in declaraciones:
            nombre = x.identificador
            tipo = x.expresion
            if isinstance(tipo, Repeticiones):
                tipo = tipo.valor
            temporal = [nombre,tipo]
            for y in self.asignaciones:

                if not buscando:
                    name = y.identificador
                    data = y.expresion.Obtener3D(controlador, ts)
                    agregar = data
                    buscando = True

                if buscando:
                    if name == nombre:
                        diccionario.append(temporal)
                        listatemporales.append(agregar.temporal)
                        codigo += agregar.codigo
                        buscando = False
                        break
        codigo += "/*Declaracion especifica*/\n"
        temp1 = controlador.Generador3D.obtenerTemporal()
        codigo += f'\t{temp1} = HP;\n'
        codigo += f'\tHeap[(int)HP] = {len(self.asignaciones)};\n'
        codigo += f'\tHP = HP + 1;\n'

        for x in listatemporales:
            codigo += f'\tHeap[(int)HP] = {x};\n'
            codigo += f'\tHP = HP + 1;\n'

        codigo += "/*fin Declaracion Strcuk*/\n"

        retorno = RetornoType(copy.deepcopy(copy.copy(self)),t.STRUCT)
        retorno.temporal = temp1
        retorno.codigo = codigo
        retorno.diccionario = diccionario
        return retorno

    def SetValor(self):
        print("Ni idea")


    def ObtenerValor_var(self):
        print("Saber")