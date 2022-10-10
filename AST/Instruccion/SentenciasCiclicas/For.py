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
class For(Intruccion):
    def __init__(self,ID_Iterable,elementos,lista_instrucciones):
        self.ID_Iterable = ID_Iterable
        self.elementos = elementos
        self.lista_instrucciones = lista_instrucciones
        self.etqE = ""
        self.etqS = ""

    def Ejecutar3D(self, controlador, ts):
        print("Con iteracion: ",self.ID_Iterable)
        tipo_for = self.elementos[0]
        codigo = "/* For instruccion */\n"


        if tipo_for == 1:
                pass
        elif tipo_for == 2:
            #parametro1 = self.elementos[1].Obtener3D(controlador, ts)
            parametro2 = self.elementos[2].Obtener3D(controlador, ts)

            declaracion = Declaracion(Identificador(self.ID_Iterable),self.elementos[1],tipo.ENTERO,True)
            codigo += declaracion.Ejecutar3D(controlador, ts)
            codigo += parametro2.codigo + '\n'

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

