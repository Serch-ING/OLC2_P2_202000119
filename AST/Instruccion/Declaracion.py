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
        self.objeto = None


    def Ejecutar3D(self, controlador, ts):
        print(" ==== Declarar === ",self.expresion)
        codigo = ""
        if self.expresion is not None:


            return_exp: RetornoType = self.expresion.Obtener3D(controlador, ts)

            try:
                ValorExpresion = return_exp.valor
                TipoExpresion = return_exp.tipo
                if TipoExpresion == tipo.ARRAY:
                    return_exp.codigo += return_exp.codigotemp
                    declaracion_arreglo = DeclaracionArreglo(self.mut, self.identificador.id, None, self.expresion,return_exp)
                    return declaracion_arreglo.Ejecutar3D(controlador, ts)

                elif TipoExpresion == tipo.VECTOR:
                    declaracion_vector = DeclaracionVector(self.identificador.id, self.expresion, self.tipo, self.mut)
                    return declaracion_vector.Ejecutar3D(controlador, ts)
                
                elif TipoExpresion == tipo.STRUCT:
                    temp1 = controlador.Generador3D.obtenerTemporal()
                    sizeTabla = ts.size
                    codigo += return_exp.codigo + "\n"
                    codigo += f'\t{temp1} = SP + {sizeTabla};\n'
                    codigo += f'\tStack[(int){temp1}] = {return_exp.temporal};\n'
                    ts.size += 1

                    newSimbolo = Simbolos()
                    newSimbolo.SimboloStruck(self.identificador.id, return_exp.tipo, self.mut, sizeTabla,return_exp.diccionario)
                    newSimbolo.NombreStruck = return_exp.NombreStruck
                    #ts.Agregar_Simbolo(self.identificador.id, return_exp)
                    ts.Agregar_Simbolo(self.identificador.id, newSimbolo)
                    return codigo
            except:
                print("Declaracion no se esta recuperando un dato")
                return None

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
                sizeTabla = ts.size
                newSimbolo = Simbolos()
                if self.tipo == tipo.ENTERO:
                    temp1 = controlador.Generador3D.obtenerTemporal()
                    codigo += "/*Declaracion*/\n"
                    codigo += f'\t{temp1} = SP + {sizeTabla};\n'
                    codigo += f'\tStack[(int){temp1}] = 0;\n'
                    ts.size += 1

                    newSimbolo.SimboloPremitivo(self.identificador.id, 0, self.tipo, self.mut,sizeTabla)
                    ts.Agregar_Simbolo(self.identificador.id, newSimbolo)
                    return  codigo

                elif self.tipo == tipo.DECIMAL:
                    newSimbolo.SimboloPremitivo(self.identificador.id, 0.0, self.tipo, self.mut,sizeTabla)
                    ts.Agregar_Simbolo(self.identificador.id, newSimbolo)

                elif self.tipo == tipo.CARACTER:
                    newSimbolo.SimboloPremitivo(self.identificador.id, '', self.tipo, self.mut,sizeTabla)
                    ts.Agregar_Simbolo(self.identificador.id, newSimbolo)

                elif self.tipo == tipo.STRING or self.tipo == tipo.DIRSTRING:
                    newSimbolo.SimboloPremitivo(self.identificador.id, "", self.tipo, self.mut,sizeTabla)
                    ts.Agregar_Simbolo(self.identificador.id, newSimbolo)

                elif self.tipo == tipo.BOOLEANO:
                    temp1 = controlador.Generador3D.obtenerTemporal()
                    codigo += "/*Declaracion*/\n"
                    codigo += f'\t{temp1} = SP + {sizeTabla};\n'
                    codigo += f'\tStack[(int){temp1}] = 0;\n'
                    ts.size += 1

                    newSimbolo.SimboloPremitivo(self.identificador.id, False, self.tipo, self.mut, sizeTabla)
                    ts.Agregar_Simbolo(self.identificador.id, newSimbolo)
                    return codigo

                elif self.tipo == tipo.STRUCT:
                    tempHP = controlador.Generador3D.obtenerTemporal()
                    sizeTabla = ts.size

                    objeto = ts.ObtenerSimbolo(self.objeto)
                    valoresarr = objeto.valoresObjeto

                    codigo += f'\t{tempHP} = HP;\n'
                    codigo += f'\tHeap[(int)HP] = {len(valoresarr)};\n'
                    codigo += f'\tHP = HP + 1;\n'
                    for x in valoresarr:
                        codigo += f'\tHeap[(int)HP] = 0;\n'
                        codigo += f'\tHP = HP + 1;\n'

                    temp1 = controlador.Generador3D.obtenerTemporal()
                    codigo += f'\t{temp1} = SP + {sizeTabla};\n'
                    codigo += f'\tStack[(int){temp1}] = {tempHP};\n'
                    ts.size += 1

                    newSimbolo = Simbolos()
                    newSimbolo.SimboloStruck(self.identificador.id, self.tipo, self.mut, sizeTabla,self.objeto)
                    newSimbolo.NombreStruck = self.objeto
                    # ts.Agregar_Simbolo(self.identificador.id, return_exp)
                    ts.Agregar_Simbolo(self.identificador.id, newSimbolo)
                    return codigo
            else:
                newSimbolo = Simbolos()
                newSimbolo.SimboloPremitivo(self.identificador.id, None, tipo.UNDEFINED, self.mut,sizeTabla)
                ts.Agregar_Simbolo(self.identificador.id, newSimbolo)

       # print("=== SE DECLARO LA VARIABLES === ", self.identificador.id)
       # print("=== TIPO === ", self.tipo)
       # print("=== Expresion === ", self.expresion)
