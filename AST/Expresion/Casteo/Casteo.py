from AST.Abstracto.Expresion import Expresion
from AST.TablaSimbolos.Tipos import tipo, RetornoType


class Casteo(Expresion):

    def __init__(self, expresion, tipo_destino):
        self.expresion = expresion
        self.tipo_destino = tipo_destino

    def ObtenerValor(self, controlador, ts):
        return_exp1: RetornoType = self.expresion.ObtenerValor(controlador, ts)
        valor_exp1 = return_exp1.valor
        tipo_exp1 = return_exp1.tipo

        if tipo_exp1 == tipo.ENTERO:
            if self.tipo_destino == tipo.ENTERO:
                return RetornoType(valor_exp1, tipo.ENTERO)

            elif self.tipo_destino == tipo.DECIMAL:
                return RetornoType(float(valor_exp1), tipo.DECIMAL)

            elif self.tipo_destino == tipo.CARACTER:
                return RetornoType(chr(valor_exp1), tipo.CARACTER)

            elif self.tipo_destino == tipo.USIZE:
                return RetornoType(int(valor_exp1), tipo.USIZE)

        elif tipo_exp1 == tipo.DECIMAL:
            if self.tipo_destino == tipo.ENTERO:
                return RetornoType(int(valor_exp1), tipo.ENTERO)

            elif self.tipo_destino == tipo.DECIMAL:
                return RetornoType(valor_exp1, tipo.DECIMAL)

            elif self.tipo_destino == tipo.USIZE:
                return RetornoType(int(valor_exp1), tipo.USIZE)

        elif tipo_exp1 == tipo.BOOLEANO:

            if self.tipo_destino == tipo.ENTERO:
                if valor_exp1:
                    return RetornoType(1, tipo.ENTERO)
                else:
                    return RetornoType(0, tipo.ENTERO)

            elif self.tipo_destino == tipo.BOOLEANO:
                return RetornoType(valor_exp1, tipo.BOOLEANO)

            elif self.tipo_destino == tipo.USIZE:
                if valor_exp1:
                    return RetornoType(1, tipo.USIZE)
                else:
                    return RetornoType(0, tipo.USIZE)

        elif tipo_exp1 == tipo.CARACTER:
            if self.tipo_destino == tipo.ENTERO:
                return RetornoType(int(ord(valor_exp1)), tipo.ENTERO)

            elif self.tipo_destino == tipo.CARACTER:
                return RetornoType(valor_exp1, tipo.CARACTER)

            if self.tipo_destino == tipo.USIZE:
                return RetornoType(int(ord(valor_exp1)), tipo.USIZE)

        elif tipo_exp1 == tipo.DIRSTRING:
            if self.tipo_destino == tipo.DIRSTRING:
                return RetornoType(valor_exp1, tipo.DIRSTRING)

        elif tipo_exp1 == tipo.STRING:
            if self.tipo_destino == tipo.STRING:
                return RetornoType(valor_exp1, tipo.STRING)

        elif tipo_exp1 == tipo.USIZE:
            if self.tipo_destino == tipo.ENTERO:
                return RetornoType(valor_exp1, tipo.ENTERO)

            elif self.tipo_destino == tipo.DECIMAL:
                return RetornoType(float(valor_exp1), tipo.DECIMAL)

