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

    def Ejecutar3D(self, controlador, ts):
        print("If como  instruccion")
        codigo = "/* IF instruccion */\n"
        etq1 = controlador.Generador3D.obtenerEtiqueta()
        etq2 = controlador.Generador3D.obtenerEtiqueta()
        etq3 = None

        return_exp1:RetornoType = self.condicion.Obtener3D(controlador, ts)
        codigotemp = return_exp1.codigo

        ts_local1 = TablaDeSimbolos(ts, "If" + str(id(self)))
        bloque_if = self.Recorrer_ins(controlador,ts_local1,self.bloque_if)

        codigo += f'\tif {codigotemp} goto {etq1};\n'
        codigo += f'\tgoto {etq2};\n'
        codigo += f'\t{etq1}:\n'
        codigo += bloque_if

        if self.bloque_else != None:
            etq3 = controlador.Generador3D.obtenerEtiqueta()
            codigo += f'\tgoto {etq3};\n'

        codigo += f'\t{etq2}:\n'

        if self.bloque_else != None:
            ts_local2 = TablaDeSimbolos(ts, "If" + str(id(self)))
            bloque_else = self.Recorrer_ins(controlador, ts_local2, self.bloque_else)
            codigo += bloque_else
            codigo += f'\t{etq3}:\n'


        #cabiar
        controlador.Generador3D.agregarInstruccion(codigo)



    def Recorrer_ins(self,controlador,ts,lista):
        codigo = None
        for instruccion in lista:
            #try:
                codigo = instruccion.Ejecutar3D(controlador, ts)
                return codigo
            #except:
            #    print("Erro en if")


    def Obtener3D(self, controlador, ts):
        print("If como  expresion")
        return_exp: RetornoType = self.condicion.Obtener3D(controlador, ts)
        valor_Exp = return_exp.valor
        tipo_Exp = return_exp.tipo

        if tipo_Exp == tipo.BOOLEANO:

            if valor_Exp:

                ts_local = TablaDeSimbolos(ts, "If" + str(id(self)))
                return self.Recorrer_exp_val(controlador, ts_local, self.bloque_if)

            else:

                if self.bloques_elif is not None:

                    for list_if in self.bloques_elif:
                        return_if: RetornoType = list_if.condicion.Obtener3D(controlador, ts)
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
                retorno:RetornoType = instruccion.Obtener3D(controlador, ts)
            except:
                retorno = instruccion.Ejecutar3D(controlador, ts)
                if retorno is not None:
                    if isinstance(retorno,RetornoType):
                        return retorno

        return retorno


