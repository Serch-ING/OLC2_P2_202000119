
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


    def Ejecutar3D(self, controlador, ts):
        print("====== Instruccion Struct ======")
        print(self.identificador)
        print(self.expresiones)
        print(self.exp)


        if isinstance(self.identificador, AccesoArreglo):
            struck_ccr = self.identificador.Obtener3D(controlador, ts)
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
                            valor = self.exp.Obtener3D(controlador, ts)
                            struck_dic[id].valor = valor.valor
                            return


                        else:

                            valor = self.exp.Obtener3D(controlador, ts)
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


    def Obtener3D(self, controlador, ts):
        print("====== Expresion Struct ======")
        print(self.identificador)
        print(self.expresiones)
        #print(self.exp)

        #return self.fn_obtner_valor(self.identificador,copy.deepcopy(self.expresiones))
        return self.obtener_valores(self.identificador, copy.deepcopy(self.expresiones),controlador,ts)

    def obtener_valores(self,identificador,expresiones,controlador,ts):
        codigo = f'/*obtener {self.identificador.id}*/\n'

        id_buscado = identificador.Obtener3D(controlador, ts)
        codigo += id_buscado.codigo

        id_arr = expresiones[0]

        simbolo = ts.ObtenerSimbolo(identificador.id)
        diccionario_id = simbolo.diccionario

        valor_acc = diccionario_id.get(id_arr.id)

        contador = 1

        temp1 = controlador.Generador3D.obtenerTemporal()

        for x in diccionario_id:
            if id_arr.id == x:
                break
            contador += 1
            print(x)

        codigo += f'\t{temp1} = {id_buscado.temporal} + {contador};\n'

        retorno = RetornoType()
        retorno.iniciarRetorno(codigo,"",temp1,valor_acc.tipo)

        return  retorno



    def fn_obtner_valor(self,identificador,expresiones):

        if isinstance(identificador,AccesoArreglo):
            struck_ccr = identificador.Obtener3D(self.controlador, self.ts)
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





