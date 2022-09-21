from AST.Abstracto.Instruccion import Intruccion
from AST.TablaSimbolos.Tipos import RetornoType,tipo


class Continue(Intruccion):


    def EjecutarInstruccion(self, controlador, ts):
        print(" Se encontro con un continue: ")

        valor_Exp = RetornoType()
        valor_Exp.final = tipo.CONTINUE
        return valor_Exp


