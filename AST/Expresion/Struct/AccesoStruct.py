
from AST.Abstracto.Expresion import Expresion
from AST.Abstracto.Instruccion import Intruccion
from AST.TablaSimbolos.Tipos import RetornoType
from AST.Expresion.Arreglo.AccesoArreglo import AccesoArreglo
import colorama
from colorama import Fore
from colorama import Style
import copy
class AccesoStruct(Intruccion,Expresion):

    def __init__(self,id,expresiones,exp):
        self.identificador = id
        self.expresiones =expresiones
        self.exp=exp
        self.ts = None
        self.controlador = None


    def EjecutarInstruccion(self, controlador, ts):
        print("====== Instruccion Struct ======")
        print(self.identificador)
        print(self.expresiones)
        print(self.exp)


        if isinstance(self.identificador, AccesoArreglo):
            struck_ccr = self.identificador.ObtenerValor(controlador, ts)
            struck_dic = struck_ccr.valor.diccionario
        else:
            struck_ccr = ts.ObtenerSimbolo(self.identificador.id)
            struck_dic = struck_ccr.valor.diccionario
        expresiones = copy.deepcopy(self.expresiones)

        while (True):

            if len(expresiones) == 1:
                id = expresiones[0].id
                valor_acc = struck_dic.get(id)
                if valor_acc is not  None:
                    if not hasattr(self.exp,'valor'):
                        if isinstance( self.exp,AccesoStruct):
                            valor = self.exp.ObtenerValor(controlador,ts)
                            struck_dic[id].valor = valor.valor
                            return


                        else:

                            valor = self.exp.ObtenerValor(controlador, ts)
                            struck_dic[id].valor = valor.valor
                            return None
                print(Fore.BLUE + Style.BRIGHT + "ERROR Inst 2" + Style.RESET_ALL)
                while True:
                    pass
            else:
                id = expresiones[0].id
                valor_acc = struck_dic.get(id)
                if valor_acc is not None:
                    struck_dic = valor_acc.valor.diccionario
                    expresiones.pop(0)

            print(Fore.BLUE + Style.BRIGHT + "ERROR Inst" + Style.RESET_ALL)


    def ObtenerValor(self, controlador, ts):
        print("====== Expresion Struct ======")
        print(self.identificador)
        print(self.expresiones)
        #print(self.exp)
        self.ts = ts
        self.controlador = controlador
        return self.fn_obtner_valor(self.identificador,copy.deepcopy(self.expresiones))


    def fn_obtner_valor(self,identificador,expresiones):

        if isinstance(identificador,AccesoArreglo):
            struck_ccr = identificador.ObtenerValor(self.controlador,self.ts)
            print(struck_ccr)
            struck_dic = struck_ccr.valor.diccionario
        else:
            struck_ccr =  self.ts.ObtenerSimbolo(identificador.id)
            struck_dic = struck_ccr.valor.diccionario

        while(True):
            if not isinstance(expresiones[0], AccesoStruct):
                if len(expresiones) == 1:
                    id = expresiones[0].id
                    valor_acc = struck_dic.get(id)
                    if valor_acc is not None:
                        return RetornoType(valor_acc.valor, valor_acc.tipo)
                    print(Fore.BLUE + Style.BRIGHT + "ERROR Obtener" + Style.RESET_ALL)
                else:
                    id = expresiones[0].id
                    valor_acc = struck_dic.get(id)
                    if valor_acc is not None:

                        struck_dic = valor_acc.valor.diccionario
                        expresiones.pop(0)

            else:

                expr = expresiones[0].identificador
                expresiones = expresiones[0].expresiones
                if not isinstance(expr, AccesoStruct):
                    if len(expresiones) == 1:
                        id = expr.id
                        valor_acc = struck_dic.get(id)
                        struck_dic = valor_acc.valor.diccionario





