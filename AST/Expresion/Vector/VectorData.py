from AST.Abstracto.Expresion import Expresion
from AST.TablaSimbolos.Tipos import  RetornoType
from AST.TablaSimbolos.Tipos import tipo as t
from AST.TablaSimbolos.InstanciaVector import InstanciaVector

class VectorData(Expresion):

    def __init__(self,expresiones,exp2=None):
        self.expresiones=expresiones
        self.exp2 = exp2

    def Obtener3D(self, controlador, ts):
        print("=== Llego a vector data")
        if self.exp2 is None:
            print("=== Llego a arreglo data")
            codigo = ""
            codigotemp = ""
            codigotempOtros = ""
            expresionesCompiladas = []
            listatemporales = []

            # COMPILAR EXPRESIONES, OBTENER TAMAÑO DE CADA DIMENSION Y VALIDAR CONGRUENCIA DE TIPOS
            for i in range(0, len(self.expresiones)):
                expresion = self.expresiones[i]
                valorExpresion = expresion.Obtener3D(controlador, ts)
                codigo += valorExpresion.codigo

                listatemporales.append(valorExpresion.temporal)
                expresionesCompiladas.append(valorExpresion)

            listaDimensiones = []
            valores = []
            listaDimensiones.append(len(expresionesCompiladas))  # TAMAÑO DE LA DIMENSION 1
            tipoFinal = t.UNDEFINED

            temp = controlador.Generador3D.obtenerTemporal()
            codigo += f'\t{temp} = HP;\n'
            codigo += f'\tHeap[HP] = {len(expresionesCompiladas)};\n'
            codigo += f'\tHP = HP +1;\n'
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
                    valores.insert(i, instanciaArray.valores)

                    if i == 0:
                        tipoFinal = instanciaArray.tipo
                        listaDimensiones.extend(instanciaArray.dimensiones)
                        codigo += f'\tHeap[HP] = {len(listatemporales) * (i + 1) - 1 * (i + 1)} + {(i + 1)};\n'
                    else:
                        factor = (len(listatemporales) - (i))

                        resultado = 1
                        for x in expresionCompilada.dimensiones:
                            resultado *= x

                        if len(expresionCompilada.dimensiones) > 1:
                            resultado += expresionCompilada.dimensiones[len(expresionCompilada.dimensiones) - 1] + 1

                        codigo += f'\tHeap[HP] =   {(resultado + 1) * (listaDimensiones[0] - factor) + factor};\n'

                    codigo += f'\tHP = HP +1;\n'

            instanciaArrayRetorno = InstanciaVector(tipoFinal, listaDimensiones, valores)
            retorno = RetornoType(instanciaArrayRetorno, t.ARRAY)
            retorno.iniciarRetornoArreglo(codigo, "", "", temp, t.ARRAY, "", listaDimensiones)
            return retorno

        else:
            valor= []
            for i in range (0,self.exp2.valor):
                valor.append(self.expresiones)

            vectorData = VectorData(valor)
            retunr_var = vectorData.Obtener3D(controlador, ts)
            return retunr_var

