from AST.Abstracto.Expresion import Expresion
from AST.Expresion.Operaciones.Operacion import Operacion, operador
from AST.TablaSimbolos.Tipos import tipo as t
from AST.TablaSimbolos.Tipos import RetornoType

class Relacional(Operacion, Expresion):

    def __init__(self, exp1, signo, exp2, expU):
        super().__init__(exp1, signo, exp2, expU)

    def Obtener3D(self, controlador, ts):
        return_exp1:RetornoType = self.exp1.Obtener3D(controlador, ts)
        return_exp2:RetornoType = self.exp2.Obtener3D(controlador, ts)

        valor_exp1 = return_exp1.valor
        valor_exp2 = return_exp2.valor

        tipo_exp1 = return_exp1.tipo
        tipo_exp2 = return_exp2.tipo

        temp_exp1 = return_exp1.temporal
        temp_exp2 = return_exp2.temporal

        if self.operador == operador.MAYORIGUAL:
            pass

        elif self.operador == operador.MAYORQUE:

            retorno = RetornoType(valor_exp1 > valor_exp2)
            codigo = return_exp1.codigo
            codigo += return_exp2.codigo
            controlador.Generador3D.agregarInstruccion(codigo)
            retorno.codigo += f'({temp_exp1} > {temp_exp2})'
            return retorno

        elif self.operador == operador.MENORIGUAL:
           pass

        elif self.operador == operador.MENORQUE:
            pass

        elif self.operador == operador.IGUALIGUAL:
            pass

        elif self.operador == operador.DIFERENCIA:
           pass

