from AST.Abstracto.Instruccion import Intruccion
from AST.TablaSimbolos.Tipos import RetornoType,tipo
from AST.Instruccion.Declaracion import Declaracion
from AST.Expresion.Identificador import Identificador

class Return(Intruccion):
    def __init__(self, expresion):
        self.expresion = expresion

    def Ejecutar3D(self, controlador, ts):
        print(" Se encontro con un return: ", self.expresion)
        codigo = "/*Return*/\n"
        if self.expresion != None:
            #valor_Exp: RetornoType = self.expresion.Obtener3D(controlador, ts)
            #codigo += valor_Exp.codigo + "\n"

            declaracion = Declaracion(Identificador("return"), self.expresion ,None,False,False)
            declarcionFinal = declaracion.Ejecutar3D(controlador,ts)
            codigo += declarcionFinal
            codigo += "goto SALIR;"

            return codigo

        else:
            valor_Exp = RetornoType()
            valor_Exp.final = tipo.RETURN
            return valor_Exp



