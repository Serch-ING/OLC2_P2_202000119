from AST.TablaSimbolos.Simbolos import Simbolos
from AST.TablaSimbolos.Tipos import RetornoType




class InstanciaArreglo(Simbolos):

    def __init__(self,tipo, dimensiones, valores:[]):
        super().__init__()
        super().iniciarSimboloArreglo(tipo,dimensiones, valores)
        self.varImprimir = None

    def SetValor(self,direccion,controlador,listatemporales,esreferencia):
        codigo = ""

        temp1 = controlador.Generador3D.obtenerTemporal()
        temp2 = controlador.Generador3D.obtenerTemporal()

        if not esreferencia.referencia:
            codigo += f'\t{temp1} = SP + {direccion};\n'
            codigo += f'\t{temp2} = Stack[(int){temp1}];\n'
        else:
            codigo += f'\t{temp2} = SP + {esreferencia.direccion};\n'
            codigo += f'\t{temp2} = Stack[(int){temp2}];\n'
            while esreferencia.referencia:
                codigo += f'\t{temp2} = Stack[(int){temp2}];\n'
                esreferencia = esreferencia.tsproviene.ObtenerSimbolo(esreferencia.idproviene)


        temp3 = ""


        while self.peek_stack(listatemporales) is not None:
            temp3 = controlador.Generador3D.obtenerTemporal()
            codigo += f'\t{temp3} = {temp2} + {listatemporales[0]};\n'
            codigo += f'\t{temp3} = {temp3} +  1;\n'
            listatemporales.remove(listatemporales[0])

            if self.peek_stack(listatemporales) is not None:
                temp4 = controlador.Generador3D.obtenerTemporal()
                codigo += f'\t{temp4} = Heap[(int){temp3}];\n'
                codigo += f'\t{temp2} = {temp3} + {temp4};\n'

        retorno = RetornoType()
        retorno.iniciarRetorno(codigo, "", temp3, "")

        # valor = self.ciclo(listaDimensiones, index, valores, direccion, controlador)
        return retorno


    def peek_stack(self,stack):
        if stack:
            return stack[-1]  # this will get the last element of stack
        else:
            return None

    def Obtener3D(self, direccion,controlador,listatemporales,esreferencia,ts):

        codigo = ""

        temp1 = controlador.Generador3D.obtenerTemporal()
        temp2 = controlador.Generador3D.obtenerTemporal()

        if not esreferencia.referencia:
            codigo += f'\t{temp1} = SP + {direccion};\n'
            codigo += f'\t{temp2} = Stack[(int){temp1}];\n'
        else:
            codigo += f'\t{temp2} = SP + {esreferencia.direccion};\n'
            codigo += f'\t{temp2} = Stack[(int){temp2}];\n'
            while esreferencia.referencia:
                codigo += f'\t{temp2} = Stack[(int){temp2}];\n'
                esreferencia = esreferencia.tsproviene.ObtenerSimbolo(esreferencia.idproviene)

        temp4=""

        size = controlador.Generador3D.obtenerTemporal()
        codigo += f'\t{size} = Heap[(int){temp2}];\n'

        primeravex= True
        etq1 = controlador.Generador3D.obtenerEtiqueta()
        etq2 = controlador.Generador3D.obtenerEtiqueta()
        etq3 = controlador.Generador3D.obtenerEtiqueta()


        while self.peek_stack(listatemporales) is not None:
            temp3 = controlador.Generador3D.obtenerTemporal()
            tempooo = listatemporales[0]
            codigo += f'\t{temp3} = {temp2} + {listatemporales[0]};\n'
            codigo += f'\t{temp3} = {temp3} +  1;\n'
            listatemporales.remove(listatemporales[0])

            if primeravex and self.varImprimir is not None:
                primeravex = False
                codigo += f'\tif({tempooo} < {size}) goto {etq1};\n'
                codigo += f'\tgoto {etq2};\n'

                codigo += f'\t{etq1}:\n'
                codigo += f'\tif({tempooo} < 0) goto {etq2};\n'

            temp4 = controlador.Generador3D.obtenerTemporal()
            codigo += f'\t{temp4} = Heap[(int){temp3}];\n'

            if self.peek_stack(listatemporales) is not None:
                codigo += f'\t{temp2} = {temp3} + {temp4};\n'

        if self.varImprimir is not None:
            codigo += f'\tgoto {etq3};\n'
            codigo += f'\t{etq2}:\n'
            exp = self.varImprimir.Ejecutar3D(controlador, ts)
            codigo += exp
            codigo += f'\t{etq3}:\n'

        retorno = RetornoType()
        retorno.iniciarRetorno(codigo,"",temp4,"")

        #valor = self.ciclo(listaDimensiones, index, valores, direccion, controlador)
        return retorno

    def Obtener3DV2(self,direccion,controlador,listatemporales,esreferencia):

        codigo = ""

        temp1 = controlador.Generador3D.obtenerTemporal()
        temp2 = controlador.Generador3D.obtenerTemporal()

        if not esreferencia.referencia:
            codigo += f'\t{temp1} = SP + {direccion};\n'
            codigo += f'\t{temp2} = Stack[(int){temp1}];\n'
        else:
            codigo += f'\t{temp2} = SP + {esreferencia.direccion};\n'
            codigo += f'\t{temp2} = Stack[(int){temp2}];\n'
            while esreferencia.referencia:
                codigo += f'\t{temp2} = Stack[(int){temp2}];\n'
                esreferencia = esreferencia.tsproviene.ObtenerSimbolo(esreferencia.idproviene)

        temp4=""

        while self.peek_stack(listatemporales) is not None:
            temp3 = controlador.Generador3D.obtenerTemporal()
            codigo += f'\t{temp3} = {temp2} + {listatemporales[0]};\n'
            codigo += f'\t{temp3} = {temp3} +  1;\n'
            listatemporales.remove(listatemporales[0])

            temp4 = controlador.Generador3D.obtenerTemporal()
            codigo += f'\t{temp4} = Heap[(int){temp3}];\n'

            codigo += f'\t{temp2} = {temp3} + {temp4};\n'

        #codigo += f'\t{temp4} = Heap[(int){temp2}];\n'


        retorno = RetornoType()
        retorno.iniciarRetorno(codigo,"",temp2,"")

        #valor = self.ciclo(listaDimensiones, index, valores, direccion, controlador)
        return retorno


    def ciclo(self,listaDimensiones, index, valores,direccion,controlador):
        codigo = ""
        indiceDimension: int = listaDimensiones.pop(0)
        tamanoDimension: int = self.dimensiones[index]

        if len(listaDimensiones) > 0:

            subArreglo = valores[indiceDimension]
            return self.Obtener3D(listaDimensiones, index + 1, subArreglo, direccion, controlador)

        else:

            temp1 = controlador.Generador3D.obtenerTemporal()
            temp2 = controlador.Generador3D.obtenerTemporal()
            temp3 = controlador.Generador3D.obtenerTemporal()

            codigo += f'\t{temp1} = SP + {direccion};\n'
            codigo += f'\t{temp2} = Stack[(int){temp1}];\n'
            codigo += f'\t{temp2} = {temp2} + 1;\n'
            codigo += f'\t{temp3} = Heap[(int){temp2}];\n'
            retorno = RetornoType(valores[indiceDimension])
            retorno.iniciarRetorno(codigo, "", temp3, "")

            return retorno



