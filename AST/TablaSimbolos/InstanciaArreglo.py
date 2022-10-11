from AST.TablaSimbolos.Simbolos import Simbolos
from AST.TablaSimbolos.Tipos import RetornoType
class InstanciaArreglo(Simbolos):

    def __init__(self,tipo, dimensiones, valores:[]):
        super().__init__()
        super().iniciarSimboloArreglo(tipo,dimensiones, valores)

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

    def Obtener3D(self, listaDimensiones, index, valores,direccion,controlador):
        codigo = ""
        indiceDimension:int = listaDimensiones.pop(0)
        tamanoDimension:int = self.dimensiones[index]

        if len(listaDimensiones) > 0:

            if indiceDimension > (tamanoDimension-1):
                return None

            else:

                subArreglo = valores[indiceDimension]
                #return self.Obtener3D(listaDimensiones, index+1, subArreglo)
                return ""

        else:
            if indiceDimension > (tamanoDimension-1):
                return None
            else:
                temp1 = controlador.Generador3D.obtenerTemporal()
                temp2 = controlador.Generador3D.obtenerTemporal()
                temp3 = controlador.Generador3D.obtenerTemporal()
                temp4 = controlador.Generador3D.obtenerTemporal()

                codigo += f'\t{temp1} = SP + {direccion};\n'
                codigo += f'\t{temp2} = Stack[(int){temp1}];\n'
                codigo += f'\t{temp3} = {temp2} + {indiceDimension+1};\n'
                codigo += f'\t{temp4} = Heap[(int){temp3}];\n'
                retorno = RetornoType(valores[indiceDimension])
                retorno.iniciarRetorno(codigo,"",temp4,"")
                #return valores[indiceDimension]
                return retorno

