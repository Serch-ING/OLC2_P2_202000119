from AST.TablaSimbolos.Simbolos import Simbolos
from AST.TablaSimbolos.Tipos import RetornoType
from AST.TablaSimbolos.Tipos import tipo

class InstanciaVector(Simbolos):

    def __init__(self,tipo, dimensiones, valores:[]):
        super().__init__()
        super().iniciarSimboloVector(tipo,dimensiones, valores)
        self.objeto = None

    def SetValor(self, listaDimensiones, index, valores, dato_new):

        indiceDimension:int = listaDimensiones.pop(0)
        tamanoDimension:int = self.dimensiones[index]

        if len(listaDimensiones) > 0:

            if indiceDimension > (tamanoDimension-1):
                return

            else:
                subArreglo = valores[indiceDimension]
                self.SetValor(listaDimensiones, index+1, subArreglo, dato_new)

        else:
            if indiceDimension > (tamanoDimension-1):
                return
            else:
              if type( valores[indiceDimension]) == type(dato_new):

                  valores[indiceDimension] = dato_new

    def peek_stack(self, stack):
        if stack:
            return stack[-1]  # this will get the last element of stack
        else:
            return None


    def ObtenerValor(self, direccion, controlador, listatemporales, esreferencia):

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

        temp4 = ""

        while self.peek_stack(listatemporales) is not None:
            temp3 = controlador.Generador3D.obtenerTemporal()
            codigo += f'\t{temp3} = {temp2} + {listatemporales[0]};\n'
            codigo += f'\t{temp3} = {temp3} +  2;\n'

            listatemporales.remove(listatemporales[0])

            temp4 = controlador.Generador3D.obtenerTemporal()
            codigo += f'\t{temp4} = Heap[(int){temp3}];\n'

            codigo += f'\t{temp2} = {temp4};\n'
            #codigo += f'\t{temp2} = {temp3} + {temp4};\n'

        # codigo += f'\t{temp4} = Heap[(int){temp2}];\n'

        retorno = RetornoType()
        retorno.iniciarRetorno(codigo, "", temp2,"")

        # valor = self.ciclo(listaDimensiones, index, valores, direccion, controlador)
        return retorno

    def ObtenerValorV2(self, direccion, controlador, listatemporales, esreferencia):

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

        temp4 = ""

        while self.peek_stack(listatemporales) is not None:
            temp3 = controlador.Generador3D.obtenerTemporal()
            codigo += f'\t{temp3} = {temp2} + {listatemporales[0]};\n'
            codigo += f'\t{temp3} = {temp3} +  2;\n'
            listatemporales.remove(listatemporales[0])

            temp4 = controlador.Generador3D.obtenerTemporal()
            codigo += f'\t{temp2} = Heap[(int){temp3}];\n'

            #codigo += f'\t{temp4} = Heap[(int){temp3}];\n'

            #if self.peek_stack(listatemporales) is not None:
            #    temp5 = controlador.Generador3D.obtenerTemporal()
            #    codigo += f'\t{temp5} = {temp4} + 2;\n'
            #    codigo += f'\t{temp2} = Heap[(int){temp5}];\n'


        retorno = RetornoType()
        retorno.iniciarRetorno(codigo, "", temp2,"")

        return retorno


