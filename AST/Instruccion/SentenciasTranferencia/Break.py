from AST.Abstracto.Instruccion import Intruccion
from AST.TablaSimbolos.Tipos import RetornoType,tipo


class Break(Intruccion):
    def __init__(self,  expresion):
        self.expresion = expresion

    def EjecutarInstruccion(self, controlador, ts):
        print(" Se encontro con un break: ",self.expresion)

        if self.expresion != None:
            valor_Exp:RetornoType = self.expresion.ObtenerValor(controlador, ts)
            valor_Exp.final = tipo.BREAK
            return valor_Exp
        else:
            valor_Exp = RetornoType()
            valor_Exp.final = tipo.BREAK
            return valor_Exp


