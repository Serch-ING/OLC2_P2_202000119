from AST.Abstracto.Instruccion import Intruccion
from AST.Abstracto.Expresion import Expresion
from AST.TablaSimbolos.TablaSimbolos import TablaDeSimbolos

class BloqueMatch(Intruccion,Expresion):

    def __init__(self, matches, instrucciones,condicion):
        self.matches = matches
        self.instrucciones = instrucciones
        self.condicion=condicion
        self.ts_local = None

    def EjecutarInstruccion(self, controlador, ts):
        #print("Se ejecuto instucccion con: ", ("ts","tslocal")[self.condicion])
        self.ts_local = TablaDeSimbolos(ts, "Matc" + str(id(self.matches)))
        retorno = None

        for intruccion in self.instrucciones:
            try:
                retorno = intruccion.EjecutarInstruccion(controlador, (ts, self.ts_local)[self.condicion])
            except:
                pass
        return retorno

    def ObtenerValor(self, controlador, ts):
        #print("Se ejecuto expresion con: ", ("ts", "tslocal")[self.condicion])
        self.ts_local = TablaDeSimbolos(ts, "Matc" + str(id(self.matches)))
        retorno = None

        for intruccion in self.instrucciones:
            try:
                retorno = intruccion.ObtenerValor(controlador, (ts, self.ts_local)[self.condicion])
            except:
                intruccion.EjecutarInstruccion(controlador, (ts, self.ts_local)[self.condicion])
        return retorno
