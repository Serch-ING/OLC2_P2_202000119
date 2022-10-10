from AST.Abstracto.Instruccion import Intruccion
from AST.TablaSimbolos.Tipos import RetornoType,tipo


class Continue(Intruccion):

    def __init__(self):
        self.etq = ""


    def Ejecutar3D(self, controlador, ts):
        codigo = ""
        codigo += f'goto {self.etq};'
        return codigo


