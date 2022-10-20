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
            retorno = RetornoType(instanciaArrayRetorno, t.VECTOR)
            retorno.iniciarRetornoArreglo(codigo, "", "", temp, t.VECTOR, "", listaDimensiones)
            return retorno

        else:
            exp = self.expresiones.Obtener3D(controlador,ts)
            iteracion = self.exp2.Obtener3D(controlador, ts)
            valor= []
            codigo = "/*Vector de vector*/\n"
            codigo+= exp.codigo
            codigo += iteracion.codigo
            temp1 = controlador.Generador3D.obtenerTemporal()
            codigo += f'\t{temp1} = 0;\n'

            tempF = controlador.Generador3D.obtenerTemporal()
            codigo += f'\t{tempF} = HP;\n'

            etq1 = controlador.Generador3D.obtenerEtiqueta()
            etq2 = controlador.Generador3D.obtenerEtiqueta()
            etq3 = controlador.Generador3D.obtenerEtiqueta()

            codigo += f'\tHeap[HP] = {iteracion.temporal};\n'
            codigo += f'HP = HP +1 ;\n'

            codigo += f'\tHeap[HP] = {iteracion.temporal};\n'
            codigo += f'HP = HP +1 ;\n'

            codigo += f'\t{etq1}:\n'
            codigo += f'if ({temp1} < {iteracion.temporal}) goto {etq2};\n'
            codigo += f'goto {etq3};\n'

            codigo += f'\t{etq2}:\n'
            codigo += f'\tHeap[HP] = {exp.temporal};\n'
            codigo += f'HP = HP +1 ;\n'
            codigo += f'\t{temp1} = {temp1} + 1;\n'
            codigo += f'goto {etq1};\n'

            codigo += f'\t{etq3}: /* termino vector de vector*/\n'

            #vectorData = VectorData(valor)
            #retunr_var = vectorData.Obtener3D(controlador, ts)

            retorno = RetornoType()
            retorno.iniciarRetorno(codigo,"",tempF,t.VECTOR)
            return retorno

