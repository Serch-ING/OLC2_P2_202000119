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
            instruccion.Ejecutar3D(controlador, ts)
            print(instruccion)
        return codigo

        if self.tipo is not None:
                print("####Se ejecuto pero esperaba retornar un dato ")

    def agregarFuncion(self, ts: TablaDeSimbolos):
        print("================== Se guardo funcion ================ ", self.identificador)
        if not ts.Existe_id(self.identificador):
            ts.Agregar_Simbolo(self.identificador, self)

        # print("Se supone que se guardo")
        # ts.Print_Table()
