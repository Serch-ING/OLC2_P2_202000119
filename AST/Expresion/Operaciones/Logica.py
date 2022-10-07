from AST.Abstracto.Expresion import Expresion
from AST.Expresion.Operaciones.Operacion import Operacion, operador
from AST.TablaSimbolos.Tipos import tipo,RetornoType


class Logica(Operacion, Expresion):
    def __init__(self, exp1, signo, exp2, expU=False):
        super().__init__(exp1, signo, exp2, expU)

    def Obtener3D(self, controlador, ts):

        return_exp1:RetornoType = self.exp1.Obtener3D(controlador, ts)
        tipo_exp1 = return_exp1.tipo
        exp1_temp = return_exp1.temporal


        if not self.expU:

            return_exp2: RetornoType = self.exp2.Obtener3D(controlador, ts)
            #valor_exp2 = return_exp2.valor
            #tipo_exp2 = return_exp2.tipo

            if self.operador == operador.AND:
                pass
                #if tipo_exp1 == tipo_exp2 and tipo_exp1 == tipo.BOOLEANO:
                #    return RetornoType(valor_exp1 and valor_exp2,tipo.BOOLEANO)

            elif self.operador == operador.OR:
                pass
                #if tipo_exp1 == tipo_exp2 and tipo_exp1 == tipo.BOOLEANO:
                #    return RetornoType(valor_exp1 or valor_exp2, tipo.BOOLEANO)

        else:
            if self.operador == operador.NOT:
                if tipo_exp1 == tipo.BOOLEANO:
                    codigo = "/*NOT*/\n"
                    temp1 = controlador.Generador3D.obtenerTemporal()
                    etq1 = controlador.Generador3D.obtenerEtiqueta()
                    etq2 = controlador.Generador3D.obtenerEtiqueta()
                    etq3 = controlador.Generador3D.obtenerEtiqueta()
                    codigo += f'\tif ({exp1_temp} == {1}) goto {etq1};\n'
                    codigo += f'\tgoto {etq2};\n'
                    codigo += f'\t{etq1}:\n'
                    codigo += f'\t{temp1} = 0;\n'
                    codigo += f'\tgoto {etq3};\n'
                    codigo += f'\t{etq2}:\n'
                    codigo += f'\t{temp1} = 1;\n'
                    codigo += f'\t{etq3}:\n'

                    retorno = RetornoType()
                    retorno.iniciarRetorno(codigo, "", temp1, tipo_exp1)
                    return retorno

