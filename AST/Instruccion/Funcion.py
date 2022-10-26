from AST.Abstracto.Instruccion import Intruccion
from AST.TablaSimbolos.TablaSimbolos import TablaDeSimbolos
from AST.TablaSimbolos.Tipos import RetornoType, tipo
from AST.Expresion.Identificador import Identificador
from Analizador.Gramatica import E_list
from AST.Instruccion.Declaracion import Declaracion
from AST.Expresion.Identificador import Identificador
from AST.TablaSimbolos.TablaSimbolos import TablaDeSimbolos, Simbolos
from AST.Expresion.Primitivo import Primitivo


class Funcion(Intruccion):

    def __init__(self, identificador, tipo, parametros, instrucciones):
        self.identificador = identificador
        self.tipo = tipo
        self.parametros = parametros
        self.instrucciones = instrucciones
        self.retorno = None

    def Ejecutar3D(self, controlador, ts):
        print("Intrucciones de : ", self.identificador)
        codigo = ""
        temporal = ""
        tipoadd = None
        if self.tipo is not None:
            tipoadd = self.tipo
            if isinstance(self.tipo,Identificador):
                existe_id: Simbolos = ts.ObtenerSimbolo(self.tipo.id)
                tipoadd = tipo.STRUCT

            declaracion = Declaracion(Identificador("return"),None,tipoadd,True)
            if tipoadd == tipo.STRUCT:
                declaracion.objeto = self.tipo.id

            declaracion = declaracion.Ejecutar3D(controlador,ts)
            self.retorno = Identificador("return")
            codigo += declaracion
            print("llego")


            #temporal = "t" + ts.name
            #controlador.Generador3D.agregarReturn(temporal)
            #codigo += f'\t{temporal} = SP + {ts.size};\n'
            #codigo += f'\tStack[(int){temp1}]= 0;\n'

            #simbolo = Simbolos()
            #simbolo.SimboloPremitivo("return", None, self.tipo, True, ts.size)
            #ts.Agregar_Simbolo("return", simbolo)
            #ts.size += 1

        for instruccion in self.instrucciones:
            codigo += instruccion.Ejecutar3D(controlador, ts)

        #return codigo

        if self.tipo is not None:
            codigo += "\n\nSALIR: "


        if self.identificador == "main":
            retorno = RetornoType()
            retorno.iniciarRetorno("","","",None)
            controlador.Generador3D.agregarInstruccion(codigo)
            return None

        else:
            controlador.Generador3D.agregarFuncion(codigo, self.identificador)
            identificador = Identificador("return")
            identificador = identificador.Obtener3D(controlador,ts)

            if isinstance(self.tipo, Identificador):
                identificador.NombreStruck = self.tipo.id

            return identificador

    def agregarFuncion(self, ts: TablaDeSimbolos):
        print("================== Se guardo funcion ================ ", self.identificador)
        if not ts.Existe_id(self.identificador):
            ts.Agregar_Simbolo(self.identificador, self)

        # print("Se supone que se guardo")
        # ts.Print_Table()
