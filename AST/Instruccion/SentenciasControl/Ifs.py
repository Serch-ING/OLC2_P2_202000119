from AST.Abstracto.Instruccion import Intruccion
from AST.Abstracto.Expresion import Expresion
from AST.TablaSimbolos.Tipos import tipo,RetornoType
from AST.TablaSimbolos.TablaSimbolos import TablaDeSimbolos
from Analizador.Gramatica import E_list
from AST.Instruccion.SentenciasTranferencia.Break import Break
from AST.Instruccion.SentenciasTranferencia.Continue import Continue

class Ifs(Intruccion,Expresion):

    def __init__(self,condicion,bloque_if,bloque_else,bloques_elif):
        self.condicion=condicion
        self.bloque_if = bloque_if
        self.bloque_else = bloque_else
        self.bloques_elif = bloques_elif
        self.etqE = ""
        self.etqS = ""

    def Ejecutar3D(self, controlador, ts):
        print("If como  instruccion")
        codigo = "/* IF instruccion */\n"
        etqSalida = controlador.Generador3D.obtenerEtiqueta()

        self.condicion.etiquetaV = controlador.Generador3D.obtenerEtiqueta()
        self.condicion.etiquetaF = controlador.Generador3D.obtenerEtiqueta()
        return_exp1:RetornoType = self.condicion.Obtener3D(controlador, ts)


        codigo += return_exp1.codigo
        codigo += f'\t{return_exp1.etiquetaV}:\n'
        ts_local = TablaDeSimbolos(ts, "If" + str(id(self)))
        codigo += self.Recorrer_ins(controlador,ts_local,self.bloque_if)
        codigo += f'\tgoto {etqSalida};\n'
        codigo += f'\t{return_exp1.etiquetaF}:\n'

        if self.bloques_elif != None:
            for insElseif in self.bloques_elif:

                insElseif.condicion.etiquetaV = controlador.Generador3D.obtenerEtiqueta()
                insElseif.condicion.etiquetaF = controlador.Generador3D.obtenerEtiqueta()
                return_expElif: RetornoType = insElseif.condicion.Obtener3D(controlador, ts)

                codigo += return_expElif.codigo
                codigo += f'\t{return_expElif.etiquetaV}:\n'
                ts_localElif = TablaDeSimbolos(ts, "ElIf" + str(id(insElseif)))
                codigo += self.Recorrer_ins(controlador, ts_localElif, insElseif.bloque_if)
                codigo += f'\tgoto {etqSalida};\n'
                codigo += f'\t{return_expElif.etiquetaF}:\n'

        if self.bloque_else!= None:
            ts_localElse = TablaDeSimbolos(ts, "Else" + str(id(self)))
            codigo += self.Recorrer_ins(controlador, ts_localElse, self.bloque_else)

        codigo += f'\t{etqSalida}: \n'
        return codigo


    def Recorrer_ins(self,controlador,ts,lista):
        codigo = ""
        for instruccion in lista:
            if isinstance(instruccion, Ifs):
                instruccion.etqE = self.etqE
                instruccion.etqS = self.etqS

            if isinstance(instruccion, Break):
                instruccion.etq = self.etqS

            if isinstance(instruccion, Continue):
                instruccion.etq = self.etqE

            codigo += instruccion.Ejecutar3D(controlador, ts)
        return codigo

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
        #retorno = ""
        for instruccion in lista:
            try:
                retorno:RetornoType = instruccion.Obtener3D(controlador, ts)
            except:
                retorno = instruccion.Ejecutar3D(controlador, ts)
                if retorno is not None:
                    if isinstance(retorno,RetornoType):
                        return retorno

        #return retorno
        return ""


