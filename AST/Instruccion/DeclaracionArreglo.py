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
        codigo = ""

        print(Fore.BLUE + Style.BRIGHT + "Llegpo a declaracion arreglo" + Style.RESET_ALL)
        if self.expfinal is not None:
            Exp_arreglo: RetornoType = self.expfinal
        else:
            Exp_arreglo: RetornoType = self.expresion.Obtener3D(controlador, ts)


        '''if len(Exp_arreglo.dimensiones) == 1:
            Exp_arreglo.codigo = Exp_arreglo.codigo + Exp_arreglo.codigotemp + Exp_arreglo.codigotempOtros
        elif  len(Exp_arreglo.dimensiones) == 2:
            Exp_arreglo.codigo = Exp_arreglo.codigotemp + Exp_arreglo.codigo + Exp_arreglo.codigotempOtros
        else:
            Exp_arreglo.codigo = Exp_arreglo.codigotemp + Exp_arreglo.codigo'''

        if self.dimensiones is not None:
            self.tipo = self.dimensiones.pop(0)

            objetoArreglo = Exp_arreglo.valor
            objetoArreglo.identificador = self.identificador
            objetoArreglo.mut = self.mutable

            sizeTabla = ts.size
            temp1 = controlador.Generador3D.obtenerTemporal()
            codigo += "/*Declaracion*/\n"
            codigo += Exp_arreglo.codigo + "\n"
            codigo += f'\t{temp1} = SP + {sizeTabla};\n'
            codigo += f'\tStack[(int){temp1}] = {Exp_arreglo.temporal};\n'
            ts.size += 1

            objetoArreglo.direccion = sizeTabla
            ts.Agregar_Simbolo(self.identificador,objetoArreglo)
            ts.Print_Table()
            return codigo
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

