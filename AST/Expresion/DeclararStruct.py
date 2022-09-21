from AST.Abstracto.Instruccion import Intruccion
from AST.TablaSimbolos.TablaSimbolos import TablaDeSimbolos
from AST.TablaSimbolos.Tipos import RetornoType, tipo
from AST.Abstracto.Expresion import Expresion


class DeclararStruct(Expresion):

    def ObtenerValor(self, controlador, ts):
        pass

    def __init__(self,id,declaraciones):
        self.identificador = id
        self.declaraciones = declaraciones



    def GuardarStruct(self, ts):
        print("================== Se guardo struct ================ ", self.identificador)
        if not ts.Existe_id(self.identificador):
            ts.Agregar_Simbolo(self.identificador,RetornoType(self,tipo.STRUCT))