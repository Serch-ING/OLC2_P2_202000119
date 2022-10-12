from AST.Abstracto.Instruccion import Intruccion
from AST.TablaSimbolos.TablaSimbolos import TablaDeSimbolos
from AST.TablaSimbolos.Tipos import RetornoType, tipo
from AST.Expresion.Identificador import Identificador
from Analizador.Gramatica import E_list

class Funcion(Intruccion):

    def __init__(self, identificador, tipo, parametros, instrucciones):
        self.identificador = identificador
        self.tipo = tipo
        self.parametros = parametros
        self.instrucciones = instrucciones

    def Ejecutar3D(self, controlador, ts):
        print("Intrucciones de : ", self.identificador)
        codigo = ""
        for instruccion in self.instrucciones:
            codigo += instruccion.Ejecutar3D(controlador, ts)

        #return codigo

        if self.tipo is not None:
            codigo += "\n\nSALIR: "

        if self.identificador == "main":
            controlador.Generador3D.agregarInstruccion(codigo)
        else:

            controlador.Generador3D.agregarFuncion(codigo, self.identificador)

    def agregarFuncion(self, ts: TablaDeSimbolos):
        print("================== Se guardo funcion ================ ", self.identificador)
        if not ts.Existe_id(self.identificador):
            ts.Agregar_Simbolo(self.identificador, self)

        # print("Se supone que se guardo")
        # ts.Print_Table()
