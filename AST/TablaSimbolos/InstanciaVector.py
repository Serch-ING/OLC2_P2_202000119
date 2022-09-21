from AST.TablaSimbolos.Simbolos import Simbolos

class InstanciaVector(Simbolos):

    def __init__(self,tipo, dimensiones, valores:[]):
        super().__init__()
        super().iniciarSimboloVector(tipo,dimensiones, valores)

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

    def ObtenerValor(self, listaDimensiones, index, valores):

        indiceDimension:int = listaDimensiones.pop(0)
        tamanoDimension:int = self.dimensiones

        if len(listaDimensiones) > 0:



            subArreglo = valores[indiceDimension]
            return self.ObtenerValor(listaDimensiones, index+1, subArreglo)

        else:
            if isinstance(valores,InstanciaVector):
                return valores.valores[indiceDimension]

            return valores[indiceDimension]

