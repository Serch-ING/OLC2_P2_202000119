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


                    codigo += exp1.codigo


                    temp1 = controlador.Generador3D.obtenerTemporal()
                    codigo += f'\t{temp1} = SP + {return_exp.direccion};\n'
                    temp2 = controlador.Generador3D.obtenerTemporal()
                    codigo += f'\t{temp2} = Stack[(int){temp1}];\n'

                    codigo += self.generarAddSpacio(temp2, valor_expresion, controlador, temp1)
                    valor_expresion.append(valor_exp1)
                    direccionA = len(valor_expresion) - 1

                    codigo += f'\tHeap[(int){temp2}] = {len(valor_expresion)};\n'

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
                exp2 = self.exp2.Obtener3D(controlador, ts)


                codigo += exp1.codigo
                codigo += exp2.codigo

                temp1 = controlador.Generador3D.obtenerTemporal()
                codigo += f'\t{temp1} = SP + {return_exp.direccion};\n'
                temp2 = controlador.Generador3D.obtenerTemporal()
                codigo += f'\t{temp2} = Stack[(int){temp1}];\n'


                codigo += self.generarAddSpacio(temp2,valor_expresion,controlador,temp1)
                valor_expresion.append(self.exp1)

                tempF = controlador.Generador3D.obtenerTemporal()
                codigo += f'\t{tempF} = {temp2};\n'

                temp3 = controlador.Generador3D.obtenerTemporal() # Obtener longitud
                codigo += f'\t{temp3} = Heap[(int){temp2}];\n'

                codigo += f'\t{temp3} = {temp3} - {exp1.temporal};\n' #quitar lo que se salta
                temp4 = controlador.Generador3D.obtenerTemporal()
                codigo += f'\t{temp4} = 0;\n' # temporal

                codigo += f'\t{temp2} = {temp2} + 2;\n'
                codigo += f'\t{temp2} = {temp2} + {exp1.temporal};\n'

                temp5 = controlador.Generador3D.obtenerTemporal()
                codigo += f'\t{temp5} = {temp2};\n'

                etq1 = controlador.Generador3D.obtenerEtiqueta()
                etq2 = controlador.Generador3D.obtenerEtiqueta()
                etq3 = controlador.Generador3D.obtenerEtiqueta()

                codigo += f'\t{etq1}:\n'
                codigo += f'\tif( {temp4} < {temp3}) goto {etq2};\n'
                codigo += f'\tgoto {etq3};\n'
                codigo += f'\t{etq2}:\n'

                temp6 = controlador.Generador3D.obtenerTemporal()
                codigo += f'\t{temp6} = Heap[(int){temp5}];\n'#guardamos actual

                temp7 = controlador.Generador3D.obtenerTemporal()
                codigo += f'\t{temp7} = {temp5} + 1;\n'

                temp8 = controlador.Generador3D.obtenerTemporal()
                codigo += f'\t{temp8} = Heap[(int){temp7}];\n' #guardamos el sieguiente

                codigo += f'\tHeap[(int){temp5}] = {exp2.temporal};\n'
                codigo += f'\tHeap[(int){temp7}] = {temp6};\n'
                codigo += f'\t{exp2.temporal} = {temp8};\n'

                codigo += f'\t{temp5} = {temp5} + 2;\n'
                codigo += f'\t{temp4} = {temp4} + 1;\n'
                codigo += f'\tgoto {etq1};\n'

                codigo += f'\t{etq3}:\n'

                codigo += f'\tHeap[(int){tempF}] = {len(valor_expresion)};\n'#asignar lueva longiud
                temp9 = controlador.Generador3D.obtenerTemporal()
                codigo += f'\t{temp9} = {tempF} + 1;\n'


                return codigo

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

    def generarAddSpacio(self,inical,valor_expresion,controlador,vaStack):
        codigo = "/*Validar mover vector*/\n"

        temp1 = controlador.Generador3D.obtenerTemporal()
        codigo += f'\t{temp1} ={inical} + 1;\n'

        temp2 = controlador.Generador3D.obtenerTemporal() #obtener capacidad
        codigo += f'\t{temp2} = Heap[(int){temp1}];\n'

        etq4 = controlador.Generador3D.obtenerEtiqueta()
        etq5 = controlador.Generador3D.obtenerEtiqueta()

        codigo += f'\tif( {len(valor_expresion)} == {temp2}) goto {etq4};\n'
        codigo += f'\tgoto {etq5};\n'
        codigo += f'\t{etq4}:\n'

        Capacidad = controlador.Generador3D.obtenerTemporal()
        codigo += f'\t{Capacidad} = {temp2} * 2;\n'

        indeceinical = controlador.Generador3D.obtenerTemporal()
        codigo+= "/*Inicial*/\n"
        codigo += f'\t{indeceinical} = {inical} + 2;\n'

        indecefinal = controlador.Generador3D.obtenerTemporal()
        codigo += "/*Final*/\n"
        codigo += f'\t{indecefinal} =  {indeceinical} + {len(valor_expresion)};\n'

        etq6 = controlador.Generador3D.obtenerEtiqueta()
        etq7 = controlador.Generador3D.obtenerEtiqueta()
        etq8 = controlador.Generador3D.obtenerEtiqueta()

        temp11 = controlador.Generador3D.obtenerTemporal()
        codigo += f'\t{temp11} = HP;\n'

        codigo += f'\tHeap[(int){temp11}] = {len(valor_expresion)};\n'
        codigo += f'\t{temp11} = {temp11}+1;\n'
        codigo += f'\tHeap[(int){temp11}] = {Capacidad};\n'
        codigo += f'\t{temp11} = {temp11}+1;\n'

        codigo += f'\t{etq6}:\n'
        codigo += f'\tif( {indeceinical} < {indecefinal}) goto {etq7};\n'
        codigo += f'\tgoto {etq8};\n'
        codigo += f'\t{etq7}:\n'

        temp12 = controlador.Generador3D.obtenerTemporal()
        codigo += f'\t{temp12} = Heap[(int){indeceinical}];\n'
        codigo += f'\tHeap[(int){temp11}] = {temp12};\n'
        codigo += f'\t{temp11} = {temp11}+1;\n'
        codigo += f'\t{indeceinical} = {indeceinical} + 1;\n'

        codigo += f'\tgoto {etq6};\n'
        codigo += f'\t{etq8}:\n'

        codigo += f'\t{inical} = HP;\n'
        codigo += f'\tStack[(int){vaStack}] = HP;\n'
        codigo += f'\tHP= HP + 2;\n'
        codigo += f'\tHP= HP + {Capacidad};\n'
        codigo += "/*End validar*/\n"

        codigo += f'\t{etq5}:\n'


        return codigo



