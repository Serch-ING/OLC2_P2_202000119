from AST.Abstracto.Expresion import Expresion
from AST.Expresion.Operaciones.Operacion import operador, Operacion
from AST.TablaSimbolos.Tipos import tipo,RetornoType
from Analizador.Gramatica import E_list

class Aritmetica(Operacion, Expresion):
    def __init__(self, exp1, signo, exp2, expU=False):
        super().__init__(exp1, signo, exp2, expU)

    def Obtener3D(self, controlador, ts):
        codigo = "/*ARITMETICA*/\n"
        return_exp1: RetornoType = self.exp1.Obtener3D(controlador, ts)
        exp1_temp = return_exp1.temporal
        #valor_exp1 = return_exp1.valor
        codigo += return_exp1.codigo + "\n"
        tipo_exp1 = return_exp1.tipo

        if not self.expU:

            return_exp2: RetornoType = self.exp2.Obtener3D(controlador, ts)
            exp2_temp = return_exp2.temporal
            #valor_exp2 = return_exp2.valor
            codigo += return_exp2.codigo + "\n"

            if self.operador == operador.SUMA:
                codigo += "/*SUMA*/\n"
                temp = controlador.Generador3D.obtenerTemporal()
                codigo += f'\t{temp} = {exp1_temp} + {exp2_temp};\n'
                retorno = RetornoType()
                retorno.iniciarRetorno(codigo,"",temp,tipo_exp1)
                return retorno

            elif self.operador == operador.RESTA:
                codigo += "/*RESTA*/\n"
                temp = controlador.Generador3D.obtenerTemporal()
                codigo += f'\t{temp} = {exp1_temp} - {exp2_temp};\n'
                retorno = RetornoType()
                retorno.iniciarRetorno(codigo, "", temp, tipo_exp1)
                return retorno

            elif self.operador == operador.MULTIPLICACION:
                codigo += "/*MULTIPLICACION*/\n"
                temp = controlador.Generador3D.obtenerTemporal()
                codigo += f'\t{temp} = {exp1_temp} * {exp2_temp};\n'
                retorno = RetornoType()
                retorno.iniciarRetorno(codigo, "", temp, tipo_exp1)
                return retorno

            elif self.operador == operador.DIVISION:
                codigo += "/*DIVISION*/\n"
                temp = controlador.Generador3D.obtenerTemporal()
                codigo += f'\t{temp} = {exp1_temp} / {exp2_temp};\n'
                retorno = RetornoType()
                retorno.iniciarRetorno(codigo, "", temp, tipo_exp1)
                return retorno

            elif self.operador == operador.MOD:
                codigo += "/*MODULO*/\n"
                temp = controlador.Generador3D.obtenerTemporal()
                codigo += f'\t{temp} = (int){exp1_temp} % (int){exp2_temp};\n'
                retorno = RetornoType()
                retorno.iniciarRetorno(codigo, "", temp, tipo_exp1)
                return retorno

            elif self.operador == operador.POT:

                pass

            elif self.operador == operador.POTF:

                pass

        else:

            if self.operador == operador.RESTA:
                codigo += "/*NEGACION*/\n"
                temp = controlador.Generador3D.obtenerTemporal()
                codigo += f'\t{temp} = {exp1_temp} * {-1};\n'
                retorno = RetornoType()
                retorno.iniciarRetorno(codigo, "", temp, tipo_exp1)
                return retorno

                """if isinstance(valor_exp1, int):
                    return RetornoType(int(valor_exp1 * -1), tipo.ENTERO)

                elif isinstance(valor_exp1, float):
                    return RetornoType(float(valor_exp1 * -1), tipo.DECIMAL)

                else:
                    return "No es digito" """

