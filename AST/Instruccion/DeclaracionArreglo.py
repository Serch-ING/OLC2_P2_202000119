from AST.Abstracto.Instruccion import Intruccion
import colorama
from colorama import Fore
from colorama import Style
from AST.TablaSimbolos.Tipos import tipo, RetornoType

class DeclaracionArreglo(Intruccion):
    def __init__(self, mutable, identificador, dimensiones, expresion):
        self.mutable = mutable
        self.identificador = identificador
        self.dimensiones = dimensiones
        self.expresion = expresion
        self.tipo = None

    def EjecutarInstruccion(self, controlador, ts):
        print(Fore.BLUE + Style.BRIGHT + "Llegpo a declaracion arreglo" + Style.RESET_ALL)
        Exp_arreglo: RetornoType = self.expresion.ObtenerValor(controlador,ts)

        if self.dimensiones is not None:
            self.tipo = self.dimensiones.pop(0)
            print("dimesiones, ",self.dimensiones)
            if Exp_arreglo.tipo != tipo.ARRAY:
                return

            objetoArreglo = Exp_arreglo.valor

            if objetoArreglo.tipo != self.tipo:
                return


            i = len(objetoArreglo.dimensiones)-1
            objetoArreglo.identificador = self.identificador

            for x in self.dimensiones:
                if x.valor != objetoArreglo.dimensiones[i]:
                    print("ERROR")
                    return
                i -= 1
            objetoArreglo.mut = self.mutable
            ts.Agregar_Simbolo(self.identificador,objetoArreglo)
            ts.Print_Table()

        else:

            if Exp_arreglo.tipo != tipo.ARRAY:
                return

            objetoArreglo = Exp_arreglo.valor
            self.tipo =  objetoArreglo.tipo
            objetoArreglo.identificador = self.identificador
            ts.Agregar_Simbolo(self.identificador, objetoArreglo)
            ts.Print_Table()



            print("=== Sin valores")