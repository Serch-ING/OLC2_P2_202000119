from AST.Abstracto.Instruccion import Intruccion
from AST.Abstracto.Expresion import Expresion
from AST.TablaSimbolos.Tipos import tipo, RetornoType
from AST.TablaSimbolos.TablaSimbolos import TablaDeSimbolos
from AST.Instruccion.SentenciasControl.Ifs import Ifs
from AST.Instruccion.SentenciasTranferencia.Break import Break
from AST.Instruccion.SentenciasTranferencia.Continue import Continue

class Loop(Intruccion,Expresion):

    def __init__(self, lista_instrucciones):
        self.lista_instrucciones = lista_instrucciones
        self.etqE = ""
        self.etqS = ""

    def Obtener3D(self, controlador, ts):
        print("Llego a loop")
        try:
            while True:
                ts_local = TablaDeSimbolos(ts, "Loop" + str(id(self)))

                for instruccion in self.lista_instrucciones:
                    retorno = instruccion.Ejecutar3D(controlador, ts_local)

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


    def Ejecutar3D(self, controlador, ts):

        codigo = "/* WHILE instruccion */\n"

        etqLoop = controlador.Generador3D.obtenerEtiqueta()
        etqSalida = controlador.Generador3D.obtenerEtiqueta()

        self.etqE = etqLoop
        self.etqS = etqSalida

        codigo += f'{etqLoop}:\n'

        ts_local = TablaDeSimbolos(ts, "While" + str(id(self)))
        codigo += self.Recorrer_ins(controlador, ts_local, self.lista_instrucciones)

        codigo += f'\tgoto {etqLoop};\n'
        codigo += f'\t{etqSalida}:\n'

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


