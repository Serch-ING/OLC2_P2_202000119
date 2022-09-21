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

    def EjecutarInstruccion(self, controlador, ts):
        print(" ==== Declarar === ",self.expresion)
        if self.expresion is not None:
            return_exp: RetornoType = self.expresion.ObtenerValor(controlador, ts)
            try:
                ValorExpresion = return_exp.valor
                TipoExpresion = return_exp.tipo
                if TipoExpresion == tipo.ARRAY:
                    declaracion_arreglo = DeclaracionArreglo(self.mut,self.identificador.id,None, self.expresion)
                    declaracion_arreglo.EjecutarInstruccion(controlador,ts)
                    return None
                elif TipoExpresion == tipo.VECTOR:
                    declaracion_vector = DeclaracionVector(self.identificador.id,self.expresion,self.tipo,self.mut)
                    declaracion_vector.EjecutarInstruccion(controlador,ts)
                    return None
                elif TipoExpresion == tipo.STRUCT:
                    ts.Agregar_Simbolo(self.identificador.id, return_exp)
                    return None
            except:
                print("Declaracion no se esta recuperando un dato")
                return None


            if self.tipo is not None:

                if type(self.tipo) == type(TipoExpresion):

                    newSimbolo = Simbolos()
                    newSimbolo.SimboloPremitivo(self.identificador.id, ValorExpresion, self.tipo, self.mut)
                    ts.Agregar_Simbolo(self.identificador.id, newSimbolo)

            else:

                self.tipo = TipoExpresion
                newSimbolo = Simbolos()
                newSimbolo.SimboloPremitivo(self.identificador.id, ValorExpresion, self.tipo, self.mut)
                ts.Agregar_Simbolo(self.identificador.id, newSimbolo)
                return None

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
