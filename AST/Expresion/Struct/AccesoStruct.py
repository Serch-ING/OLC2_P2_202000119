
from AST.Abstracto.Expresion import Expresion
from AST.Abstracto.Instruccion import Intruccion
from AST.TablaSimbolos.Tipos import RetornoType
from AST.Expresion.Arreglo.AccesoArreglo import AccesoArreglo
import colorama
from colorama import Fore
from colorama import Style
import copy
from AST.Expresion.Identificador import Identificador
from AST.TablaSimbolos.Tipos import tipo as t

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

        codigo = f'/*asignar en struck*/\n'

        valor = self.exp.Obtener3D(controlador,ts)
        codigo += valor.codigo

        retorno = self.obtener_valores(self.identificador, copy.deepcopy(self.expresiones), controlador, ts)
        codigo += retorno.codigo

        codigo += f'\tHeap[(int){retorno.temporal}] = {valor.temporal};\n'
        return codigo

    def Obtener3D(self, controlador, ts):
        print("====== Expresion Struct ======")
        print(self.identificador)
        print(self.expresiones)

        codigo = f'/*obtener en struck*/\n'

        retorno = self.obtener_valores(self.identificador, copy.deepcopy(self.expresiones),controlador,ts)
        retorno.codigo = codigo + retorno.codigo


        temp1 = controlador.Generador3D.obtenerTemporal()
        retorno.codigo += f'\t{temp1} = Heap[(int){retorno.temporal}];\n'
        retorno.temporal = temp1

        return retorno

    def obtener_valores(self,identificador,expresiones,controlador,ts):
        codigo = ""

        if isinstance(self.identificador, AccesoArreglo):
            simbolo = ts.ObtenerSimbolo(self.identificador.idArreglo)
            BusquedaStruck = ts.ObtenerSimbolo(simbolo.objeto)
        else:
            simbolo = ts.ObtenerSimbolo(identificador.id)
            BusquedaStruck = ts.ObtenerSimbolo(simbolo.NombreStruck)

        diccionario_id = BusquedaStruck.valoresObjeto


        temp2 = controlador.Generador3D.obtenerTemporal()

        if isinstance(self.identificador, AccesoArreglo):
            #self.identificador.opcion = True
            retornoAccesoArreglo = self.identificador.Obtener3D(controlador, ts)
            codigo += retornoAccesoArreglo.codigo
            codigo += f'\t{temp2} = {retornoAccesoArreglo.temporal};\n'
        else:
            temp1 = controlador.Generador3D.obtenerTemporal()
            if not simbolo.referencia:
                codigo += f'\t{temp1} = SP + {simbolo.direccion};\n'
                codigo += f'\t{temp2} = Stack[(int){temp1}];\n'
            else:
                codigo += f'\t{temp2} = SP + {simbolo.direccion};\n'
                codigo += f'\t{temp2} = Stack[(int){temp2}];\n'
                while simbolo.referencia:
                    codigo += f'\t{temp2} = Stack[(int){temp2}];\n'
                    simbolo = simbolo.tsproviene.ObtenerSimbolo(simbolo.idproviene)




        #ejecutamos a donde buscara
        #id_buscado = identificador.Obtener3D(controlador, ts)
        #codigo += id_buscado.codigo

        #ejecutamps
        retornoTemp = self.recorrerArreglo(expresiones.pop(0), diccionario_id, expresiones, ts, controlador,temp2)
        #retornoTemp = self.recorrerArreglo(expresiones.pop(0),diccionario_id,expresiones,ts,controlador,id_buscado.temporal)

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






