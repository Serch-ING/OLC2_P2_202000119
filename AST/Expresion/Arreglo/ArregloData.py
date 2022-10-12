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
        codigotemp = ""
        codigotempOtros = ""
        expresionesCompiladas = []
        listatemporales = []

        # COMPILAR EXPRESIONES, OBTENER TAMAÑO DE CADA DIMENSION Y VALIDAR CONGRUENCIA DE TIPOS
        for i in range(0, len(self.expresiones)):
            expresion = self.expresiones[i]
            valorExpresion = expresion.Obtener3D(controlador, ts)

            codigo += valorExpresion.codigo
            codigotempOtros += valorExpresion.codigotemp
            listatemporales.append(valorExpresion.temporal)
            expresionesCompiladas.append(valorExpresion)


        listaDimensiones = []
        valores = []
        listaDimensiones.append(len(expresionesCompiladas))  # TAMAÑO DE LA DIMENSION 1
        tipoFinal = t.UNDEFINED

        temp = controlador.Generador3D.obtenerTemporal()
        codigotemp += f'\t{temp} = HP;\n'
        codigotemp += f'\tHeap[HP] = {len(expresionesCompiladas)};\n'
        codigotemp += f'\tHP = HP +1;\n'

        for i in range(0, len(expresionesCompiladas)):
            expresionCompilada = expresionesCompiladas[i]

            if expresionCompilada.tipo != t.ARRAY:
                tipoFinal = expresionCompilada.tipo
                valores.append(expresionCompilada.valor)
                codigotemp += f'\tHeap[HP] = {listatemporales[i]};\n'
                codigotemp += f'\tHP = HP +1;\n'
                continue
            else:
                instanciaArray = expresionCompilada.valor
                if i == 0:
                    tipoFinal = instanciaArray.tipo
                    listaDimensiones.extend(instanciaArray.dimensiones)
                valores.insert(i, instanciaArray.valores)
                codigotemp += f'\tHeap[HP] = {len(listatemporales)*(i+1)-1*(i+1)} + HP;\n'

                codigotemp += f'\tHP = HP +1;\n'



        if codigotempOtros!= "":
            codigo = codigo + codigotemp + codigotempOtros

        instanciaArrayRetorno = InstanciaArreglo(tipoFinal, listaDimensiones, valores)
        retorno = RetornoType(instanciaArrayRetorno, t.ARRAY)
        retorno.iniciarRetornoArreglo(codigo,codigotemp,"",temp,t.ARRAY)


        return retorno

