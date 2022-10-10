from AST.Abstracto.Instruccion import Intruccion
from AST.TablaSimbolos.Tipos import tipo,RetornoType
from AST.TablaSimbolos.TablaSimbolos import TablaDeSimbolos
from AST.Instruccion.SentenciasControl.Ifs import Ifs
from AST.Instruccion.SentenciasTranferencia.Break import Break
from AST.Instruccion.SentenciasTranferencia.Continue import Continue

class While(Intruccion):
    def __init__(self,expresion,lista_instrucciones):
        self.condicion = expresion
        self.lista_instrucciones = lista_instrucciones
        self.etqE = ""
        self.etqS = ""

    def Ejecutar3D(self, controlador, ts):


        codigo = "/* WHILE instruccion */\n"

        self.condicion.etiquetaV = controlador.Generador3D.obtenerEtiqueta()
        self.condicion.etiquetaF = controlador.Generador3D.obtenerEtiqueta()
        return_exp1: RetornoType = self.condicion.Obtener3D(controlador, ts)

        etqWhile = controlador.Generador3D.obtenerEtiqueta()
        self.etqE= etqWhile
        self.etqS=return_exp1.etiquetaF
        codigo += f'{etqWhile}:\n'
        codigo += return_exp1.codigo
        codigo += f'\t{return_exp1.etiquetaV}:\n'

        ts_local = TablaDeSimbolos(ts, "While" + str(id(self)))
        codigo += self.Recorrer_ins(controlador, ts_local, self.lista_instrucciones)

        codigo += f'\tgoto {etqWhile};\n'
        codigo += f'\t{return_exp1.etiquetaF}:\n'

        return codigo


    def Recorrer_ins(self,controlador,ts,lista):
        codigo = ""
        for instruccion in lista:
            if isinstance(instruccion,Ifs):
                instruccion.etqE = self.etqE
                instruccion.etqS = self.etqS

            if isinstance(instruccion,Break):
                instruccion.etq = self.etqS

            if isinstance(instruccion, Continue):
                instruccion.etq = self.etqE

            codigo += instruccion.Ejecutar3D(controlador, ts)

        return codigo


