
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

        self.objeto = self.tipo


    def Ejecutar3D(self, controlador, ts):

        codigo= "/*Declaracion vector*/\n"
        if not isinstance(self.expresion,list):
            Exp_arreglo: RetornoType = self.expresion.Obtener3D(controlador, ts)
            objetoVector = Exp_arreglo.valor

            objetoVector.identificador = self.identificador
            objetoVector.mut = self.mut
            objetoVector.withcapacity = len(objetoVector.valores)

            temp1 = controlador.Generador3D.obtenerTemporal()
            codigo += Exp_arreglo.codigo

            codigo += f'\t{temp1} = SP + {ts.size};\n'
            codigo += f'\tStack[(int){temp1}] = {Exp_arreglo.temporal};\n'

            objetoVector.direccion = ts.size
            ts.Agregar_Simbolo(self.identificador, objetoVector)

            ts.size += 1

            return codigo

        else:
            if len( self.expresion) ==0:
                print("Llego solo con decalracion normal" )
                if isinstance(self.tipo, Identificador):
                    self.tipo = ts.ObtenerSimbolo(self.tipo.id).tipo

                new_vector = InstanciaVector(self.tipo, 1, [])
                new_vector.withcapacity = 0
                new_vector.tipo = self.tipo
                new_vector.mut = self.mut

                temp1 = controlador.Generador3D.obtenerTemporal()

                codigo += f'\t{temp1} = SP + {ts.size};\n'
                codigo += f'\tStack[(int){temp1}] = HP;\n'
                codigo += f'\tHP= HP + 2;\n'

                new_vector.direccion = ts.size
                ts.Agregar_Simbolo(self.identificador, new_vector)
                ts.size += 1

                return codigo
            else:
                print("Llego solo con decalracion capacity")

                self.capacidad = self.expresion.pop(0).Obtener3D(controlador, ts)

                new_vector = InstanciaVector(self.tipo, 1, [])
                new_vector.withcapacity = 0

                if isinstance(self.tipo, Identificador):
                    self.tipo = ts.ObtenerSimbolo(self.tipo.id).tipo

                new_vector.tipo = self.tipo
                new_vector.mut = self.mut

                temp1 = controlador.Generador3D.obtenerTemporal()
                temp2 = controlador.Generador3D.obtenerTemporal()

                codigo += self.capacidad.codigo
                codigo += f'\t{temp2} = HP;\n'
                codigo += f'\tHeap[(int)HP] = 0;\n'
                codigo += f'\tHP = HP + 1; \n'
                codigo += f'\tHeap[(int)HP] = {self.capacidad.temporal};\n'
                codigo += f'\tHP = HP + 1; \n'
                codigo += f'\tHP = HP + {self.capacidad.temporal}; \n'

                codigo += f'\t{temp1} = SP + {ts.size};\n'
                codigo += f'\tStack[(int){temp1}] = {temp2};\n'

                new_vector.direccion = ts.size

                if new_vector.tipo == tipo.STRUCT:
                    new_vector.objeto = self.objeto.id

                ts.Agregar_Simbolo(self.identificador, new_vector)
                ts.size += 1

                #return_exp = ts.ObtenerSimbolo(self.identificador)
                #print("Llego solo con decalracion capacity")

                return codigo