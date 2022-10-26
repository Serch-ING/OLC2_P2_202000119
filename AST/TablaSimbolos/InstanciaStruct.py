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
        declaraciones = struct.valor.declaraciones
        codigo = "/*Declaracion Strcuk*/\n"

        listatemporales = []
        buscando = False
        name = ""
        for x in declaraciones:
            nombre = x.identificador
            tipo = x.expresion

            for y in self.asignaciones:
                name = y.identificador

                if name == nombre:
                    data = y.expresion.Obtener3D(controlador, ts)
                    listatemporales.append(data.temporal)
                    codigo += data.codigo
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
        #retorno.diccionario = diccionario
        retorno.NombreStruck = self.identificador
        return retorno

    def SetValor(self):
        print("Ni idea")


    def ObtenerValor_var(self):
        print("Saber")