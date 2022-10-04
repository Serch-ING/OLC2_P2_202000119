from AST.Abstracto.Expresion import Expresion
from AST.TablaSimbolos.Tipos import Tipos, RetornoType
from AST.TablaSimbolos.Tipos import tipo as ttipo


class Primitivo(Expresion):

    def __init__(self, valor, tipo) :
        self.valor = valor
        self.tipo = Tipos(tipo)

    def Obtener3D(self, controlador, ts) -> RetornoType:

        temp = None
        codigo = ""

        if self.tipo.tipo == ttipo.ENTERO or  self.tipo.tipo == ttipo.DECIMAL:
            temp = controlador.Generador3D.obtenerTemporal()
            codigo = f'\t{temp} = {self.valor};'

        elif self.tipo.tipo != ttipo.STRING or self.tipo.tipo != ttipo.DIRSTRING:

            temp = controlador.Generador3D.obtenerTemporal()
            codigo += f'\t{temp} = HP;\n'

            for caracter in self.valor:

                codigo += f'\tHeap[HP] = {ord(caracter)};\n'
                codigo += f'\tHP = HP +1;\n'

            codigo += f'\tHeap[HP] = 0;\n'
            codigo += f'\tHP = HP +1;\n'

        retorno = RetornoType(self.valor)
        retorno.iniciarRetorno(codigo,None,temp,self.tipo.tipo)
        return retorno



