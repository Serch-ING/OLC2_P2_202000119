from AST.Abstracto.Instruccion import Intruccion
from AST.TablaSimbolos.Tipos import RetornoType,tipo
from AST.Instruccion.Declaracion import Declaracion
from AST.Expresion.Identificador import Identificador
from AST.Instruccion.Asignacion import Asignacion
class Return(Intruccion):
    def __init__(self, expresion):
        self.expresion = expresion

    def Ejecutar3D(self, controlador, ts):
        print(" Se encontro con un return: ", self.expresion)
        codigo = "/*Return*/\n"

        if self.expresion != None:
            #expvalor:RetornoType = self.expresion.Obtener3D(controlador,ts)
            #codigo += expvalor.codigo

            asignacion = Asignacion("return",self.expresion)
            asignacion = asignacion.Ejecutar3D(controlador,ts)
            codigo += asignacion
            #tstemporal = ts
            #if tstemporal.padre.name != "Main":
            #    tstemporal = tstemporal.padre

            #temporal = "t" + tstemporal.name

            #codigo += f'\tStack[(int){temporal}]= {expvalor.temporal};\n'
            codigo += "goto SALIR;"
            return codigo

        else:
            valor_Exp = RetornoType()
            valor_Exp.final = tipo.RETURN
            return valor_Exp



