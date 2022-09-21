from AST.Abstracto.Instruccion import Intruccion
from AST.Abstracto.Expresion import Expresion
from AST.TablaSimbolos.Tipos import tipo,RetornoType
from AST.TablaSimbolos.TablaSimbolos import TablaDeSimbolos
from Analizador.Gramatica import E_list

class Ifs(Intruccion,Expresion):

    def __init__(self,condicion,bloque_if,bloque_else,bloques_elif):
        self.condicion=condicion
        self.bloque_if = bloque_if
        self.bloque_else = bloque_else
        self.bloques_elif = bloques_elif

    def EjecutarInstruccion(self, controlador, ts):
        print("If como  instruccion")
        return_exp: RetornoType = self.condicion.ObtenerValor(controlador, ts)
        valor_Exp = return_exp.valor
        tipo_Exp = return_exp.tipo

        if tipo_Exp == tipo.BOOLEANO :

            if valor_Exp:

                ts_local = TablaDeSimbolos(ts, "If" + str(id(self)))
                return self.Recorrer_ins(controlador, ts_local, self.bloque_if)

            else:

                if self.bloques_elif is not None:

                    for list_if in self.bloques_elif:
                        return_if: RetornoType = list_if.condicion.ObtenerValor(controlador, ts)
                        valor_if = return_if.valor
                        tipo_if = return_if.tipo

                        if tipo_if == tipo.BOOLEANO :
                            if valor_if:
                                return self.Recorrer_ins(controlador, ts, self.bloques_elif)

                if self.bloque_else is not None:
                    ts_local = TablaDeSimbolos(ts, "Else" + str(id(self)))
                    return self.Recorrer_ins(controlador, ts_local,self.bloque_else)
        else:

            E_list.agregar_error("La expresion en if no es booleano : " + str(valor_Exp), 2, ts.name,
                                 0, 0)
            E_list.print_errores()
    def Recorrer_ins(self,controlador,ts,lista):
        retorno = None
        for instruccion in lista:
            #try:
                retorno = instruccion.EjecutarInstruccion(controlador, ts)

                if retorno is not None:
                    if isinstance(retorno,RetornoType):
                        return retorno
            #except:
            #    print("Erro en if")


    def ObtenerValor(self, controlador, ts):
        print("If como  expresion")
        return_exp: RetornoType = self.condicion.ObtenerValor(controlador, ts)
        valor_Exp = return_exp.valor
        tipo_Exp = return_exp.tipo

        if tipo_Exp == tipo.BOOLEANO:

            if valor_Exp:

                ts_local = TablaDeSimbolos(ts, "If" + str(id(self)))
                return self.Recorrer_exp_val(controlador, ts_local, self.bloque_if)

            else:

                if self.bloques_elif is not None:

                    for list_if in self.bloques_elif:
                        return_if: RetornoType = list_if.condicion.ObtenerValor(controlador, ts)
                        valor_if = return_if.valor
                        tipo_if = return_if.tipo

                        if tipo_if == tipo.BOOLEANO:
                            if valor_if:
                                return self.Recorrer_exp_val(controlador, ts, self.bloques_elif)

                if self.bloque_else is not None:
                    ts_local = TablaDeSimbolos(ts, "Else" + str(id(self)))
                    return self.Recorrer_exp_val(controlador, ts_local, self.bloque_else)

    def Recorrer_exp_val(self,controlador,ts,lista):
        retorno = None
        for instruccion in lista:
            try:
                retorno:RetornoType = instruccion.ObtenerValor(controlador, ts)
            except:
                retorno = instruccion.EjecutarInstruccion(controlador, ts)
                if retorno is not None:
                    if isinstance(retorno,RetornoType):
                        return retorno

        return retorno


