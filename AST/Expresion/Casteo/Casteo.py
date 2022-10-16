from AST.Abstracto.Expresion import Expresion
from AST.TablaSimbolos.Tipos import tipo, RetornoType


class Casteo(Expresion):

    def __init__(self, expresion, tipo_destino):
        self.expresion = expresion
        self.tipo_destino = tipo_destino

    def Obtener3D(self, controlador, ts):
        codigo = "/*Casteo*/\n"
        return_exp1: RetornoType = self.expresion.Obtener3D(controlador, ts)
        valor_exp1 = return_exp1.valor
        tipo_exp1 = return_exp1.tipo

        if tipo_exp1 == tipo.ENTERO:
            if self.tipo_destino == tipo.ENTERO:
                codigo += return_exp1.codigo + "\n"
                codigo += f'{return_exp1.temporal} = (int){return_exp1.temporal};\n'
                retorno = RetornoType()
                retorno.iniciarRetorno(codigo, "", return_exp1.temporal, tipo.DECIMAL)
                return retorno

            elif self.tipo_destino == tipo.DECIMAL:
                codigo += return_exp1.codigo + "\n"
                codigo += f'{return_exp1.temporal} = (float){return_exp1.temporal};\n'
                retorno = RetornoType()
                retorno.iniciarRetorno(codigo,"",return_exp1.temporal,tipo.DECIMAL)
                return retorno

            elif self.tipo_destino == tipo.CARACTER:
                codigo += return_exp1.codigo + "\n"
                codigo += f'{return_exp1.temporal} = (char){return_exp1.temporal};\n'
                retorno = RetornoType()
                retorno.iniciarRetorno(codigo, "", return_exp1.temporal, tipo.DECIMAL)
                return retorno

            elif self.tipo_destino == tipo.USIZE:
                codigo += return_exp1.codigo + "\n"
                codigo += f'{return_exp1.temporal} = (int){return_exp1.temporal};\n'
                retorno = RetornoType()
                retorno.iniciarRetorno(codigo, "", return_exp1.temporal, tipo.DECIMAL)
                return retorno

        elif tipo_exp1 == tipo.DECIMAL:
            if self.tipo_destino == tipo.ENTERO:
                codigo += return_exp1.codigo + "\n"
                codigo += f'{return_exp1.temporal} = (int){return_exp1.temporal};\n'
                retorno = RetornoType()
                retorno.iniciarRetorno(codigo, "", return_exp1.temporal, tipo.DECIMAL)
                return retorno

            elif self.tipo_destino == tipo.DECIMAL:
                codigo += return_exp1.codigo + "\n"
                codigo += f'{return_exp1.temporal} = (float){return_exp1.temporal};\n'
                retorno = RetornoType()
                retorno.iniciarRetorno(codigo, "", return_exp1.temporal, tipo.DECIMAL)
                return retorno

            elif self.tipo_destino == tipo.USIZE:
                codigo += return_exp1.codigo + "\n"
                codigo += f'{return_exp1.temporal} = (int){return_exp1.temporal};\n'
                retorno = RetornoType()
                retorno.iniciarRetorno(codigo, "", return_exp1.temporal, tipo.DECIMAL)
                return retorno

        elif tipo_exp1 == tipo.BOOLEANO:

            if self.tipo_destino == tipo.ENTERO:
                if valor_exp1:
                    codigo += return_exp1.codigo + "\n"
                    codigo += f'{return_exp1.temporal} = 1;\n'
                    retorno = RetornoType()
                    retorno.iniciarRetorno(codigo, "", return_exp1.temporal, tipo.DECIMAL)
                    return retorno
                else:
                    codigo += return_exp1.codigo + "\n"
                    codigo += f'{return_exp1.temporal} = 0;\n'
                    retorno = RetornoType()
                    retorno.iniciarRetorno(codigo, "", return_exp1.temporal, tipo.DECIMAL)
                    return retorno

            elif self.tipo_destino == tipo.BOOLEANO:
                codigo += return_exp1.codigo + "\n"
                retorno = RetornoType()
                retorno.iniciarRetorno(codigo, "", return_exp1.temporal, tipo.DECIMAL)
                return retorno

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

