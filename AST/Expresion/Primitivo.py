from AST.Abstracto.Expresion import Expresion
from AST.TablaSimbolos.Tipos import Tipos, RetornoType

class Primitivo(Expresion):

    def __init__(self, valor, tipo) :
        self.valor = valor
        self.tipo = Tipos(tipo)

    def ObtenerValor(self, controlador, ts) -> RetornoType:
        return RetornoType(self.valor,self.tipo.tipo)



