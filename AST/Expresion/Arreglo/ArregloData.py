from AST.Abstracto.Expresion import Expresion
from AST.TablaSimbolos.Tipos import  RetornoType
from AST.TablaSimbolos.Tipos import tipo as t
from AST.TablaSimbolos.InstanciaArreglo import InstanciaArreglo

class ArregloData(Expresion):

    def __init__(self,expresiones):
        self.expresiones=expresiones

    def ObtenerValor(self, controlador, ts):
        print("=== Llego a arreglo data")
        tipo = t.UNDEFINED
        expresionesCompiladas = []

        # COMPILAR EXPRESIONES, OBTENER TAMAÑO DE CADA DIMENSION Y VALIDAR CONGRUENCIA DE TIPOS
        for i in range(0, len(self.expresiones)):
            expresion = self.expresiones[i]
            valorExpresion = expresion.ObtenerValor(controlador,ts)

            if i == 0:
                tipo = valorExpresion.tipo
                expresionesCompiladas.append(valorExpresion)
            else:
                if tipo != valorExpresion.tipo:
                    print(f"Los tipos dejaron de coinciddir")
                    return RetornoType()
                else:
                    expresionesCompiladas.append(valorExpresion)

        # ahora creamos la data

        listaDimensiones = []
        valores = []
        listaDimensiones.append(len(expresionesCompiladas))  # TAMAÑO DE LA DIMENSION 1
        tipoFinal = t.UNDEFINED

        for i in range(0, len(expresionesCompiladas)):
            expresionCompilada = expresionesCompiladas[i]

            if expresionCompilada.tipo != t.ARRAY:
                tipoFinal = expresionCompilada.tipo
                valores.append(expresionCompilada.valor)
                continue

            else:
                instanciaArray = expresionCompilada.valor
                if i == 0:
                    tipoFinal = instanciaArray.tipo
                    listaDimensiones.extend(instanciaArray.dimensiones)
                else:
                    if instanciaArray.tipo != tipoFinal: return RetornoType()

                valores.insert(i, instanciaArray.valores)

        instanciaArrayRetorno = InstanciaArreglo(tipoFinal, listaDimensiones, valores)
        return RetornoType(instanciaArrayRetorno, t.ARRAY)

