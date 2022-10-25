from AST.Abstracto.Expresion import Expresion
from AST.TablaSimbolos.Tipos import RetornoType,tipo
from AST.Expresion.Arreglo import ArregloData
from AST.TablaSimbolos.InstanciaArreglo import InstanciaArreglo
class Repeticiones(Expresion):
    def __init__(self,valor,numero,tipo = False):
        self.valor=valor
        self.numero=numero
        self.tipo =tipo

    def Obtener3D(self, controlador, ts):
        if not self.tipo:
            codigo = "/*repeticiones*/\n"
            valor: RetornoType = self.valor.Obtener3D(controlador, ts)
            numero: RetornoType = self.numero.Obtener3D(controlador, ts)

            codigo += valor.codigo
            codigo += numero.codigo

            temp1 = controlador.Generador3D.obtenerTemporal()
            etq1 = controlador.Generador3D.obtenerEtiqueta()
            etq2 = controlador.Generador3D.obtenerEtiqueta()
            etq3 = controlador.Generador3D.obtenerEtiqueta()
            temp2 = controlador.Generador3D.obtenerTemporal()

            codigo += f'\t{temp1} = 0;\n'
            codigo += f'\t{temp2} = HP;\n'
            codigo += f'\tHeap[(int)HP] = {numero.temporal};\n'
            codigo += f'\tHP = HP + 1;\n'

            codigo += f'\t{etq1}:\n'
            codigo += f'\tif({temp1} < {numero.temporal}) goto {etq2};\n'
            codigo += f'\tgoto {etq3};\n'

            codigo += f'\t{etq2}:\n'
            codigo += f'\tHeap[(int)HP] = {valor.temporal};\n'
            codigo += f'\tHP = HP + 1;\n'
            codigo += f'\t{temp1} = {temp1} + 1;\n'
            codigo += f'\tgoto {etq1};\n'

            codigo += f'\t{etq3}:\n'

            retorno = RetornoType()
            retorno.iniciarRetorno(codigo,"",temp2,valor.tipo)

            return retorno
        else:
            return RetornoType( self.valor, tipo.ARRAY)