from AST.Abstracto.Instruccion import Intruccion
from AST.TablaSimbolos.Tipos import tipo
from AST.TablaSimbolos.Tipos import RetornoType
from AST.TablaSimbolos.TablaSimbolos import TablaDeSimbolos,Simbolos
from AST.TablaSimbolos.InstanciaArreglo import InstanciaArreglo
from AST.Instruccion.Asignacion import Asignacion
from AST.Instruccion.Declaracion import Declaracion
from AST.Expresion.Identificador import Identificador
from AST.Expresion.Operaciones.Aritmetica import Aritmetica
from AST.Expresion.Operaciones.Operacion import operador
from AST.Expresion.Primitivo import Primitivo
from AST.Instruccion.SentenciasTranferencia.Break import Break
from AST.Instruccion.SentenciasTranferencia.Continue import Continue
from AST.Instruccion.SentenciasControl.Ifs import Ifs
from AST.Expresion.Operaciones.Relacional import Relacional
from AST.Expresion.Identificador import Identificador
class For(Intruccion):
    def __init__(self,ID_Iterable,elementos,lista_instrucciones):
        self.ID_Iterable = ID_Iterable
        self.elementos = elementos
        self.lista_instrucciones = lista_instrucciones
        self.etqE = ""
        self.etqS = ""

    def Ejecutar3D(self, controlador, ts):
        diccionario = None
        print("Con iteracion: ",self.ID_Iterable)
        tipo_for = self.elementos[0]
        codigo = "/* For instruccion */\n"


        if tipo_for == 1:

            array = self.elementos[1].Obtener3D(controlador, ts)
            #declaracion = Declaracion(Identificador(self.ID_Iterable), None, tipo.ENTERO, True)
            declaracion = Declaracion(Identificador(self.ID_Iterable), None, array.tipo, False)

            if array.tipo == tipo.STRUCT:
                SimboloTemp: Simbolos = ts.ObtenerSimbolo(array.Objeto)
                declaracion.objeto = array.Objeto
            codigo += declaracion.Ejecutar3D(controlador, ts)

            array.codigo += array.codigotemp
            codigo += array.codigo

            temp1 = controlador.Generador3D.obtenerTemporal()

            etiquetaV = controlador.Generador3D.obtenerEtiqueta()
            etiquetaF = controlador.Generador3D.obtenerEtiqueta()
            etqFor = controlador.Generador3D.obtenerEtiqueta()
            self.etqE = etqFor
            self.etqS = etiquetaF

            temp2 = controlador.Generador3D.obtenerTemporal()
            temp3 = controlador.Generador3D.obtenerTemporal()
            temp4 = controlador.Generador3D.obtenerTemporal()
            temp5 = controlador.Generador3D.obtenerTemporal()
            existe_id: Simbolos = ts.ObtenerSimbolo(self.ID_Iterable)

            codigo += f'\t{temp1} = 0;\n'

            postamanio = controlador.Generador3D.obtenerTemporal()
            codigo += f'\t{postamanio} =  {array.temporal};\n'
            if array.tipo == tipo.STRUCT:
                codigo += f'\t{postamanio} =  {postamanio} + 1;\n'

            codigo += f'\t{etqFor}:\n'
            codigo += f'\t{temp2} = {temp1} + {postamanio};\n'
            codigo += f'\t{temp3} = {temp2} + 1;\n'

            codigo += f'\t{temp4} = Heap[(int){temp3}];\n'
            codigo += f'\t{temp5} = SP + {existe_id.direccion};\n'
            codigo += f'\tStack[(int){temp5}] = {temp4};\n'

            tempTamanio = controlador.Generador3D.obtenerTemporal()

            if isinstance(self.elementos[1],Identificador):
                codigo += f'\t{tempTamanio} = Heap[(int){array.temporal}];\n'

            else:
                codigo += f'\t{tempTamanio} = Heap[(int){array.temporal}];\n'
                #codigo += f'\t{tempTamanio} = Stack[(int){array.temporal}];\n'
                #codigo += f'\t{tempTamanio} = Heap[(int){tempTamanio}];\n'

            codigo += f'\tif ({temp1} < {tempTamanio}) goto {etiquetaV};\n'
            codigo += f'\tgoto {etiquetaF};\n'

            codigo += f'\t{etiquetaV}:\n'

            codigo += self.Recorrer_ins(controlador, ts, self.lista_instrucciones)
            codigo += f'\t{temp1} = {temp1} + 1;\n'

            codigo += f'\tgoto {etqFor};\n'
            codigo += f'\t{self.etqS}:\n'

            return codigo


        elif tipo_for == 2:
            #parametro1 = self.elementos[1].Obtener3D(controlador, ts)
            #parametro2 = self.elementos[2].Obtener3D(controlador, ts)

            declaracion = Declaracion(Identificador(self.ID_Iterable),self.elementos[1],tipo.ENTERO,True)
            codigo += declaracion.Ejecutar3D(controlador, ts)
            #codigo += parametro2.codigo + '\n'

            Condicion = Relacional(Identificador(self.ID_Iterable), '<', self.elementos[2], False)
            Condicion.etiquetaV = controlador.Generador3D.obtenerEtiqueta()
            Condicion.etiquetaF = controlador.Generador3D.obtenerEtiqueta()
            CondicionV = Condicion.Obtener3D(controlador, ts)

            etqFor= controlador.Generador3D.obtenerEtiqueta()
            self.etqE = etqFor
            self.etqS = Condicion.etiquetaF

            codigo += f'\t{etqFor}:\n'

            codigo += CondicionV.codigo
            codigo += f'\t{ Condicion.etiquetaV}:\n'

            codigo += self.Recorrer_ins(controlador, ts, self.lista_instrucciones)
            adignacion = Asignacion(self.ID_Iterable,Aritmetica(Identificador(self.ID_Iterable),'+',Primitivo(1,'ENTERO')))
            codigo += adignacion.Ejecutar3D(controlador,ts)

            codigo += f'\tgoto {etqFor};\n'
            codigo += f'\t{self.etqS}:\n'

            return codigo


    def Recorrer_ins(self,controlador,ts,lista):
        codigo = ""
        for instruccion in lista:
            if isinstance(instruccion,Ifs):
                instruccion.etqE = self.etqE
                instruccion.etqS = self.etqS

            if isinstance(instruccion,Break):
                instruccion.etq = self.etqS

            if isinstance(instruccion, Continue):
                instruccion.etq = self.etqE

            codigo += instruccion.Ejecutar3D(controlador, ts)

        return codigo

