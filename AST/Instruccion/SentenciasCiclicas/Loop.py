from AST.Abstracto.Instruccion import Intruccion
from AST.Abstracto.Expresion import Expresion
from AST.TablaSimbolos.Tipos import tipo, RetornoType
from AST.TablaSimbolos.TablaSimbolos import TablaDeSimbolos


class Loop(Intruccion,Expresion):

    def __init__(self, lista_instrucciones):
        self.lista_instrucciones = lista_instrucciones

    def ObtenerValor(self, controlador, ts):
        print("Llego a loop")
        try:
            while True:
                ts_local = TablaDeSimbolos(ts, "Loop" + str(id(self)))

                for instruccion in self.lista_instrucciones:
                    retorno = instruccion.EjecutarInstruccion(controlador, ts_local)

                    if retorno is not None:
                        if isinstance(retorno, RetornoType):
                            if retorno.final == tipo.BREAK:
                                if retorno.tipo == tipo.UNDEFINED:
                                    print("Erro se esperaba una expresion")
                                    return None

                                return retorno

                            if retorno.final == tipo.CONTINUE:
                                break

                            if retorno.final == tipo.RETURN:
                                print("Erro no se esperaba un return")
                                return None
        except:
            print("Error en el Loop")


    def EjecutarInstruccion(self, controlador, ts):
        #print("Loop ins")
        #print("Llego a loop")
        #try:
            while True:
                ts_local = TablaDeSimbolos(ts, "Loop" + str(id(self)))

                for instruccion in self.lista_instrucciones:
                    retorno = instruccion.EjecutarInstruccion(controlador, ts_local)

                    if retorno is not None:
                        if isinstance(retorno, RetornoType):
                            if retorno.final == tipo.BREAK:
                                if retorno.tipo != tipo.UNDEFINED:
                                    print("Erro no se esperaba una expresion")

                                return None

                            if retorno.final == tipo.CONTINUE:
                                break

                            if retorno.final == tipo.RETURN:
                                return retorno
        #except:
            #print("Error en el Loop")

