from AST.TablaSimbolos.Simbolos import Simbolos
from AST.TablaSimbolos.Tipos import tipo as t

class Instancia(Simbolos):

    def __init__(self,idClase, idInstancia, entornoInstancia):
        super().__init__()
        super().iniciarSimboloInstancia(idClase, idInstancia, entornoInstancia, t.OBJETO)