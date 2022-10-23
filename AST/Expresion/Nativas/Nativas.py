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


        if self.funcion == "abs()":
            return_exp1 = self.expresion.Obtener3D(controlador, ts)
            tipo_exp1 = return_exp1.tipo

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
            return_exp1 = self.expresion.Obtener3D(controlador, ts)
            tipo_exp1 = return_exp1.tipo

            if tipo_exp1 == tipo.DECIMAL:
                codigo += return_exp1.codigo

                tempraiz = controlador.Generador3D.obtenerTemporal()
                codigo += f'\t{tempraiz} = {return_exp1.temporal} / 2;\n'

                temp = controlador.Generador3D.obtenerTemporal()

                etq1 = controlador.Generador3D.obtenerEtiqueta()
                etq2 = controlador.Generador3D.obtenerEtiqueta()
                etq3 = controlador.Generador3D.obtenerEtiqueta()

                codigo += f'\t{etq1}:\n'
                codigo += f'if({tempraiz} != {temp}) goto {etq2};'
                codigo += f'\tgoto {etq3};\n'

                codigo += f'\t{etq2}:\n'
                codigo += f'\t{temp} = {tempraiz};\n'
                codigo += f'\t{tempraiz} = {return_exp1.temporal} / {temp};\n'
                codigo += f'\t{tempraiz} = {tempraiz} + {temp};\n'
                codigo += f'\t{tempraiz} = {tempraiz} / 2;\n'
                codigo += f'\tgoto {etq1};\n'

                codigo += f'\t{etq3}:\n'

                #codigo += f'\t{return_exp1.temporal} = sqrt({return_exp1.temporal}) ;\n'


                retorno = RetornoType()
                #retorno.iniciarRetorno(codigo, "", return_exp1.temporal, tipo_exp1)
                retorno.iniciarRetorno(codigo, "", tempraiz, tipo_exp1)
                return retorno

        elif self.funcion == "to_string()" or self.funcion == "to_owned()":
            return_exp1 = self.expresion.Obtener3D(controlador, ts)
            tipo_exp1 = return_exp1.tipo

            if tipo_exp1 == tipo.DIRSTRING:
                return_exp1.tipo = tipo.STRING
                return return_exp1

        elif self.funcion == "clone()":

            return_exp1 = None
            tipo_exp1 = None

            if isinstance(self.expresion, AccesoArreglo):

                return_exp1 = self.expresion.Obtener3D(controlador, ts)
                tipo_exp1 = return_exp1.tipo
                codigo += "/*Clonacion*/\n"
                codigo += return_exp1.codigo

                if tipo_exp1 == tipo.STRING:
                    tipo_exp1 = tipo.DIRSTRING

                    temp1 = controlador.Generador3D.obtenerTemporal()
                    etq1 = controlador.Generador3D.obtenerEtiqueta()
                    etq2 = controlador.Generador3D.obtenerEtiqueta()
                    etq3 = controlador.Generador3D.obtenerEtiqueta()
                    temp2 = controlador.Generador3D.obtenerTemporal()

                    array = return_exp1
                    codigo += f'\t{temp2} = HP;\n'

                    codigo += f'\t{etq1}:\n'
                    codigo += f'\t{temp1} = Heap[(int){array.temporal}];\n'
                    codigo += f'\tif ({temp1} != 0 ) goto {etq2};\n'
                    codigo += f'\tgoto {etq3};\n'

                    codigo += f'\t{etq2}:\n'
                    codigo += f'\tHeap[HP] = {temp1};\n'
                    codigo += f'\tHP = HP +1;\n'
                    codigo += f'\t{array.temporal} = {array.temporal} + 1;\n'
                    codigo += f'\tgoto {etq1};\n'

                    codigo += f'\t{etq3}:\n'
                    codigo += f'\tHeap[HP] = 0;\n'
                    codigo += f'\tHP = HP +1;\n'

                    retorno = RetornoType()
                    retorno.iniciarRetorno(codigo, "", temp2, tipo_exp1)
                    return retorno

        elif self.funcion == "len()":
            if isinstance(self.expresion,AccesoArreglo):
                self.expresion.opcion = True
                return_exp1 = self.expresion.Obtener3D(controlador, ts)
                codigo += return_exp1.codigo

                codigo += f'\t{return_exp1.temporal} = Heap[(int){return_exp1.temporal}];\n'

                retorno = RetornoType()
                retorno.iniciarRetorno(codigo, "",return_exp1.temporal , return_exp1.tipo)
                return retorno

            else:
                return_exp1 = ts.ObtenerSimbolo(self.expresion.id)

                simbolo = return_exp1
                while simbolo.referencia:
                    simbolo = simbolo.tsproviene.ObtenerSimbolo(simbolo.idproviene)

                if isinstance(simbolo,InstanciaArreglo) or isinstance(simbolo,InstanciaVector):
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

                    #codigo += f'\n{temp1} = SP + {return_exp1.direccion};\n'
                    #codigo += f'\n{temp2} = Stack[(int){temp1}];\n'
                    codigo += f'\n{temp3} = Heap[(int){temp2}];\n'
                    retorno = RetornoType()
                    retorno.iniciarRetorno(codigo,"",temp3,tipo.ENTERO)
                    return retorno






