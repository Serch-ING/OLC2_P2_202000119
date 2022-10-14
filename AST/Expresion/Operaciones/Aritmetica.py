from AST.Abstracto.Expresion import Expresion
from AST.Expresion.Operaciones.Operacion import operador, Operacion
from AST.TablaSimbolos.Tipos import tipo,RetornoType
from Analizador.Gramatica import E_list

class Aritmetica(Operacion, Expresion):
    def __init__(self, exp1, signo, exp2, expU=False):
        super().__init__(exp1, signo, exp2, expU)

    def operacionConcatenar(self, controlador, expresionRetorno):
        codigo = ""

        etiquetaCiclo = controlador.Generador3D.obtenerEtiqueta()
        etiquetaSalida = controlador.Generador3D.obtenerEtiqueta()
        CARACTER = controlador.Generador3D.obtenerTemporal()

        codigo += f'{etiquetaCiclo}: \n'
        codigo += f'{CARACTER} = Heap[(int){expresionRetorno.temporal}];\n'
        codigo += f'if ( {CARACTER} == 0) goto {etiquetaSalida};\n'
        codigo += f'     Heap[HP] = {CARACTER};\n'
        codigo += f'     HP = HP + 1;\n'
        codigo += f'     {expresionRetorno.temporal} = {expresionRetorno.temporal} + 1;\n'
        codigo += f'     goto {etiquetaCiclo};\n'
        codigo += f'{etiquetaSalida}:\n'
        return codigo

    def Obtener3D(self, controlador, ts):
        codigo = "/*ARITMETICA*/\n"
        return_exp1: RetornoType = self.exp1.Obtener3D(controlador, ts)
        exp1_temp = return_exp1.temporal
        valor_exp1 = return_exp1.valor
        codigo += return_exp1.codigo + "\n"
        tipo_exp1 = return_exp1.tipo

        if not self.expU:

            return_exp2: RetornoType = self.exp2.Obtener3D(controlador, ts)
            exp2_temp = return_exp2.temporal
            valor_exp2 = return_exp2.valor
            codigo += return_exp2.codigo + "\n"
            tipo_exp2 = return_exp2.tipo

            if self.operador == operador.SUMA:

                codigo += "/*SUMA*/\n"
                if tipo_exp1 == tipo.STRING and tipo_exp2 == tipo.DIRSTRING:
                    temp = controlador.Generador3D.obtenerTemporal()

                    codigo += f'{temp} = HP;\n'
                    codigo += self.operacionConcatenar(controlador, return_exp1)
                    codigo += self.operacionConcatenar(controlador, return_exp2)
                    codigo += f'Heap[HP] = 0;\n'
                    codigo += f'HP = HP + 1;\n'
                    retorno = RetornoType()
                    retorno.iniciarRetorno(codigo, "", temp, tipo.STRING)
                    return retorno

                else:
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
                codigo += "/*POTENCIA int*/\n"
                etq1 = controlador.Generador3D.obtenerEtiqueta()
                etq2 = controlador.Generador3D.obtenerEtiqueta()
                etq3 = controlador.Generador3D.obtenerEtiqueta()
                temp1 = controlador.Generador3D.obtenerTemporal()
                temp2 = controlador.Generador3D.obtenerTemporal()

                codigo += f'\t{temp1} = {exp1_temp};\n'
                codigo += f'\t{temp2} = 1;\n'
                codigo += f'\t{etq3}:\n'
                codigo += f'\tif ({temp2} != {exp2_temp}) goto {etq1};\n'
                codigo += f'\tgoto {etq2};\n'
                codigo += f'\t{etq1}:\n'
                codigo += f'\t{temp1} = {temp1} * {exp1_temp};\n'
                codigo += f'\t{temp2} = {temp2} + {1};\n'
                codigo += f'\tgoto {etq3};\n'
                codigo += f'\t{etq2}:\n'
                retorno = RetornoType()
                retorno.iniciarRetorno(codigo, "", temp1, tipo_exp1)
                return retorno

            elif self.operador == operador.POTF:
                codigo += "/*POTENCIA float*/\n"
                etq1 = controlador.Generador3D.obtenerEtiqueta()
                etq2 = controlador.Generador3D.obtenerEtiqueta()
                etq3 = controlador.Generador3D.obtenerEtiqueta()
                temp1 = controlador.Generador3D.obtenerTemporal()
                temp2 = controlador.Generador3D.obtenerTemporal()

                codigo += f'\t{temp1} = (int){exp1_temp};\n'
                codigo += f'\t{temp2} = 1;\n'
                codigo += f'\t{etq3}:\n'
                codigo += f'\tif ({temp2} != (int){exp2_temp}) goto {etq1};\n'
                codigo += f'\tgoto {etq2};\n'
                codigo += f'\t{etq1}:\n'
                codigo += f'\t{temp1} = {temp1} * (int){exp1_temp};\n'
                codigo += f'\t{temp2} = {temp2} + {1};\n'
                codigo += f'\tgoto {etq3};\n'
                codigo += f'\t{etq2}:\n'
                retorno = RetornoType()
                retorno.iniciarRetorno(codigo, "", temp1, tipo_exp1)
                return retorno

        else:

            if self.operador == operador.RESTA:
                codigo += "/*NEGACION*/\n"
                temp = controlador.Generador3D.obtenerTemporal()
                codigo += f'\t{temp} = {exp1_temp} * {-1};\n'
                retorno = RetornoType(valor_exp1 * -1)
                retorno.iniciarRetorno(codigo, "", temp, tipo_exp1)
                return retorno

                """if isinstance(valor_exp1, int):
                    return RetornoType(int(valor_exp1 * -1), tipo.ENTERO)

                elif isinstance(valor_exp1, float):
                    return RetornoType(float(valor_exp1 * -1), tipo.DECIMAL)

                else:
                    return "No es digito" """

