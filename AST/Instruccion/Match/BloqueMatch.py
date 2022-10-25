from AST.Abstracto.Instruccion import Intruccion
from AST.Abstracto.Expresion import Expresion
from AST.TablaSimbolos.TablaSimbolos import TablaDeSimbolos

class BloqueMatch(Intruccion,Expresion):

    def __init__(self, matches, instrucciones,condicion):
        self.matches = matches
        self.instrucciones = instrucciones
        self.condicion=condicion
        self.ts_local = None

    def Ejecutar3D(self, controlador, ts):
        #print("Se ejecuto instucccion con: ", ("ts","tslocal")[self.condicion])
        self.ts_local = TablaDeSimbolos(ts, "Matc" + str(id(self.matches)))
        retorno = None
        codigo = "/*Bloque inst*/\n"

        for intruccion in self.instrucciones:
            try:
                retorno = intruccion.Ejecutar3D(controlador, (ts, self.ts_local)[self.condicion])
                codigo += retorno
            except:
                pass
        return codigo

    def Obtener3D(self, controlador, ts):
        #print("Se ejecuto expresion con: ", ("ts", "tslocal")[self.condicion])
        self.ts_local = TablaDeSimbolos(ts, "Matc" + str(id(self.matches)))
        codigo = "/*Bloque exp*/\n"
        retorno = None

        for intruccion in self.instrucciones:
            try:
                retorno = intruccion.Obtener3D(controlador, (ts, self.ts_local)[self.condicion])
                codigo += retorno.codigo
            except:
                retorno = intruccion.Ejecutar3D(controlador, (ts, self.ts_local)[self.condicion])
                codigo += retorno

        retorno.codigo = codigo
        return retorno
