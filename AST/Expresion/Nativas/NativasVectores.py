from AST.Abstracto.Expresion import Expresion
from AST.Abstracto.Instruccion import Intruccion
from AST.TablaSimbolos.Tipos import tipo, RetornoType
from AST.TablaSimbolos.InstanciaArreglo import InstanciaArreglo
from AST.TablaSimbolos.InstanciaVector import InstanciaVector
from AST.Expresion.Arreglo.AccesoArreglo import AccesoArreglo
import math
import copy

class NativasVectores(Expresion,Intruccion):

    def Ejecutar3D(self, controlador, ts):
        return self.Obtener3D(controlador, ts)

    def __init__(self, expresion1, funcion, expresion2 = None):
        self.exp1 = expresion1
        self.exp2 = expresion2
        self.funcion = funcion
        self.expresion = None

    def Obtener3D(self, controlador, ts):
        codigo = "/*Nativa vector*/\n"
        if self.exp1 is not None:
            return_exp = ts.ObtenerSimbolo(self.expresion.id)
            valor_expresion = return_exp.valores
            tipo_expresion = return_exp.tipo
            print("=== exp === ", self.exp1)
            print("=== exp valor === ",valor_expresion)
            print("=== exp tipo === ", tipo_expresion)
            print("=== exp tipo py === ", type(valor_expresion))

            if self.funcion == "remove":
                exp1 = self.exp1.Obtener3D(controlador, ts)
                valor_exp1 = exp1.valor
                valor_tipo = exp1.tipo
                if tipo_expresion == valor_tipo:
                    devolucion = valor_expresion.pop(valor_exp1)
                    return RetornoType(devolucion, tipo_expresion)


            elif self.funcion == "push":
                return_exp = ts.ObtenerSimbolo(self.expresion.id)

                exp1 =  self.exp1.Obtener3D(controlador, ts)
                valor_exp1 = exp1.valor
                valor_tipo = exp1.tipo
                bandera = False

                if valor_tipo == tipo.VECTOR:
                    if exp1.valor.tipo == tipo_expresion:
                        bandera = True

                if tipo_expresion == valor_tipo or bandera:
                    valor_expresion.append(valor_exp1)

                    codigo += exp1.codigo
                    direccionA = len(valor_expresion) - 1

                    temp1 = controlador.Generador3D.obtenerTemporal()
                    codigo += f'\t{temp1} = SP + {return_exp.direccion};\n'
                    temp2 = controlador.Generador3D.obtenerTemporal()
                    codigo += f'\t{temp2} = Stack[(int){temp1}];\n'
                    codigo += f'\t{temp2} = {temp2} + {direccionA+2};\n'
                    codigo += f'\tHeap[(int){temp2}] = {exp1.temporal};\n'

                    if return_exp.withcapacity == 0:
                        return_exp.withcapacity = 4
                    elif len(valor_expresion) > return_exp.withcapacity:
                        return_exp.withcapacity *= 2

                    return codigo



            elif self.funcion == "contains" :
                if self.exp1.valor in valor_expresion:
                    return RetornoType(True, tipo.BOOLEANO)
                return RetornoType(False, tipo.BOOLEANO)

            elif self.funcion == "insert":
                exp1 = self.exp1.Obtener3D(controlador, ts)
                valor_exp1 = exp1.valor
                valor_tipo1 = exp1.tipo

                exp2 = self.exp2.Obtener3D(controlador, ts)
                valor_exp2 = exp2.valor
                valor_tipo2 = exp2.tipo

                if tipo_expresion == valor_tipo2:
                    valor_expresion.insert(valor_exp1,valor_exp2)

                    if return_exp.withcapacity == 0:
                        return_exp.withcapacity = 4
                    elif len(valor_expresion) > return_exp.withcapacity:
                        return_exp.withcapacity *= 2
        else:
            if self.funcion == "capacity()":
                return_exp1 = ts.ObtenerSimbolo(self.expresion.id)

                simbolo = return_exp1
                while simbolo.referencia:
                    simbolo = simbolo.tsproviene.ObtenerSimbolo(simbolo.idproviene)

                temp1 = controlador.Generador3D.obtenerTemporal()
                temp2 = controlador.Generador3D.obtenerTemporal()
                temp3 = controlador.Generador3D.obtenerTemporal()

                if not return_exp1.referencia:
                    codigo += f'\t{temp1} = SP + {return_exp1.direccion};\n'
                    codigo += f'\t{temp2} = Stack[(int){temp1}];\n'
                else:
                    codigo += f'\t{temp2} = SP + {return_exp1.direccion};\n'
                    codigo += f'\t{temp2} = Stack[(int){temp2}];\n'
                    while return_exp1.referencia:
                        codigo += f'\t{temp2} = Stack[(int){temp2}];\n'
                        return_exp1 = return_exp1.tsproviene.ObtenerSimbolo(return_exp1.idproviene)

                # codigo += f'\n{temp1} = SP + {return_exp1.direccion};\n'
                # codigo += f'\n{temp2} = Stack[(int){temp1}];\n'
                codigo += f'\n{temp2} = {temp2} + 1;\n'
                codigo += f'\n{temp3} = Heap[(int){temp2}];\n'
                retorno = RetornoType()
                retorno.iniciarRetorno(codigo, "", temp3, tipo.ENTERO)
                return retorno




