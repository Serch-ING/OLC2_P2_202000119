from AST.Abstracto.Instruccion import Intruccion
from AST.TablaSimbolos.TablaSimbolos import TablaDeSimbolos
from AST.TablaSimbolos.Tipos import RetornoType, tipo
from AST.Abstracto.Expresion import Expresion


class DeclararStruct(Expresion):

    def Obtener3D(self, controlador, ts):
        pass

    def __init__(self,id,declaraciones):
        self.identificador = id
        self.declaraciones = declaraciones

    def GuardarStruct(self, ts):
        print("================== Se guardo struct ================ ", self.identificador)
        if not ts.Existe_id(self.identificador):
            retorno = RetornoType(self,tipo.STRUCT)
            ts.Agregar_Simbolo(self.identificador,retorno)