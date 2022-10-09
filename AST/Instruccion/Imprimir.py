from AST.Abstracto.Instruccion import Intruccion
from AST.TablaSimbolos.Tipos import tipo as t
from AST.TablaSimbolos.Tipos import RetornoType
from AST.TablaSimbolos.InstanciaArreglo import InstanciaArreglo
from AST.TablaSimbolos.InstanciaVector import InstanciaVector
from AST.Expresion.Identificador import Identificador
from AST.Expresion.Arreglo.AccesoArreglo import AccesoArreglo
from AST.Expresion.Struct.AccesoStruct import AccesoStruct


class Imprimir(Intruccion):

    def __init__(self, expresion, tipo, lista):
        self.expresion = expresion
        self.tipo = tipo
        self.lista = lista

    def Ejecutar3D(self, controlador, ts):

        codigo = ""

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
                            try:

                                if isinstance(self.lista[i], AccesoArreglo):
                                    array = self.lista[i].ObtenerValor(controlador, ts)

                                    if isinstance(array, RetornoType):
                                        texto_salida += str(array.valor)

                                elif isinstance(self.lista[i], Identificador):
                                    valoid = self.lista[i].Obtener3D(controlador,ts)
                                    codigo += valoid.codigo
                                    texto_salida += self.addsimbolos(valoid.temporal,valoid.tipo)
                                    print("")
                                else:
                                    #try:
                                        ObtenerRetorno =  self.lista[i].Obtener3D(controlador,ts)
                                        codigo += ObtenerRetorno.codigo
                                        #controlador.Generador3D.agregarInstruccion(ObtenerRetorno.codigo)
                                        texto_salida += self.addsimbolos(ObtenerRetorno.temporal , ObtenerRetorno.tipo)

                                    #except:
                                    #    texto_salida += self.addsimbolos(self.lista[i].valor,self.lista[i].tipo.tipo)
                            except:
                                print("Fallo en: ", self.lista[i])

                    retorno = self.obtenerCadenaUnida(texto_salida, controlador)
                    codigo += self.Codigofinal(retorno,controlador)
                    print("Print final: ", texto_salida)
                    return  codigo

            if self.expresion.count("{:?}") > 0:
                print(self.expresion)
                formato_nomal = self.expresion.split("{:?}")
                contador_nomal = self.expresion.count("{:?}")

                if contador_nomal == len(self.lista):

                    for i in range(0, len(formato_nomal)):
                        texto_salida += str(formato_nomal[i])

                        if i <= len(self.lista) - 1:
                            try:

                                if isinstance(self.lista[i], AccesoArreglo):
                                    array = self.lista[i].ObtenerValor(controlador, ts)

                                    if isinstance(array, RetornoType):
                                        texto_salida += str(array.valor)

                                elif isinstance(self.lista[i], Identificador):
                                    valoid = self.lista[i].Obtener3D(controlador,ts)
                                    codigo += valoid.codigo
                                    texto_salida += self.addsimbolos(valoid.temporal,valoid.tipo)
                                    print("")
                                else:
                                    #try:
                                        ObtenerRetorno =  self.lista[i].Obtener3D(controlador,ts)
                                        codigo += ObtenerRetorno.codigo
                                        #controlador.Generador3D.agregarInstruccion(ObtenerRetorno.codigo)
                                        texto_salida += self.addsimbolos(ObtenerRetorno.temporal , ObtenerRetorno.tipo)

                                    #except:
                                    #    texto_salida += self.addsimbolos(self.lista[i].valor,self.lista[i].tipo.tipo)
                            except:
                                print("Fallo en: ", self.lista[i])

                    retorno = self.obtenerCadenaUnida(texto_salida, controlador)
                    codigo += self.Codigofinal(retorno,controlador)
                    print("Print final: ", texto_salida)
                    return  codigo
        else:

            valorexp = self.expresion.Obtener3D(controlador, ts)
            if self.tipo:
                self.expresion.valor +="\n"
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
        #controlador.Generador3D.agregarInstruccion(codigo)

    def addsimbolos(self,valor,tipo):
        txt = ""
        if t.ENTERO == tipo:
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
            txt += "¥"#215×
        elif t.STRING == tipo or t.DIRSTRING == tipo  or t.CARACTER == tipo :
            txt += "×"
            txt += str(valor)
            txt += "×"#215×
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
#string----------------
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
#-------------------------
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
        #controlador.Generador3D.agregarInstruccion(codigo)


    def obtenerCadenaUnida(self, texto, controlador):
        validacion1 = False
        temporal = ""
        codigo = ""
        temp = controlador.Generador3D.obtenerTemporal()
        codigo += f'\t{temp} = HP;\n'

        for caracter in texto:
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
