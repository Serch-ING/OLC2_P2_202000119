from AST.Abstracto.Expresion import Expresion
from AST.TablaSimbolos.Tipos import  RetornoType
from AST.TablaSimbolos.Tipos import tipo as t
from AST.TablaSimbolos.InstanciaArreglo import InstanciaArreglo

class ArregloData(Expresion):

    def __init__(self,expresiones):
        self.expresiones=expresiones

    def Obtener3D(self, controlador, ts):
        print("=== Llego a arreglo data")
        codigo = ""
        tipo = t.UNDEFINED
        expresionesCompiladas = []
        listatemporales = []

        # COMPILAR EXPRESIONES, OBTENER TAMAÑO DE CADA DIMENSION Y VALIDAR CONGRUENCIA DE TIPOS
        for i in range(0, len(self.expresiones)):
            expresion = self.expresiones[i]
            valorExpresion = expresion.Obtener3D(controlador, ts)
            codigo += valorExpresion.codigo
            listatemporales.append(valorExpresion.temporal)
            if i == 0:
                tipo = valorExpresion.tipo
                expresionesCompiladas.append(valorExpresion)
            else:
                if tipo != valorExpresion.tipo:
                    print("Error")
                else:
                    expresionesCompiladas.append(valorExpresion)

        # ahora creamos la data

        listaDimensiones = []
        valores = []
        listaDimensiones.append(len(expresionesCompiladas))  # TAMAÑO DE LA DIMENSION 1
        tipoFinal = t.UNDEFINED

        temp = controlador.Generador3D.obtenerTemporal()


        codigo += f'\t{temp} = HP;\n'
        codigo += f'\tHeap[HP] = {len(expresionesCompiladas)};\n'
        codigo += f'\tHP = HP +1;\n'

        for i in range(0, len(expresionesCompiladas)):
            expresionCompilada = expresionesCompiladas[i]

            if expresionCompilada.tipo != t.ARRAY:
                tipoFinal = expresionCompilada.tipo
                valores.append(expresionCompilada.valor)

                codigo += f'\tHeap[HP] = {listatemporales[i]};\n'
                codigo += f'\tHP = HP +1;\n'
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
        retorno = RetornoType(instanciaArrayRetorno, t.ARRAY)
        retorno.iniciarRetorno(codigo,"",temp,t.ARRAY)

        return retorno

