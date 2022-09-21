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

    def EjecutarInstruccion(self, controlador, ts):
        print("Intrucciones de : ", self.identificador)

        for instruccion in self.instrucciones:

            retorno = instruccion.EjecutarInstruccion(controlador, ts)

            if retorno is not None and isinstance(retorno, RetornoType):
                if retorno.final == tipo.BREAK:
                    E_list.agregar_error("Se utilizo sentencia BREAK fuera de sentencia ciclica", 2, ts.name,
                                         0, 0)
                    continue

                if isinstance(self.tipo, Identificador):
                    self.tipo = ts.ObtenerSimbolo(self.tipo.id).tipo
                if retorno.tipo == self.tipo:
                    return retorno

                if self.tipo is None:
                    if retorno.tipo != tipo.UNDEFINED:
                        print("####Se esta intentando regresar un dato en un metodo ")
                else:
                    print("####Se intento regresar un dato diferente al de la funcion ")

                return RetornoType()

        if self.tipo is not None:
                print("####Se ejecuto pero esperaba retornar un dato ")

    def agregarFuncion(self, ts: TablaDeSimbolos):
        print("================== Se guardo funcion ================ ", self.identificador)
        if not ts.Existe_id(self.identificador):
            ts.Agregar_Simbolo(self.identificador, self)

        # print("Se supone que se guardo")
        # ts.Print_Table()
