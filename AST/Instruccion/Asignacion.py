from AST.Abstracto.Instruccion import Intruccion
from AST.TablaSimbolos.Tipos import RetornoType

class Asignacion(Intruccion):
    def __init__(self,identificador,valor):
        self.identificador=identificador
        self.valor = valor


    def Ejecutar3D(self, controlador, ts):
        if(ts.Existe_id(self.identificador)):

            Expression: RetornoType = self.valor.Obtener3D(controlador, ts)
            ValorExpresion = Expression.valor
            TipoExpresion = Expression.tipo

            ts.Actualizar_Simbolo(self.identificador,TipoExpresion,ValorExpresion,ts.name)
