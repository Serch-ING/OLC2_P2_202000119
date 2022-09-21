from AST.Abstracto.Expresion import Expresion
from AST.Abstracto.Instruccion import Intruccion
from AST.TablaSimbolos.Tipos import tipo, RetornoType
from AST.TablaSimbolos.InstanciaArreglo import InstanciaArreglo
from AST.TablaSimbolos.InstanciaVector import InstanciaVector
from AST.Expresion.Arreglo.AccesoArreglo import AccesoArreglo
import math
import copy

class NativasVectores(Expresion,Intruccion):

    def EjecutarInstruccion(self, controlador, ts):
        self.ObtenerValor(controlador,ts)

    def __init__(self, expresion1, funcion, expresion2 = None):
        self.exp1 = expresion1
        self.exp2 = expresion2
        self.funcion = funcion
        self.expresion = None

    def ObtenerValor(self, controlador, ts):
        if self.exp1 is not None:
            return_exp = ts.ObtenerSimbolo(self.expresion.id)
            valor_expresion = return_exp.valores
            tipo_expresion = return_exp.tipo
            print("=== exp === ", self.exp1)
            print("=== exp valor === ",valor_expresion)
            print("=== exp tipo === ", tipo_expresion)
            print("=== exp tipo py === ", type(valor_expresion))

            if self.funcion == "remove":
                exp1 = self.exp1.ObtenerValor(controlador, ts)
                valor_exp1 = exp1.valor
                valor_tipo = exp1.tipo
                if tipo_expresion == valor_tipo:
                    devolucion = valor_expresion.pop(valor_exp1)
                    return RetornoType(devolucion, tipo_expresion)


            elif self.funcion == "push":

                exp1 =  self.exp1.ObtenerValor(controlador,ts)
                valor_exp1 = exp1.valor
                valor_tipo = exp1.tipo
                bandera = False

                if valor_tipo == tipo.VECTOR:
                    if exp1.valor.tipo == tipo_expresion:
                        bandera = True

                if tipo_expresion == valor_tipo or bandera:
                    valor_expresion.append(valor_exp1)

                    if return_exp.withcapacity == 0:
                        return_exp.withcapacity = 4
                    elif len(valor_expresion) > return_exp.withcapacity:
                        return_exp.withcapacity *= 2



            elif self.funcion == "contains" :
                if self.exp1.valor in valor_expresion:
                    return RetornoType(True, tipo.BOOLEANO)
                return RetornoType(False, tipo.BOOLEANO)

            elif self.funcion == "insert":
                exp1 = self.exp1.ObtenerValor(controlador, ts)
                valor_exp1 = exp1.valor
                valor_tipo1 = exp1.tipo

                exp2 = self.exp2.ObtenerValor(controlador, ts)
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
                return_exp = ts.ObtenerSimbolo(self.expresion.id)
                return RetornoType(return_exp.withcapacity, tipo.ENTERO)




