
from AST.Abstracto.Instruccion import Intruccion
from AST.Expresion import Identificador
from AST.TablaSimbolos.Simbolos import Simbolos
from AST.TablaSimbolos.Tipos import tipo, RetornoType
from AST.TablaSimbolos.InstanciaVector import InstanciaVector
from colorama import Fore
from colorama import Style
from AST.Expresion.Identificador import Identificador

class DeclaracionVector(Intruccion):

    def __init__(self, id: Identificador, expresion, tipo  , mut = False, referencia = False):
        self.identificador = id
        self.expresion = expresion
        self.tipo = tipo
        self.capacidad = 0
        self.mut = mut
        self.referencia = referencia


    def EjecutarInstruccion(self, controlador, ts):
        print(Fore.BLUE + Style.BRIGHT + "Llegpo a declaracion arreglo" + Style.RESET_ALL)
        print("Llego bien a declarar vector jdsjdasfjkdfsa")
        if  not isinstance(self.expresion,list):
            Exp_arreglo: RetornoType = self.expresion.ObtenerValor(controlador, ts)
            objetoVector = Exp_arreglo.valor

            if self.tipo != None:
                if self.tipo != objetoVector.tipo:
                    return None
            else:
                self.tipo = objetoVector.tipo

            objetoVector.identificador = self.identificador
            objetoVector.mut = self.mut
            objetoVector.withcapacity = len(objetoVector.valores)
            ts.Agregar_Simbolo(self.identificador, objetoVector)
            ts.Print_Table()
            print("Hola: ",objetoVector)
        else:
            if len( self.expresion) ==0:
                print("Llego solo con decalracion normal" )
                if isinstance(self.tipo, Identificador):
                    self.tipo = ts.ObtenerSimbolo(self.tipo.id).tipo

                new_vector = InstanciaVector(self.tipo, 1, [])
                new_vector.withcapacity = self.capacidad
                new_vector.tipo = self.tipo
                new_vector.mut = self.mut

                ts.Agregar_Simbolo(self.identificador, new_vector)
            else:
                print("Llego solo con decalracion capacity")

                self.capacidad= self.expresion.pop(0).ObtenerValor(controlador, ts).valor

                new_vector = InstanciaVector(self.tipo, 1, [])
                new_vector.withcapacity = self.capacidad

                if isinstance(self.tipo, Identificador):
                    self.tipo = ts.ObtenerSimbolo(self.tipo.id).tipo
                new_vector.tipo = self.tipo
                new_vector.mut = self.mut


                ts.Agregar_Simbolo(self.identificador, new_vector)

                return_exp = ts.ObtenerSimbolo(self.identificador)
                print("Llego solo con decalracion capacity")