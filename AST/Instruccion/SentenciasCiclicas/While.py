from AST.Abstracto.Instruccion import Intruccion
from AST.TablaSimbolos.Tipos import tipo,RetornoType
from AST.TablaSimbolos.TablaSimbolos import TablaDeSimbolos

class While(Intruccion):
    def __init__(self,expresion,lista_instrucciones):
        self.expresion = expresion
        self.lista_instrucciones = lista_instrucciones

    def EjecutarInstruccion(self, controlador, ts):
        return_exp: RetornoType = self.expresion.ObtenerValor(controlador, ts)
        valor_Exp = return_exp.valor
        tipo_Exp = return_exp.tipo

        if tipo_Exp == tipo.BOOLEANO:
            if valor_Exp:
                #try:
                    while self.expresion.ObtenerValor(controlador, ts).valor:
                        ts_local = TablaDeSimbolos(ts, "While" + str(id(self)))

                        for instruccion in self.lista_instrucciones:
                            retorno = instruccion.EjecutarInstruccion(controlador,ts_local)

                            if retorno is not None:
                                if isinstance(retorno,RetornoType):
                                    if retorno.final == tipo.BREAK:
                                        if retorno.tipo != tipo.UNDEFINED:
                                            print("Se intento regresar dato con break")

                                        return None

                                    if retorno.final == tipo.CONTINUE:
                                        break

                                    return retorno
                #except:
                #    print("Error en el While")

