from AST.Abstracto.Expresion import Expresion
from AST.TablaSimbolos.Simbolos import Simbolos
from AST.TablaSimbolos.Tipos import RetornoType,tipo


class Identificador(Expresion):

    def __init__(self, id, referencia =False):
        self.id = id
        self.referencia = referencia

    def ObtenerValor(self, controlador, ts):
        existe_id: Simbolos = ts.ObtenerSimbolo(self.id)

        if existe_id is not None:
            print("!!=== tratando de recuperar dato : ", existe_id, " id buscado: ", self.id)
            print("Tabla donde se busca el valor : ", ts.name)

            return RetornoType(existe_id.valor, existe_id.tipo)
        else:
            return RetornoType("No se encontro valor", tipo.ERROR)
