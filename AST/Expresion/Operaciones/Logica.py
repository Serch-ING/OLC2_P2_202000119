from AST.Abstracto.Expresion import Expresion
from AST.Expresion.Operaciones.Operacion import Operacion, operador
from AST.TablaSimbolos.Tipos import tipo,RetornoType


class Logica(Operacion, Expresion):
    def __init__(self, exp1, signo, exp2, expU=False):
        super().__init__(exp1, signo, exp2, expU)

    def ObtenerValor(self, controlador, ts):

        return_exp1:RetornoType = self.exp1.ObtenerValor(controlador, ts)
        valor_exp1 = return_exp1.valor
        tipo_exp1 = return_exp1.tipo

        if not self.expU:

            return_exp2: RetornoType = self.exp2.ObtenerValor(controlador, ts)
            valor_exp2 = return_exp2.valor
            tipo_exp2 = return_exp2.tipo

            if self.operador == operador.AND:
                if tipo_exp1 == tipo_exp2 and tipo_exp1 == tipo.BOOLEANO:
                    return RetornoType(valor_exp1 and valor_exp2,tipo.BOOLEANO)

            elif self.operador == operador.OR:
                if tipo_exp1 == tipo_exp2 and tipo_exp1 == tipo.BOOLEANO:
                    return RetornoType(valor_exp1 or valor_exp2, tipo.BOOLEANO)

        else:
            if self.operador == operador.NOT:
                if tipo_exp1 == tipo.BOOLEANO:
                    return RetornoType( not valor_exp1, tipo.BOOLEANO)

