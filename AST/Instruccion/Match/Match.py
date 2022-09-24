from AST.Abstracto.Instruccion import Intruccion
from AST.Abstracto.Expresion import Expresion
from AST.TablaSimbolos.Tipos import RetornoType
class Match(Intruccion,Expresion):
    def __init__(self, expresion, matches):
        self.expresion = expresion
        self.matches = matches

    def Obtener3D(self, controlador, ts):
        return_exp: RetornoType = self.expresion.Obtener3D(controlador, ts)
        valor_Exp = return_exp.valor
        tipo_Exp = return_exp.tipo

        print("== -Match Expresiones- ==")
        print("varible: ", self.expresion)
        print(" valor: ", valor_Exp, " tipo: ", tipo_Exp)

        for match in self.matches:
            print("match: ", match)

            for validation in match.matches:
                if validation != '_':
                    return_validacion: RetornoType = validation.Obtener3D(controlador, ts)
                    valor_v = return_validacion.valor
                    tipo_v = return_validacion.tipo
                    if valor_Exp == valor_v and tipo_Exp == tipo_v:
                        return match.Obtener3D(controlador, ts)
                else:
                    return match.Obtener3D(controlador, ts)

    def Ejecutar3D(self, controlador, ts):
        return_exp: RetornoType = self.expresion.Obtener3D(controlador, ts)
        valor_Exp = return_exp.valor
        tipo_Exp = return_exp.tipo

        print("== -Match Instrucciones- ==")
        print("varible: ", self.expresion)
        print(" valor: ", valor_Exp, " tipo: ", tipo_Exp)

        for match in self.matches:
            print("match: ", match)

            for validation in match.matches:
                if validation != '_':
                    return_validacion: RetornoType = validation.Obtener3D(controlador, ts)
                    valor_v = return_validacion.valor
                    tipo_v = return_validacion.tipo
                    if valor_Exp == valor_v and tipo_Exp == tipo_v:
                        return match.Ejecutar3D(controlador, ts)
                else:
                    return match.Ejecutar3D(controlador, ts)






