from enum import Enum

from AST.Abstracto.Expresion import Expresion


class operador(Enum):
    SUMA = 0,
    RESTA = 1,
    MULTIPLICACION = 2,
    DIVISION = 3,
    POT = 4,
    MOD = 5,
    UNARIO = 6,
    IGUALIGUAL = 7,
    DIFERENCIA = 8,
    MENORQUE = 9,
    MAYORQUE = 10,
    MENORIGUAL = 11,
    MAYORIGUAL = 12,
    OR = 13,
    AND = 14,
    NOT = 15,
    POTF = 16,
    Err = 100


class Operacion():

    def __init__(self, exp1, signo, exp2, expU):
        self.exp1 = exp1
        self.exp2 = exp2
        self.expU = expU
        self.signo = signo
        self.operador = self.ObtenerOperador(self.signo)

    def ObtenerOperador(self, signo_operador):
        print("============= Signo valor ", signo_operador)
        if signo_operador == '+':
            return operador.SUMA
        elif signo_operador == '-':
            return operador.RESTA
        elif signo_operador == '*':
            return operador.MULTIPLICACION
        elif signo_operador == '/':
            return operador.DIVISION
        elif signo_operador == '^':
            print("============= Se reconocio potencia normal")
            return operador.POT
        elif signo_operador == '^f':
            print("========== Se reconocio potencia norasdasdsadmal")
            return operador.POTF
        elif signo_operador == '%':
            return operador.MOD
        elif signo_operador == 'UNARIO':
            return operador.UNARIO
        elif signo_operador == '==':
            return operador.IGUALIGUAL
        elif signo_operador == '!=':
            return operador.DIFERENCIA
        elif signo_operador == '<':
            return operador.MENORQUE
        elif signo_operador == '>':
            return operador.MAYORQUE
        elif signo_operador == '<=':
            return operador.MENORIGUAL
        elif signo_operador == '>=':
            return operador.MAYORIGUAL
        elif signo_operador == '||':
            return operador.OR
        elif signo_operador == '&&':
            return operador.AND
        elif signo_operador == '!':
            return operador.NOT
        else:
            return operador.Err
