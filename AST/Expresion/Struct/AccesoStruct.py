
from AST.Abstracto.Expresion import Expresion
from AST.Abstracto.Instruccion import Intruccion
from AST.TablaSimbolos.Tipos import RetornoType
from AST.Expresion.Arreglo.AccesoArreglo import AccesoArreglo
import colorama
from colorama import Fore
from colorama import Style
import copy
from AST.Expresion.Identificador import Identificador

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


        #return self.fn_obtner_valor(self.identificador,copy.deepcopy(self.expresiones))
        return self.obtener_valores(self.identificador, copy.deepcopy(self.expresiones),controlador,ts)

    def obtener_valores(self,identificador,expresiones,controlador,ts):
        codigo = f'/*obtener {self.identificador.id}*/\n'

        id_buscado = identificador.Obtener3D(controlador, ts)
        codigo += id_buscado.codigo

        simbolo = ts.ObtenerSimbolo(identificador.id)

        BusquedaStruck = ts.ObtenerSimbolo(simbolo.NombreStruck)
        diccionario_id = BusquedaStruck.valoresObjeto

        copiaExpresioes = expresiones
        retornoTemp = self.recorrerArreglo(copiaExpresioes.pop(0),diccionario_id,copiaExpresioes,ts,controlador,id_buscado.temporal)

        codigo += retornoTemp[0]

        retorno = RetornoType()
        retorno.iniciarRetorno(codigo,"",retornoTemp[1],retornoTemp[2])

        return retorno

    def recorrerArreglo(self,busqueda,diccionario,expresiones,ts,controlador,tamporal):
        codigo = ""
        tempretorno = ""
        tipoFinal = None

        temp1 = controlador.Generador3D.obtenerTemporal()
        contador = 1
        BusquedaStruck = None
        retornoTemp = []
        retorno = []

        for x in diccionario:
            nombre = x[0]
            tipo = x[1]
            if busqueda.id == nombre:
                tipoFinal = tipo
                if isinstance(tipo,Identificador):
                    BusquedaStruck = ts.ObtenerSimbolo(tipo.id)
                break
            contador += 1

        codigo += f'\t{temp1} = {tamporal} + {contador};\n'
        tempretorno = temp1
        if BusquedaStruck is not None:
            temp2 = controlador.Generador3D.obtenerTemporal()
            codigo += f'\t{temp2} = Heap[(int){temp1}];\n'
            retornoTemp = self.recorrerArreglo(expresiones.pop(0), BusquedaStruck.valoresObjeto, expresiones, ts, controlador,temp2)

        if retornoTemp != []:
            codigo += retornoTemp[0]
            tempretorno = retornoTemp[1]
            tipoFinal = retornoTemp[2]

        retorno.append(codigo)
        retorno.append(tempretorno)
        retorno.append(tipoFinal)
        return retorno




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





