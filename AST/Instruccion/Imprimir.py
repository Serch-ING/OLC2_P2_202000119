from AST.Abstracto.Instruccion import Intruccion
from AST.TablaSimbolos.Tipos import tipo as t
from AST.TablaSimbolos.Tipos import RetornoType
from AST.TablaSimbolos.InstanciaArreglo import InstanciaArreglo
from AST.TablaSimbolos.InstanciaVector import InstanciaVector
from AST.Expresion.Identificador import Identificador
from AST.Expresion.Arreglo.AccesoArreglo import AccesoArreglo
from AST.Expresion.Struct.AccesoStruct import AccesoStruct
from AST.AST_Ejecucion.AST import Generador3D

class Imprimir(Intruccion):

    def __init__(self,  expresion, tipo, lista):
        self.expresion = expresion
        self.tipo = tipo
        self.lista =lista

    def Ejecutar3D(self, controlador, ts):
        global Generador3D

        codigo = ""
        valorexp = self.expresion.Obtener3D(controlador,ts)
        codigo += valorexp.codigo



        if valorexp.tipo.tipo == t.ENTERO:
            codigo += f'\tprintf(\"%d\",{valorexp.temporal}); \n'
        elif valorexp.tipo.tipo == t.DECIMAL:
            codigo += f'\tprintf(\"%f\",{valorexp.temporal}); \n'
        elif valorexp.tipo.tipo == t.STRING or valorexp.tipo.tipo == t.DIRSTRING:
            temp = Generador3D.obtenerTemporal()
            caracter = Generador3D.obtenerTemporal()
            codigo += f'\t{temp}  = {valorexp.temporal};\n'
            etq1 = Generador3D.obtenerEtiqueta()
            etq2 = Generador3D.obtenerEtiqueta()

            codigo += f'\t{etq1}: \n'
            codigo += f'\t{caracter} = Heap[(int){temp}]; \n'
            codigo += f'\tif({caracter} == 0) goto {etq2};\n' \
                      f'\tprintf(\"%c\",(char){caracter});\n' \
                      f'\t{temp} = {temp} + 1;\n' \
                      f'\tgoto {etq1};\n' \
                      f'\t{etq2}:\n'


        Generador3D.agregarInstruccion(codigo)


    def ObtenerArrayText(self,array):
        print(type(array))
        text = ""
        if isinstance(array,list):
            text += "["

            bandera = True
            banderaint = len(array)
            aux = 0
            for x in array:
                if isinstance(x,list):
                    text += self.ObtenerArrayText(x)
                    if aux+1 != banderaint:
                        text += ","

                elif isinstance(x,InstanciaVector):
                    text += self.ObtenerArrayText(x.valores)
                    if aux + 1 != banderaint:
                        text += ","

                else:
                    if bandera:
                        text += str(x)
                        bandera = False
                    else:
                        text += "," + str(x)

                aux += 1

            text += "]"
            return text
        else:
            print("fallo")