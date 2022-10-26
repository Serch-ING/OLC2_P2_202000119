from AST.Abstracto.Instruccion import Intruccion
from AST.TablaSimbolos.Tipos import tipo as t
from AST.TablaSimbolos.Tipos import RetornoType
from AST.TablaSimbolos.InstanciaArreglo import InstanciaArreglo
from AST.TablaSimbolos.InstanciaVector import InstanciaVector
from AST.Expresion.Identificador import Identificador
from AST.Expresion.Arreglo.AccesoArreglo import AccesoArreglo
from AST.Expresion.Struct.AccesoStruct import AccesoStruct
from AST.Expresion.Operaciones.Relacional import Relacional
from AST.Instruccion.Declaracion import Declaracion
from AST.TablaSimbolos.Simbolos import Simbolos
from AST.Expresion.Operaciones.Logica import Logica
from AST.Expresion.Nativas.NativasVectores import NativasVectores




from AST.TablaSimbolos.Tipos import Tipos
from AST.Expresion.Primitivo import Primitivo
class Imprimir(Intruccion):

    def __init__(self, expresion, tipo, lista):
        self.expresion = expresion
        self.tipo = tipo
        self.lista = lista
        self.esarray = False

    def Ejecutar3D(self, controlador, ts):
        listarelacionales = []
        codigo = "/*Acceso imprimir*/\n"


        if len(self.lista) > 0:
            texto_salida = ""

            if self.expresion.count("{}") > 0:
                print(self.expresion)
                formato_nomal = self.expresion.split("{}")
                contador_nomal = self.expresion.count("{}")

                if contador_nomal == len(self.lista):

                    for i in range(0, len(formato_nomal)):
                        texto_salida += str(formato_nomal[i])

                        if i <= len(self.lista) - 1:
                            # try:

                            if isinstance(self.lista[i], AccesoArreglo):
                                primitivo = Primitivo("Se intento acceder a posicion fuera del array", Tipos('STRING'))
                                imprimir = Imprimir(primitivo, True, [])
                                #exp = imprimir.Ejecutar3D(controlador, ts)

                                self.lista[i].varprint = imprimir

                                self.lista[i].VecordeVector = False
                                array = self.lista[i].Obtener3D(controlador, ts)
                                codigo += array.codigo
                                texto_salida += self.addsimbolos(array.temporal, array.tipo)

                            elif isinstance(self.lista[i], Identificador):
                                valoid = self.lista[i].Obtener3D(controlador, ts)
                                codigo += valoid.codigo
                                texto_salida += self.addsimbolos(valoid.temporal, valoid.tipo)
                                print("")

                            elif isinstance(self.lista[i], Relacional):

                                temp = controlador.Generador3D.obtenerTemporal()

                                etqSalida = controlador.Generador3D.obtenerEtiqueta()
                                self.lista[i].etiquetaV = controlador.Generador3D.obtenerEtiqueta()
                                self.lista[i].etiquetaF = controlador.Generador3D.obtenerEtiqueta()
                                ObtenerRetorno = self.lista[i].Obtener3D(controlador, ts)
                                codigo += ObtenerRetorno.codigo
                                codigo += f'\t{self.lista[i].etiquetaV}:\n'
                                codigo += f'\t{temp} = 1;\n'
                                codigo += f'\tgoto {etqSalida};\n'
                                codigo += f'\t{temp}  = 0;\n'
                                codigo += f'\t{self.lista[i].etiquetaF}:\n'
                                codigo += f'\t{etqSalida}:\n'
                                texto_salida += self.addsimbolos(temp, ObtenerRetorno.tipo)
                                listarelacionales.append(temp)

                            elif isinstance(self.lista[i], Logica):

                                self.lista[i].etiquetaV = controlador.Generador3D.obtenerEtiqueta()
                                self.lista[i].etiquetaF = controlador.Generador3D.obtenerEtiqueta()
                                etqFuera = controlador.Generador3D.obtenerEtiqueta()
                                return_exp1 = self.lista[i].Obtener3D(controlador, ts)
                                temp1 = controlador.Generador3D.obtenerTemporal()

                                codigo += return_exp1.codigo

                                codigo += f'\t{return_exp1.etiquetaV}:\n'
                                codigo += f'\t{temp1} = 1;\n'
                                codigo += f'\tgoto {etqFuera};\n'

                                codigo += f'\t{return_exp1.etiquetaF}:\n'
                                codigo += f'\t{temp1} = 0;\n'

                                codigo += f'\t{etqFuera}:\n'

                                texto_salida += self.addsimbolos(temp1, t.ENTERO)

                            elif isinstance(self.lista[i],NativasVectores):
                                self.lista[i].provienePrint = True
                                ObtenerRetorno = self.lista[i].Obtener3D(controlador, ts)
                                codigo += ObtenerRetorno.codigo
                                # controlador.Generador3D.agregarInstruccion(ObtenerRetorno.codigo)
                                texto_salida += self.addsimbolos(ObtenerRetorno.temporal, ObtenerRetorno.tipo)

                            elif isinstance(self.lista[i], AccesoStruct):
                                ObtenerRetorno = self.lista[i].Obtener3D(controlador, ts)
                                codigo += ObtenerRetorno.codigo

                                if ObtenerRetorno.tipo == t.DIRSTRING or ObtenerRetorno.tipo == t.STRING:
                                    texto_salida += self.addsimbolos(ObtenerRetorno.temporal, ObtenerRetorno.tipo,False)

                                else:
                                    #tempF = controlador.Generador3D.obtenerTemporal()
                                    #codigo += f'\t{tempF} = Heap[(int){ObtenerRetorno.temporal}];\n'
                                    #texto_salida += self.addsimbolos(tempF, ObtenerRetorno.tipo)
                                    texto_salida += self.addsimbolos(ObtenerRetorno.temporal, ObtenerRetorno.tipo)
                            else:
                                # try:
                                ObtenerRetorno = self.lista[i].Obtener3D(controlador, ts)
                                codigo += ObtenerRetorno.codigo
                                # controlador.Generador3D.agregarInstruccion(ObtenerRetorno.codigo)
                                texto_salida += self.addsimbolos(ObtenerRetorno.temporal, ObtenerRetorno.tipo)

                            # except:
                            #    texto_salida += self.addsimbolos(self.lista[i].valor,self.lista[i].tipo.tipo)
                        # except:
                        #    print("Fallo en: ", self.lista[i])

                    retorno = self.obtenerCadenaUnida(texto_salida, controlador)
                    codigo += self.Codigofinal(retorno, controlador)
                    for x in listarelacionales:
                        codigo += f'\t{x}  = 0;\n'
                    print("Print final: ", texto_salida)
                    return codigo

            if self.expresion.count("{:?}") > 0:
                print(self.expresion)
                formato_nomal = self.expresion.split("{:?}")
                contador_nomal = self.expresion.count("{:?}")
                esPrimero = True
                retornoPrimero = ""

                if contador_nomal == len(self.lista):

                    for i in range(0, len(formato_nomal)):
                        texto_salida = str(formato_nomal[i])
                        retono = self.obtenerCadenaUnidaAarray(texto_salida, controlador)
                        codigo += retono.codigo
                        if esPrimero:
                            retornoPrimero = retono
                            esPrimero = False

                        if i <= len(self.lista) - 1:
                            try:
                                if isinstance(self.lista[i], AccesoArreglo):
                                    self.lista[i].opcion = True
                                    array = self.lista[i].Obtener3D(controlador, ts)

                                    if isinstance(array, RetornoType):
                                        codigo += array.codigo

                                        temp1 = controlador.Generador3D.obtenerTemporal()
                                        etq1 = controlador.Generador3D.obtenerEtiqueta()
                                        etq2 = controlador.Generador3D.obtenerEtiqueta()
                                        etq3 = controlador.Generador3D.obtenerEtiqueta()
                                        temp2 = controlador.Generador3D.obtenerTemporal()
                                        etq4 = controlador.Generador3D.obtenerEtiqueta()
                                        codigo += f'/*Gaurdar acceso imprimir*/\n'
                                        codigo += f'\tHeap[HP] = {ord("[")};\n'
                                        codigo += f'\tHP = HP +1;\n'

                                        codigo += f'\t{temp1} = {array.temporal} + 1;\n'
                                        codigo += f'\t{array.temporal} = Heap[(int){array.temporal}];\n'

                                        if array.etiqueta == "ETIQUETA":
                                            codigo += f'\t{temp1} = {temp1} + 1;\n'

                                        codigo += f'\t{etq1}:\n'
                                        codigo += f'\tif ({array.temporal} >0 ) goto {etq2};\n'
                                        codigo += f'\tgoto {etq3};\n'

                                        codigo += f'\t{etq2}:\n'
                                        codigo += f'\t{array.temporal} = {array.temporal} - 1;\n'

                                        codigo += f'\t{temp2} = Heap[(int){temp1}] ;\n'
                                        codigo += f'\t{temp1} = {temp1} + 1;\n'

                                        if array.tipo == t.ENTERO:
                                            codigo += f'\tHeap[HP] = {ord("¥")};\n'
                                            codigo += f'\tHP = HP +1;\n'
                                        elif array.tipo == t.DECIMAL:
                                            codigo += f'\tHeap[HP] = {ord("¢")};\n'
                                            codigo += f'\tHP = HP +1;\n'

                                        codigo += f'\tHeap[HP] = {temp2};\n'
                                        codigo += f'\tHP = HP +1;\n'

                                        codigo += f'\tif ({array.temporal} == 0 ) goto {etq4};\n'
                                        codigo += f'\tHeap[HP] = {ord(",")};\n'
                                        codigo += f'\tHP = HP +1;\n'
                                        codigo += f'\t{etq4}:\n'

                                        codigo += f'\tgoto {etq1};\n'
                                        codigo += f'\t{etq3}:\n'

                                        codigo += f'\tHeap[HP] = {ord("]")};\n'
                                        codigo += f'\tHP = HP +1;\n'

                                elif isinstance(self.lista[i], Identificador):
                                    simbolo: Simbolos = ts.ObtenerSimbolo(self.lista[i].id)

                                    while simbolo.referencia:
                                        simbolo = simbolo.tsproviene.ObtenerSimbolo(simbolo.idproviene)

                                    valoid = self.lista[i].Obtener3D(controlador, ts)
                                    codigo += valoid.codigo
                                    tempAcceso = controlador.Generador3D.obtenerTemporal()
                                    codigo += f'\t{tempAcceso} = Heap[(int){valoid.temporal}];\n'

                                    validacion = False
                                    if len(simbolo.valores) > 0:
                                        if simbolo.valores[0] != t.VECTOR:
                                            validacion = True
                                    else:
                                        validacion = True

                                    if isinstance(simbolo, InstanciaArreglo) or validacion :
                                        temp1 = controlador.Generador3D.obtenerTemporal()
                                        etq1 = controlador.Generador3D.obtenerEtiqueta()
                                        etq2 = controlador.Generador3D.obtenerEtiqueta()
                                        etq3 = controlador.Generador3D.obtenerEtiqueta()
                                        temp2 = controlador.Generador3D.obtenerTemporal()
                                        etq4 = controlador.Generador3D.obtenerEtiqueta()

                                        codigo += f'\tHeap[HP] = {ord("[")};\n'
                                        codigo += f'\tHP = HP +1;\n'
                                        if isinstance(simbolo, InstanciaVector):
                                            codigo += f'\t{valoid.temporal} = {valoid.temporal} + 1;\n'
                                        codigo += f'\t{temp1} = {valoid.temporal};\n'
                                        codigo += f'\t{etq1}:\n'
                                        codigo += f'\tif ({tempAcceso} >0 ) goto {etq2};\n'
                                        codigo += f'\tgoto {etq3};\n'

                                        codigo += f'\t{etq2}:\n'
                                        codigo += f'\t{tempAcceso} = {tempAcceso} - 1;\n'


                                        codigo += f'\t{temp1} = {temp1} + 1;\n'
                                        codigo += f'\t{temp2} = Heap[(int){temp1}] ;\n'

                                        if valoid.tipo == t.ENTERO:
                                            codigo += f'\tHeap[HP] = {ord("¥")};\n'
                                            codigo += f'\tHP = HP +1;\n'
                                        elif valoid.tipo == t.DECIMAL:
                                            codigo += f'\tHeap[HP] = {ord("¢")};\n'
                                            codigo += f'\tHP = HP +1;\n'
                                        elif valoid.tipo == t.DIRSTRING or valoid.tipo == t.STRING:
                                            temp3 = controlador.Generador3D.obtenerTemporal()
                                            temp4 = controlador.Generador3D.obtenerTemporal()
                                            etq5 = controlador.Generador3D.obtenerEtiqueta()
                                            etq6 = controlador.Generador3D.obtenerEtiqueta()
                                            etq7 = controlador.Generador3D.obtenerEtiqueta()
                                            codigo+="/*parte strint*/\n"
                                            codigo += f'\t{temp3} = {temp2};\n'
                                            #codigo += f'\t{temp3} = {temp2} - 1;\n'

                                            codigo += f'\t{etq7}:\n'
                                            #codigo += f'\t{temp3} = {temp2} + 1;\n'
                                            codigo += f'\t{temp4} = Heap[(int){temp3}] ;\n'

                                            codigo += f'\tif ({temp4} != 0 ) goto {etq5};\n'
                                            codigo += f'\tgoto {etq6};\n'

                                            codigo += f'\t{etq5}:\n'
                                            codigo += f'\tHeap[HP] = {temp4};\n'
                                            codigo += f'\tHP = HP +1;\n'

                                            codigo += f'\t{temp3} = {temp3} + 1;\n'
                                            codigo += f'\tgoto {etq7};\n'
                                            codigo += f'\t{etq6}:\n'

                                        if valoid.tipo == t.ENTERO or valoid.tipo == t.DECIMAL:
                                            codigo += f'\tHeap[HP] = {temp2};\n'
                                            codigo += f'\tHP = HP +1;\n'

                                        codigo += f'\tif ({tempAcceso} == 0 ) goto {etq4};\n'
                                        codigo += f'\tHeap[HP] = {ord(",")};\n'
                                        codigo += f'\tHP = HP +1;\n'
                                        codigo += f'\t{etq4}:\n'

                                        codigo += f'\tgoto {etq1};\n'
                                        codigo += f'\t{etq3}:\n'

                                        codigo += f'\tHeap[HP] = {ord("]")};\n'
                                        codigo += f'\tHP = HP +1;\n'

                                    elif isinstance(simbolo, InstanciaVector):
                                        temp1 = controlador.Generador3D.obtenerTemporal()
                                        etq1 = controlador.Generador3D.obtenerEtiqueta()
                                        etq2 = controlador.Generador3D.obtenerEtiqueta()
                                        etq3 = controlador.Generador3D.obtenerEtiqueta()
                                        temp2 = controlador.Generador3D.obtenerTemporal()
                                        etq4 = controlador.Generador3D.obtenerEtiqueta()

                                        codigo += f'\tHeap[HP] = {ord("[")};\n'
                                        codigo += f'\tHP = HP +1;\n'
                                        # si es vector
                                        codigo += f'\t{valoid.temporal} = {valoid.temporal} + 1;\n'
                                        codigo += f'\t{temp1} = {valoid.temporal};\n'
                                        codigo += f'\t{etq1}:\n'
                                        codigo += f'\tif ({tempAcceso} >0 ) goto {etq2};\n'
                                        codigo += f'\tgoto {etq3};\n'

                                        codigo += f'\t{etq2}:\n'
                                        codigo += f'\t{tempAcceso} = {tempAcceso} - 1;\n'

                                        codigo += f'\t{temp1} = {temp1} + 1;\n'
                                        codigo += f'\t{temp2} = Heap[(int){temp1}] ;\n'

                                        temp3 = controlador.Generador3D.obtenerTemporal()
                                        codigo += f'\t{temp3} = Heap[(int){temp2}] ;\n' #obtine tamaio

                                        temp4 = controlador.Generador3D.obtenerTemporal()
                                        codigo += f'\t{temp4} = {temp2} ;\n'

                                        codigo += self.printvect(controlador, temp3, temp4, valoid.tipo)

                                        codigo += f'\tif ({tempAcceso} == 0 ) goto {etq4};\n'
                                        codigo += f'\tHeap[HP] = {ord(",")};\n'
                                        codigo += f'\tHP = HP +1;\n'
                                        codigo += f'\t{etq4}:\n'

                                        codigo += f'\tgoto {etq1};\n'
                                        codigo += f'\t{etq3}:\n'

                                        codigo += f'\tHeap[HP] = {ord("]")};\n'
                                        codigo += f'\tHP = HP +1;\n'



                                    else:
                                        texto_salida += self.addsimbolos(valoid.temporal, valoid.tipo)

                                elif isinstance(self.lista[i], AccesoStruct):
                                    valoid = self.lista[i].Obtener3D(controlador, ts)
                                    codigo += valoid.codigo

                                    tempactual = controlador.Generador3D.obtenerTemporal()
                                    #codigo += f'\t{tempactual} = Heap[(int){valoid.temporal}];\n'
                                    codigo += f'\t{tempactual} = {valoid.temporal};\n'

                                    tempAcceso = controlador.Generador3D.obtenerTemporal()
                                    codigo += f'\t{tempAcceso} = Heap[(int){tempactual}];\n'

                                    temp1 = controlador.Generador3D.obtenerTemporal()
                                    etq1 = controlador.Generador3D.obtenerEtiqueta()
                                    etq2 = controlador.Generador3D.obtenerEtiqueta()
                                    etq3 = controlador.Generador3D.obtenerEtiqueta()
                                    temp2 = controlador.Generador3D.obtenerTemporal()
                                    etq4 = controlador.Generador3D.obtenerEtiqueta()

                                    codigo += f'\tHeap[HP] = {ord("[")};\n'
                                    codigo += f'\tHP = HP +1;\n'

                                    codigo += f'\t{temp1} = {tempactual};\n'

                                    codigo += f'\t{etq1}:\n'
                                    codigo += f'\tif ({tempAcceso} >0 ) goto {etq2};\n'
                                    codigo += f'\tgoto {etq3};\n'

                                    codigo += f'\t{etq2}:\n'
                                    codigo += f'\t{tempAcceso} = {tempAcceso} - 1;\n'

                                    codigo += f'\t{temp1} = {temp1} + 1;\n'
                                    codigo += f'\t{temp2} = Heap[(int){temp1}] ;\n'

                                    if valoid.tipo == t.ENTERO:
                                        codigo += f'\tHeap[HP] = {ord("¥")};\n'
                                        codigo += f'\tHP = HP +1;\n'
                                    elif valoid.tipo == t.DECIMAL:
                                        codigo += f'\tHeap[HP] = {ord("¢")};\n'
                                        codigo += f'\tHP = HP +1;\n'
                                    elif valoid.tipo == t.DIRSTRING or valoid.tipo == t.STRING:
                                        temp3 = controlador.Generador3D.obtenerTemporal()
                                        temp4 = controlador.Generador3D.obtenerTemporal()
                                        etq5 = controlador.Generador3D.obtenerEtiqueta()
                                        etq6 = controlador.Generador3D.obtenerEtiqueta()
                                        etq7 = controlador.Generador3D.obtenerEtiqueta()
                                        codigo += "/*parte strint*/\n"
                                        codigo += f'\t{temp3} = {temp2};\n'
                                        # codigo += f'\t{temp3} = {temp2} - 1;\n'

                                        codigo += f'\t{etq7}:\n'
                                        # codigo += f'\t{temp3} = {temp2} + 1;\n'
                                        codigo += f'\t{temp4} = Heap[(int){temp3}] ;\n'

                                        codigo += f'\tif ({temp4} != 0 ) goto {etq5};\n'
                                        codigo += f'\tgoto {etq6};\n'

                                        codigo += f'\t{etq5}:\n'
                                        codigo += f'\tHeap[HP] = {temp4};\n'
                                        codigo += f'\tHP = HP +1;\n'

                                        codigo += f'\t{temp3} = {temp3} + 1;\n'
                                        codigo += f'\tgoto {etq7};\n'
                                        codigo += f'\t{etq6}:\n'

                                    if valoid.tipo == t.ENTERO or valoid.tipo == t.DECIMAL:
                                        codigo += f'\tHeap[HP] = {temp2};\n'
                                        codigo += f'\tHP = HP +1;\n'

                                    codigo += f'\tif ({tempAcceso} == 0 ) goto {etq4};\n'
                                    codigo += f'\tHeap[HP] = {ord(",")};\n'
                                    codigo += f'\tHP = HP +1;\n'
                                    codigo += f'\t{etq4}:\n'

                                    codigo += f'\tgoto {etq1};\n'
                                    codigo += f'\t{etq3}:\n'

                                    codigo += f'\tHeap[HP] = {ord("]")};\n'
                                    codigo += f'\tHP = HP +1;\n'

                                    print("")

                                else:
                                    # try:
                                    ObtenerRetorno = self.lista[i].Obtener3D(controlador, ts)
                                    codigo += ObtenerRetorno.codigo
                                    # controlador.Generador3D.agregarInstruccion(ObtenerRetorno.codigo)
                                    texto_salida += self.addsimbolos(ObtenerRetorno.temporal, ObtenerRetorno.tipo)

                                # except:
                                #    texto_salida += self.addsimbolos(self.lista[i].valor,self.lista[i].tipo.tipo)
                            except:
                                print("Fallo en: ", self.lista[i])

                    if self.tipo:
                        codigo += f'\tHeap[HP] = 10;\n'
                        codigo += f'\tHP = HP +1;\n'

                    codigo += f'\tHeap[HP] = 0;\n'
                    codigo += f'\tHP = HP +1;\n'
                    codigo += self.CodigofinalV2(retornoPrimero, controlador)
                    return codigo
        else:

            valorexp = self.expresion.Obtener3D(controlador, ts)

            if self.tipo:
                self.expresion.valor += "\n"
                valorexp = self.expresion.Obtener3D(controlador, ts)

            codigo += valorexp.codigo

            temp = controlador.Generador3D.obtenerTemporal()
            caracter = controlador.Generador3D.obtenerTemporal()
            codigo += f'\t{temp}  = {valorexp.temporal};\n'
            etq1 = controlador.Generador3D.obtenerEtiqueta()
            etq2 = controlador.Generador3D.obtenerEtiqueta()

            codigo += f'\t{etq1}: \n'
            codigo += f'\t{caracter} = Heap[(int){temp}]; \n'
            codigo += f'\tif({caracter} == 0) goto {etq2};\n' \
                      f'\tprintf(\"%c\",(char){caracter});\n' \
                      f'\t{temp} = {temp} + 1;\n' \
                      f'\tgoto {etq1};\n' \
                      f'\t{etq2}:\n'
        return codigo
        # controlador.Generador3D.agregarInstruccion(codigo)

    def printvect(self,controlador,tempAcceso,temporal,tipoV):
        codigo = ""
        temp1 = controlador.Generador3D.obtenerTemporal()
        etq1 = controlador.Generador3D.obtenerEtiqueta()
        etq2 = controlador.Generador3D.obtenerEtiqueta()
        etq3 = controlador.Generador3D.obtenerEtiqueta()
        temp2 = controlador.Generador3D.obtenerTemporal()
        etq4 = controlador.Generador3D.obtenerEtiqueta()
        codigo += "/*Parte fun*/\n"
        codigo += f'\tHeap[HP] = {ord("[")};\n'
        codigo += f'\tHP = HP +1;\n'
        #si es vector
        codigo += f'\t{temporal} = {temporal} + 1;\n'
        codigo += f'\t{temp1} = {temporal};\n'
        codigo += f'\t{etq1}:\n'
        codigo += f'\tif ({tempAcceso} >0 ) goto {etq2};\n'
        codigo += f'\tgoto {etq3};\n'

        codigo += f'\t{etq2}:\n'
        codigo += f'\t{tempAcceso} = {tempAcceso} - 1;\n'

        codigo += f'\t{temp1} = {temp1} + 1;\n'
        codigo += f'\t{temp2} = Heap[(int){temp1}] ;\n'

        if tipoV == t.ENTERO:
            codigo += f'\tHeap[HP] = {ord("¥")};\n'
            codigo += f'\tHP = HP +1;\n'
        elif tipoV == t.DECIMAL:
            codigo += f'\tHeap[HP] = {ord("¢")};\n'
            codigo += f'\tHP = HP +1;\n'
        elif tipoV == t.DIRSTRING or tipoV == t.STRING:
            temp3 = controlador.Generador3D.obtenerTemporal()
            temp4 = controlador.Generador3D.obtenerTemporal()
            etq5 = controlador.Generador3D.obtenerEtiqueta()
            etq6 = controlador.Generador3D.obtenerEtiqueta()
            etq7 = controlador.Generador3D.obtenerEtiqueta()
            codigo += "/*parte strint*/\n"
            codigo += f'\t{temp3} = {temp2};\n'
            # codigo += f'\t{temp3} = {temp2} - 1;\n'

            codigo += f'\t{etq7}:\n'
            # codigo += f'\t{temp3} = {temp2} + 1;\n'
            codigo += f'\t{temp4} = Heap[(int){temp3}] ;\n'

            codigo += f'\tif ({temp4} != 0 ) goto {etq5};\n'
            codigo += f'\tgoto {etq6};\n'

            codigo += f'\t{etq5}:\n'
            codigo += f'\tHeap[HP] = {temp4};\n'
            codigo += f'\tHP = HP +1;\n'

            codigo += f'\t{temp3} = {temp3} + 1;\n'
            codigo += f'\tgoto {etq7};\n'
            codigo += f'\t{etq6}:\n'
        if tipoV == t.ENTERO or tipoV == t.DECIMAL:
            codigo += f'\tHeap[HP] = {temp2};\n'
            codigo += f'\tHP = HP +1;\n'

        codigo += f'\tif ({tempAcceso} == 0 ) goto {etq4};\n'
        codigo += f'\tHeap[HP] = {ord(",")};\n'
        codigo += f'\tHP = HP +1;\n'
        codigo += f'\t{etq4}:\n'

        codigo += f'\tgoto {etq1};\n'
        codigo += f'\t{etq3}:\n'

        codigo += f'\tHeap[HP] = {ord("]")};\n'
        codigo += f'\tHP = HP +1;\n'
        codigo += "/*Termina fun*/\n"
        return codigo

    def addsimbolos(self, valor, tipo,validacion = True):
        txt = ""
        if t.ENTERO == tipo or t.USIZE == tipo:
            txt += "¥"
            txt += str(valor)
            txt += "¥"

        elif t.DECIMAL == tipo:
            txt += "¢"
            txt += str(valor)
            txt += "¢"

        elif t.BOOLEANO == tipo:
            txt += "¥"
            txt += str(valor)
            txt += "¥"  # 215×

        elif (t.STRING == tipo or t.DIRSTRING == tipo or t.CARACTER == tipo) and validacion:
            txt += "×"
            txt += str(valor)
            txt += "×"  # 215×

        elif (t.STRING == tipo or t.DIRSTRING == tipo or t.CARACTER == tipo) and not validacion:
            txt += "þ"
            txt += str(valor)
            txt += "þ"  # 215×

        else:
            txt += str(valor)
        return txt

    def Codigofinal(self, retornotype, controlador):
        codigo = "/* Imprimir */\n"
        valorexp = retornotype
        codigo += valorexp.codigo
        temp = controlador.Generador3D.obtenerTemporal()
        caracter = controlador.Generador3D.obtenerTemporal()
        codigo += f'\t{temp}  = {valorexp.temporal};\n'
        etq1 = controlador.Generador3D.obtenerEtiqueta()
        etq2 = controlador.Generador3D.obtenerEtiqueta()
        etq3 = controlador.Generador3D.obtenerEtiqueta()
        etq4 = controlador.Generador3D.obtenerEtiqueta()
        etq5 = controlador.Generador3D.obtenerEtiqueta()

        etq6 = controlador.Generador3D.obtenerEtiqueta()
        temp2 = controlador.Generador3D.obtenerTemporal()
        etq7 = controlador.Generador3D.obtenerEtiqueta()
        etq8 = controlador.Generador3D.obtenerEtiqueta()

        caracterTemp = controlador.Generador3D.obtenerTemporal()

        codigo += f'\t{etq1}: \n'
        codigo += f'\t{caracter} = Heap[(int){temp}]; \n'
        codigo += f'\tif({caracter} == 0) goto {etq2};\n'

        codigo += f'\tif({caracter} == 215) goto {etq6};\n'
        codigo += f'\tif({caracter} == 165) goto {etq3};\n'
        codigo += f'\tif({caracter} == 162) goto {etq4};\n'

        codigo += f'\tprintf(\"%c\",(char){caracter});\n'
        codigo += f'\tgoto {etq5};\n'
        # string----------------
        codigo += f'\t{etq6}:\n'
        codigo += f'\t{temp} = {temp} + 1;\n'
        codigo += f'\t{temp2} = Heap[(int){temp}]; \n'

        codigo += f'\t{etq7}:\n'
        codigo += f'\t{caracterTemp} = Heap[(int){temp2}]; \n'
        codigo += f'\tif ({caracterTemp} != 0) goto {etq8};\n'
        codigo += f'\tgoto {etq5};\n'

        codigo += f'\t{etq8}:\n'
        codigo += f'\tprintf(\"%c\",(char){caracterTemp});\n'
        codigo += f'\t{temp2} = {temp2} + 1;\n'
        codigo += f'\tgoto {etq7};\n'
        # -------------------------
        codigo += f'\t{etq3}:\n' \
                  f'\t{temp} = {temp} + 1;\n' \
                  f'\t{caracter} = Heap[(int){temp}]; \n' \
                  f'\tprintf(\"%d\",(int){caracter});\n'
        codigo += f'\tgoto {etq5};\n'

        codigo += f'\t{etq4}:\n' \
                  f'\t{temp} = {temp} + 1;\n' \
                  f'\t{caracter} = Heap[(int){temp}]; \n' \
                  f'\tprintf(\"%f\",{caracter});\n'

        codigo += f'\t{etq5}:\n'
        codigo += f'\t{temp} = {temp} + 1;\n' \
                  f'\tgoto {etq1};\n' \
                  f'\t{etq2}:\n'

        return codigo
        # controlador.Generador3D.agregarInstruccion(codigo)

    def CodigofinalV2(self, retornotype, controlador):
        codigo = "/* Imprimir */\n"
        valorexp = retornotype
        temp = controlador.Generador3D.obtenerTemporal()
        caracter = controlador.Generador3D.obtenerTemporal()
        codigo += f'\t{temp}  = {valorexp.temporal};\n'
        etq1 = controlador.Generador3D.obtenerEtiqueta()
        etq2 = controlador.Generador3D.obtenerEtiqueta()
        etq3 = controlador.Generador3D.obtenerEtiqueta()
        etq4 = controlador.Generador3D.obtenerEtiqueta()
        etq5 = controlador.Generador3D.obtenerEtiqueta()

        etq6 = controlador.Generador3D.obtenerEtiqueta()
        temp2 = controlador.Generador3D.obtenerTemporal()
        etq7 = controlador.Generador3D.obtenerEtiqueta()
        etq8 = controlador.Generador3D.obtenerEtiqueta()

        caracterTemp = controlador.Generador3D.obtenerTemporal()

        codigo += f'\t{etq1}: \n'
        codigo += f'\t{caracter} = Heap[(int){temp}]; \n'
        codigo += f'\tif({caracter} == 0) goto {etq2};\n'

        codigo += f'\tif({caracter} == 215) goto {etq6};\n'
        codigo += f'\tif({caracter} == 165) goto {etq3};\n'
        codigo += f'\tif({caracter} == 162) goto {etq4};\n'

        codigo += f'\tprintf(\"%c\",(char){caracter});\n'
        codigo += f'\tgoto {etq5};\n'
        # string----------------
        codigo += f'\t{etq6}:\n'
        codigo += f'\t{temp} = {temp} + 1;\n'
        codigo += f'\t{temp2} = Heap[(int){temp}]; \n'

        codigo += f'\t{etq7}:\n'
        codigo += f'\t{caracterTemp} = Heap[(int){temp2}]; \n'
        codigo += f'\tif ({caracterTemp} != 0) goto {etq8};\n'
        codigo += f'\tgoto {etq5};\n'

        codigo += f'\t{etq8}:\n'
        codigo += f'\tprintf(\"%c\",(char){caracterTemp});\n'
        codigo += f'\t{temp2} = {temp2} + 1;\n'
        codigo += f'\tgoto {etq7};\n'
        # -------------------------
        codigo += f'\t{etq3}:\n' \
                  f'\t{temp} = {temp} + 1;\n' \
                  f'\t{caracter} = Heap[(int){temp}]; \n' \
                  f'\tprintf(\"%d\",(int){caracter});\n'
        codigo += f'\tgoto {etq5};\n'

        codigo += f'\t{etq4}:\n' \
                  f'\t{temp} = {temp} + 1;\n' \
                  f'\t{caracter} = Heap[(int){temp}]; \n' \
                  f'\tprintf(\"%f\",{caracter});\n'

        codigo += f'\t{etq5}:\n'
        codigo += f'\t{temp} = {temp} + 1;\n' \
                  f'\tgoto {etq1};\n' \
                  f'\t{etq2}:\n'

        return codigo
        # controlador.Generador3D.agregarInstruccion(codigo)

    def obtenerCadenaUnidaAarray(self, texto, controlador):
        validacion1 = False

        temporal = ""
        codigo = ""
        temp = controlador.Generador3D.obtenerTemporal()
        codigo += f'\t{temp} = HP;\n'

        for caracter in texto:
            estado = 0
            if caracter == '\\' and estado == 0:
                estado = 1
                continue

            if estado == 1:
                if caracter == 'n':
                    codigo += f'\tHeap[HP] = 10;\n'
                    codigo += f'\tHP = HP +1;\n'
                    estado = 0
                    continue

            if (caracter == "¥" or caracter == "¢" or caracter == "×") and not validacion1:
                codigo += f'\tHeap[HP] = {ord(caracter)};\n'
                codigo += f'\tHP = HP +1;\n'
                validacion1 = True
                continue

            if validacion1:
                if caracter == "¥" or caracter == "¢" or caracter == "×":
                    codigo += f'\tHeap[HP] = {temporal};\n'
                    codigo += f'\tHP = HP +1;\n'
                    temporal = ""
                    validacion1 = False
                    continue
                temporal += caracter
                continue

            codigo += f'\tHeap[HP] = {ord(caracter)};\n'
            codigo += f'\tHP = HP +1;\n'

        # codigo += f'\tHeap[HP] = 0;\n'
        # codigo += f'\tHP = HP +1;\n'
        retorno = RetornoType()
        retorno.iniciarRetorno(codigo, None, temp, None)
        return retorno

    def obtenerCadenaUnida(self, texto, controlador):
        validacion1 = False
        validacion2 = False
        temporal = ""
        codigo = ""
        temp = controlador.Generador3D.obtenerTemporal()
        codigo += f'\t{temp} = HP;\n'

        estado = 0
        for caracter in texto:

            if caracter == '\\' and estado == 0:
                estado = 1
                continue

            if estado == 1:
                if caracter == 'n':
                    codigo += f'\tHeap[HP] = 10;\n'
                    codigo += f'\tHP = HP +1;\n'
                    estado = 0
                    continue

            if (caracter == "¥" or caracter == "¢" or caracter == "×") and not validacion1:
                codigo += f'\tHeap[HP] = {ord(caracter)};\n'
                codigo += f'\tHP = HP +1;\n'
                validacion1 = True
                continue

            if validacion1:
                if caracter == "¥" or caracter == "¢" or caracter == "×":
                    codigo += f'\tHeap[HP] = {temporal};\n'
                    codigo += f'\tHP = HP +1;\n'
                    temporal = ""
                    validacion1 = False
                    continue
                temporal += caracter
                continue

            if (caracter == "þ") and not validacion2:
                validacion2 = True
                continue

            if validacion2:
                if caracter == "þ":
                    temp3 = controlador.Generador3D.obtenerTemporal()
                    temp4 = controlador.Generador3D.obtenerTemporal()

                    etq5 = controlador.Generador3D.obtenerEtiqueta()
                    etq6 = controlador.Generador3D.obtenerEtiqueta()
                    etq7 = controlador.Generador3D.obtenerEtiqueta()
                    codigo += "/*parte strint*/\n"
                    codigo += f'\t{temp3} = {temporal};\n'
                    #codigo += f'\t{temp3} = Heap[(int){temp3}] ;\n'

                    codigo += f'\t{etq7}:\n'
                    codigo += f'\t{temp4} = Heap[(int){temp3}] ;\n'

                    codigo += f'\tif ({temp4} != 0 ) goto {etq5};\n'
                    codigo += f'\tgoto {etq6};\n'

                    codigo += f'\t{etq5}:\n'
                    codigo += f'\tHeap[HP] = {temp4};\n'
                    codigo += f'\tHP = HP +1;\n'

                    codigo += f'\t{temp3} = {temp3} + 1;\n'
                    codigo += f'\tgoto {etq7};\n'
                    codigo += f'\t{etq6}:\n'
                    #codigo += f'\tHeap[HP] = {temporal};\n'
                    #codigo += f'\tHP = HP +1;\n'
                    temporal = ""
                    validacion2 = False
                    continue
                temporal += caracter
                continue

            codigo += f'\tHeap[HP] = {ord(caracter)};\n'
            codigo += f'\tHP = HP +1;\n'

        if self.tipo:
            codigo += f'\tHeap[HP] = 10 ;\n'
            codigo += f'\tHP = HP +1;\n'

        codigo += f'\tHeap[HP] = 0;\n'
        codigo += f'\tHP = HP +1;\n'
        retorno = RetornoType()
        retorno.iniciarRetorno(codigo, None, temp, None)
        return retorno

    def ObtenerArrayText(self, array):
        print(type(array))
        text = ""
        if isinstance(array, list):
            text += "["

            bandera = True
            banderaint = len(array)
            aux = 0
            for x in array:
                if isinstance(x, list):
                    text += self.ObtenerArrayText(x)
                    if aux + 1 != banderaint:
                        text += ","

                elif isinstance(x, InstanciaVector):
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
