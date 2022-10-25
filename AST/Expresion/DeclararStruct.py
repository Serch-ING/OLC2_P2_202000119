from AST.Abstracto.Instruccion import Intruccion
from AST.TablaSimbolos.TablaSimbolos import TablaDeSimbolos
from AST.TablaSimbolos.Tipos import RetornoType, tipo
from AST.Abstracto.Expresion import Expresion

from AST.Expresion.Repeticiones import Repeticiones

class DeclararStruct(Expresion):

    def Obtener3D(self, controlador, ts):
        pass

    def __init__(self,id,declaraciones):
        self.identificador = id
        self.declaraciones = declaraciones

    def GuardarStruct(self, ts):
        print("================== Se guardo struct ================ ", self.identificador)
        diccionario = []
        if not ts.Existe_id(self.identificador):
            for x in self.declaraciones:
                tipoadd = x.expresion
                if isinstance(tipoadd, Repeticiones):
                    #pass
                    tipoadd = tipoadd.valor
                diccionario.append([x.identificador,tipoadd])
            retorno = RetornoType(self,tipo.STRUCT)
            retorno.valoresObjeto = diccionario
            ts.Agregar_Simbolo(self.identificador,retorno)