from AST.Abstracto.Expresion import Expresion
from AST.Expresion.Operaciones.Operacion import Operacion, operador
from AST.TablaSimbolos.Tipos import tipo,RetornoType
from AST.Expresion.Nativas.NativasVectores import NativasVectores

class Logica(Operacion, Expresion):
    def __init__(self, exp1, signo, exp2, expU=False):
        super().__init__(exp1, signo, exp2, expU)
        self.etiquetaV = ""
        self.etiquetaF = ""

    def Obtener3D(self, controlador, ts):


        codigo = ""

        if not self.expU:



            if self.operador == operador.AND:
                self.exp1.etiquetaV = controlador.Generador3D.obtenerEtiqueta()
                self.exp1.etiquetaF = self.etiquetaF
                return_exp1: RetornoType = self.exp1.Obtener3D(controlador, ts)
                valor_exp1 = return_exp1.valor

                self.exp2.etiquetaV = self.etiquetaV
                self.exp2.etiquetaF = self.etiquetaF
                return_exp2: RetornoType = self.exp2.Obtener3D(controlador, ts)
                valor_exp2 = return_exp2.valor


                codigo += return_exp1.codigo + "\n"
                codigo += f'\t{return_exp1.etiquetaV}: \n'
                codigo += return_exp2.codigo + "\n"

                retorno = RetornoType(valor_exp1 and valor_exp2,tipo.BOOLEANO)
                retorno.etiquetaV = self.etiquetaV
                retorno.etiquetaF = self.etiquetaF
                retorno.codigo = codigo
                return retorno


            elif self.operador == operador.OR:
                self.exp1.etiquetaV = self.etiquetaV
                self.exp1.etiquetaF = controlador.Generador3D.obtenerEtiqueta()


                return_exp1: RetornoType = self.exp1.Obtener3D(controlador, ts)
                valor_exp1 = return_exp1.valor

                self.exp2.etiquetaV = self.etiquetaV
                self.exp2.etiquetaF = self.etiquetaF
                return_exp2: RetornoType = self.exp2.Obtener3D(controlador, ts)
                valor_exp2 = return_exp2.valor

                codigo += return_exp1.codigo + "\n"
                codigo += f'\t{return_exp1.etiquetaF}: \n'
                codigo += return_exp2.codigo + "\n"

                retorno = RetornoType(valor_exp1 or valor_exp2,tipo.BOOLEANO)
                retorno.etiquetaV = self.etiquetaV
                retorno.etiquetaF = self.etiquetaF
                retorno.codigo = codigo
                return retorno

        else:
            if self.operador == operador.NOT:
                self.exp1.etiquetaV = self.etiquetaF
                self.exp1.etiquetaF = self.etiquetaV

                return_exp1: RetornoType = self.exp1.Obtener3D(controlador, ts)
                tipo_exp1 = return_exp1.tipo
                valor_exp1 = return_exp1.valor

                #if tipo_exp1 == tipo.BOOLEANO:

                codigo += return_exp1.codigo + "\n"

                temporal = ""
                if return_exp1.temporal != "":
                    etq1 = controlador.Generador3D.obtenerEtiqueta()
                    etq2 = controlador.Generador3D.obtenerEtiqueta()
                    etq3 = controlador.Generador3D.obtenerEtiqueta()

                    codigo += f'\tif({return_exp1.temporal} ==0 ) goto {etq1};\n'
                    codigo += f'\tgoto {etq2};\n'

                    codigo += f'\t{etq1}:\n'
                    codigo += f'{return_exp1.temporal} = 1;\n'
                    codigo += f'\tgoto {etq3};\n'

                    codigo += f'\t{etq2}:\n'
                    codigo += f'{return_exp1.temporal} = 0;\n'

                    codigo += f'\t{etq3}:\n'

                    #codigo += f'{return_exp1.temporal} = !{return_exp1.temporal};\n'
                    temporal = return_exp1.temporal

                    if return_exp1.etiqueta == "a":
                        codigo += f'\tif ({return_exp1.temporal}) goto {self.etiquetaV};\n'
                        codigo += f'\tgoto {self.etiquetaF};\n'


                retorno = RetornoType()
                retorno.iniciarRetorno(codigo, "", temporal, tipo_exp1)
                retorno.etiquetaF = self.etiquetaF
                retorno.etiquetaV = self.etiquetaV
                return retorno

