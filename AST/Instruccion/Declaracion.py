from AST.Abstracto.Instruccion import Intruccion
from AST.Expresion import Identificador
from AST.TablaSimbolos.Simbolos import Simbolos
from AST.TablaSimbolos.Tipos import tipo, RetornoType
from AST.Instruccion.DeclaracionArreglo import DeclaracionArreglo
from AST.Instruccion.DeclaracionVector import DeclaracionVector
class Declaracion(Intruccion):

    def __init__(self, id: Identificador, expresion, tipo, mut,referencia = False):
        self.identificador = id
        self.expresion = expresion
        self.tipo = tipo
        self.mut = mut
        self.referencia = referencia


    def Ejecutar3D(self, controlador, ts):
        print(" ==== Declarar === ",self.expresion)
        if self.expresion is not None:
            return_exp: RetornoType = self.expresion.Obtener3D(controlador, ts)
            codigo = ""

            if self.tipo is not None:
                sizeTabla = ts.size
                temp1 = controlador.Generador3D.obtenerTemporal()
                codigo += "/*Declaracion*/\n"
                codigo += return_exp.codigo + "\n"
                codigo += f'\t{temp1} = SP + {sizeTabla};\n'
                codigo += f'\tStack[(int){temp1}] = {return_exp.temporal};\n'
                ts.size += 1

                newSimbolo = Simbolos()
                newSimbolo.SimboloPremitivo(self.identificador.id,return_exp.valor, self.tipo, self.mut,sizeTabla)
                ts.Agregar_Simbolo(self.identificador.id, newSimbolo)
                return codigo
                #controlador.Generador3D.agregarInstruccion(codigo)

            else:
                #ValorExpresion = return_exp.valor
                TipoExpresion = return_exp.tipo
                self.tipo = TipoExpresion
                sizeTabla = ts.size
                temp1 = controlador.Generador3D.obtenerTemporal()
                codigo += "/*Declaracion*/\n"
                codigo += return_exp.codigo + "\n"
                codigo += f'\t{temp1} = SP + {sizeTabla};\n'
                codigo += f'\tStack[(int){temp1}] = {return_exp.temporal};\n'
                ts.size += 1

                newSimbolo = Simbolos()
                newSimbolo.SimboloPremitivo(self.identificador.id, None, self.tipo, self.mut, sizeTabla)
                ts.Agregar_Simbolo(self.identificador.id, newSimbolo)
                return codigo
                #controlador.Generador3D.agregarInstruccion(codigo)

        else:

            if self.tipo is not None:

                if self.tipo == tipo.ENTERO:
                    newSimbolo = Simbolos()
                    newSimbolo.SimboloPremitivo(self.identificador.id, 0, self.tipo, self.mut)
                    ts.Agregar_Simbolo(self.identificador.id, newSimbolo)

                elif self.tipo == tipo.DECIMAL:
                    newSimbolo = Simbolos()
                    newSimbolo.SimboloPremitivo(self.identificador.id, 0.0, self.tipo, self.mut)
                    ts.Agregar_Simbolo(self.identificador.id, newSimbolo)

                elif self.tipo == tipo.CARACTER:
                    newSimbolo = Simbolos()
                    newSimbolo.SimboloPremitivo(self.identificador.id, '', self.tipo, self.mut)
                    ts.Agregar_Simbolo(self.identificador.id, newSimbolo)

                elif self.tipo == tipo.STRING or self.tipo == tipo.DIRSTRING:
                    newSimbolo = Simbolos()
                    newSimbolo.SimboloPremitivo(self.identificador.id, "", self.tipo, self.mut)
                    ts.Agregar_Simbolo(self.identificador.id, newSimbolo)

                elif self.tipo == tipo.BOOLEANO:
                    newSimbolo = Simbolos()
                    newSimbolo.SimboloPremitivo(self.identificador.id, False, self.tipo, self.mut)
                    ts.Agregar_Simbolo(self.identificador.id, newSimbolo)

            else:
                newSimbolo = Simbolos()
                newSimbolo.SimboloPremitivo(self.identificador.id, None, tipo.UNDEFINED, self.mut)
                ts.Agregar_Simbolo(self.identificador.id, newSimbolo)

       # print("=== SE DECLARO LA VARIABLES === ", self.identificador.id)
       # print("=== TIPO === ", self.tipo)
       # print("=== Expresion === ", self.expresion)
