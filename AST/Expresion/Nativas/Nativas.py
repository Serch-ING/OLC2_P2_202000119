from AST.Abstracto.Expresion import Expresion
from AST.TablaSimbolos.Tipos import tipo,RetornoType
from AST.TablaSimbolos.InstanciaArreglo import InstanciaArreglo
from AST.TablaSimbolos.InstanciaVector import InstanciaVector
from AST.Expresion.Arreglo.AccesoArreglo import AccesoArreglo
import math
import copy

class Nativas(Expresion):

    def __init__(self, expresion, funcion):
        self.expresion = expresion
        self.funcion = funcion

    def Obtener3D(self, controlador, ts):
        codigo = "/*Nativas*/\n"
        return_exp1: RetornoType = self.expresion.Obtener3D(controlador, ts)
        tipo_exp1 = return_exp1.tipo
        print("=== exp === ", self.expresion)
        print("=== exp tipo === ", tipo_exp1)
        print("=== exp tipo py === ", type(2))

        if self.funcion == "abs()":
            if tipo_exp1 == tipo.ENTERO or tipo_exp1 == tipo.DECIMAL:
                etq1 = controlador.Generador3D.obtenerEtiqueta()
                etq2 = controlador.Generador3D.obtenerEtiqueta()
                codigo += return_exp1.codigo
                codigo += f'\tif ({return_exp1.temporal}<0) goto {etq1};\n'
                codigo += f'\tgoto {etq2};\n'
                codigo += f'\t{etq1}:\n'
                codigo += f'\t{return_exp1.temporal} = {return_exp1.temporal} * -1;\n'
                codigo += f'\t{etq2}:\n'
                retorno = RetornoType()
                retorno.iniciarRetorno(codigo,"",return_exp1.temporal,tipo_exp1)
                return retorno

        elif self.funcion == "sqrt()":
            if tipo_exp1 == tipo.DECIMAL:
                codigo += return_exp1.codigo
                codigo += f'\t{return_exp1.temporal} = sqrt({return_exp1.temporal}) ;\n'
                retorno = RetornoType()
                retorno.iniciarRetorno(codigo, "", return_exp1.temporal, tipo_exp1)
                return retorno

        elif self.funcion == "to_string()" or self.funcion == "to_owned()":
            if tipo_exp1 == tipo.DIRSTRING:
                return_exp1.tipo = tipo.DIRSTRING
                return return_exp1

        elif self.funcion == "clone()":
            if tipo_exp1 == tipo.STRING:
                tipo_exp1 = tipo.DIRSTRING
            #return RetornoType(copy.deepcopy(valor_exp1), tipo_exp1)

        elif self.funcion == "len()":
            if isinstance(self.expresion,AccesoArreglo):
                return_exp1: RetornoType = self.expresion.Obtener3D(controlador, ts)
                if isinstance(return_exp1,RetornoType):
                    return RetornoType(len(return_exp1.valor), tipo.ENTERO)
                print(return_exp1)
            else:
                return_exp1 = ts.ObtenerSimbolo(self.expresion.id)
                if isinstance(return_exp1,InstanciaArreglo) or isinstance(return_exp1,InstanciaVector):
                    temp1 = controlador.Generador3D.obtenerTemporal()
                    temp2 = controlador.Generador3D.obtenerTemporal()
                    temp3 = controlador.Generador3D.obtenerTemporal()
                    codigo += f'\n{temp1} = SP + {return_exp1.direccion};\n'
                    codigo += f'\n{temp2} = Stack[(int){temp1}];\n'
                    codigo += f'\n{temp3} = Heap[(int){temp2}];\n'
                    retorno = RetornoType()
                    retorno.iniciarRetorno(codigo,"",temp3,tipo.ENTERO)
                    return retorno






