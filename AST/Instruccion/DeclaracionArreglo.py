from AST.Abstracto.Instruccion import Intruccion
import colorama
from colorama import Fore
from colorama import Style
from AST.TablaSimbolos.Tipos import tipo, RetornoType

class DeclaracionArreglo(Intruccion):
    def __init__(self, mutable, identificador, dimensiones, expresion,expfinal):
        self.mutable = mutable
        self.identificador = identificador
        self.dimensiones = dimensiones
        self.expresion = expresion
        self.tipo = None

        self.expfinal =expfinal

    def Ejecutar3D(self, controlador, ts):


        print(Fore.BLUE + Style.BRIGHT + "Llegpo a declaracion arreglo" + Style.RESET_ALL)
        if self.expfinal is not None:
            Exp_arreglo: RetornoType = self.expfinal
        else:
            Exp_arreglo: RetornoType = self.expresion.Obtener3D(controlador, ts)



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

            temp1 = controlador.Generador3D.obtenerTemporal()
            sizeTabla = ts.size
            Exp_arreglo.codigo += f'\t{temp1} = SP + {sizeTabla};\n'
            Exp_arreglo.codigo += f'\tStack[(int){temp1}] = {Exp_arreglo.temporal};\n'
            ts.size += 1

            objetoArreglo = Exp_arreglo.valor
            self.tipo =  objetoArreglo.tipo
            objetoArreglo.identificador = self.identificador
            objetoArreglo.direccion = sizeTabla
            ts.Agregar_Simbolo(self.identificador, objetoArreglo)
            ts.Print_Table()



            return Exp_arreglo.codigo

