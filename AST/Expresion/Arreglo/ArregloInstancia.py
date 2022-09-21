from AST.Abstracto.Expresion import Expresion
from AST.TablaSimbolos.Tipos import tipo as t
from AST.TablaSimbolos.Tipos import RetornoType
from AST.TablaSimbolos.InstanciaArreglo import InstanciaArreglo

class ArregloInstancia(Expresion):

    def __init__(self, tipo, dimensiones ):
        self.tipo = tipo
        self.dimensiones = dimensiones

    def ObtenerValor(self, controlador,ts) -> RetornoType:

        dimensionesCompiladas:[] = self.obtenerDimensiones(ts)
        dimensionesInt = []
        for retornoType in dimensionesCompiladas:
            dimensionesInt.append(retornoType.valor)
        valores = self.agregarValor(dimensionesCompiladas)

        arreglo = InstanciaArreglo(t.ENTERO, valores, dimensionesInt)
        return RetornoType(arreglo, t.ARRAY)

    def obtenerDimensiones(self, entorno)->[]:

        listaDimensiones = []

        for dim in self.dimensiones:
            valor = dim.obtenerValor(entorno)
            if valor.tipo != t.ENTERO:
                return []

            listaDimensiones.append(valor)

        return listaDimensiones

    def agregarValor(self, dimensionesCompiladas) ->[]:

        anchoNuevo = dimensionesCompiladas.pop(0)
        anchoNuevoInt = anchoNuevo.valor

        valores = []
        if len(dimensionesCompiladas) > 0:

            subArreglo = self.agregarValor(dimensionesCompiladas)
            for i in range(0, anchoNuevoInt):
                valores.insert(i, subArreglo)
        else:
            for i in range(0, anchoNuevoInt):
                valores.insert(i, 50)

        return valores