from AST.Abstracto.Instruccion import Intruccion
from AST.TablaSimbolos.Tipos import tipo as t
from AST.TablaSimbolos.Tipos import RetornoType
from AST.TablaSimbolos.InstanciaArreglo import InstanciaArreglo
from AST.TablaSimbolos.InstanciaVector import InstanciaVector
from AST.Expresion.Identificador import Identificador
from AST.Expresion.Arreglo.AccesoArreglo import AccesoArreglo
from AST.Expresion.Struct.AccesoStruct import AccesoStruct
class Imprimir(Intruccion):

    def __init__(self,  expresion, tipo, lista):
        self.expresion = expresion
        self.tipo = tipo
        self.lista =lista

    def EjecutarInstruccion(self, controlador, ts):

        global valor, tipo
        if len(self.lista) > 0:
            texto_salida = ""

            self.expresion = self.expresion.replace('\\n', '\n')
            print( self.expresion )
            if  self.expresion.count("{}") > 0:
                formato_nomal = self.expresion.split("{}")
                contador_nomal = self.expresion.count("{}")

                if contador_nomal == len(self.lista):

                    for i in range (0,len(formato_nomal)):
                        texto_salida += str(formato_nomal[i])
                        if i <= len(self.lista)-1:
                            try:
                                if isinstance(self.lista[i],AccesoArreglo):
                                    array = self.lista[i].ObtenerValor(controlador,ts)

                                    if isinstance(array, RetornoType):
                                        texto_salida += str(array.valor)
                                else:
                                    valor = self.lista[i].ObtenerValor(controlador,ts)

                                    texto_salida += str(valor.valor)
                            except:
                                print("Fallo en: ",self.lista[i])

                    print("Print final: ", texto_salida)
                            #print("Obtener tipo: ", self.lista[i].ObtenerTipo(controlador, ts))

                else:
                    # Error
                    pass


            if self.expresion.count("{:?}") > 0:
                print("Llego a impresion")
                ts.Print_Table()
                formato_nomal = self.expresion.split("{:?}")
                contador_nomal = self.expresion.count("{:?}")

                if contador_nomal == len(self.lista):

                    for i in range (0,len(formato_nomal)):
                        texto_salida += str(formato_nomal[i])
                        if i <= len(self.lista)-1:
                            try:

                                if isinstance(self.lista[i],Identificador):
                                    array = ts.ObtenerSimbolo(self.lista[i].id)

                                    if isinstance(array, InstanciaArreglo) or  isinstance(array, InstanciaVector):
                                        texto_salida += self.ObtenerArrayText(array.valores)
                                    else:
                                        texto_salida += str(self.lista[i].ObtenerValor(controlador, ts).valor)

                                elif isinstance(self.lista[i],AccesoArreglo):
                                    array = self.lista[i].ObtenerValor(controlador,ts)

                                    if isinstance(array, RetornoType):
                                        if isinstance(array.valor,InstanciaVector):
                                            texto_salida += self.ObtenerArrayText(array.valor.valores)
                                        else:
                                            texto_salida += self.ObtenerArrayText(array.valor)
                                elif isinstance(self.lista[i], AccesoStruct):
                                    dato = self.lista[i].ObtenerValor(controlador, ts)
                                    print(dato)
                                    if isinstance(dato.valor, InstanciaArreglo) or isinstance(dato.valor, InstanciaVector):
                                        texto_salida += self.ObtenerArrayText(dato.valor.valores)
                                    else:
                                        texto_salida += str(self.lista[i].ObtenerValor(controlador, ts).valor)

                                #array = self.lista[i].ObtenerValor(controlador,ts)

                            except:
                                print("Fallo en: ",self.lista[i])

                    print("Print final: ", texto_salida)
                            #print("Obtener tipo: ", self.lista[i].ObtenerTipo(controlador, ts))

                else:
                    # Error
                    pass


            #formato_lista = self.expresion.split("{:?}")
            #contador_lista  = self.expresion.count("{:?}")

            controlador.imprimir(texto_salida, self.tipo)
        else:
            return_exp: RetornoType = self.expresion.ObtenerValor(controlador, ts)

            valor = return_exp.valor
            tipo = return_exp.tipo
            valor = valor.replace('\\n', '\n')
            print("======!!!! ", tipo , " !!!!======")
            if tipo == t.STRING or tipo == t.DIRSTRING:
                print("Se confirmo")
                controlador.imprimir(valor , self.tipo)
            else:
                #error
                pass

    def ObtenerArrayText(self,array):
        print(type(array))
        text = ""
        if isinstance(array,list):
            text += "["

            bandera = True
            banderaint = len(array)
            aux = 0
            for x in array:
                if isinstance(x,list):
                    text += self.ObtenerArrayText(x)
                    if aux+1 != banderaint:
                        text += ","

                elif isinstance(x,InstanciaVector):
                    text += self.ObtenerArrayText(x.valores)
                    if aux + 1 != banderaint:
                        text += ","

                else:
                    if bandera:
                        text += str(x)
                        bandera = False
                    else:
                        text += "," + str(x)

                aux += 1

            text += "]"
            return text
        else:
            print("fallo")