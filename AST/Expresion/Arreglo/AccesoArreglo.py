from AST.Abstracto.Expresion import Expresion
from AST.Abstracto.Instruccion import Intruccion
from AST.TablaSimbolos.Tipos import RetornoType,tipo
from AST.TablaSimbolos.InstanciaArreglo import InstanciaArreglo
from AST.TablaSimbolos.TablaSimbolos import TablaDeSimbolos
from AST.TablaSimbolos.InstanciaVector import InstanciaVector
from AST.Expresion.Identificador import Identificador
class AccesoArreglo(Expresion,Intruccion):
    def __init__(self, idArreglo, listaExpresiones, valor = None):
        self.idArreglo = idArreglo
        self.listaExpresiones = listaExpresiones
        self.valor = valor
        self.codigo = ""
        self.temporales = []
        self.opcion = False
        self.EsVector = True

    def Ejecutar3D(self, controlador, ts):
        codigo = "/*Asignacion Arreglo*/"
        ts.Print_Table()
        if ts.Existe_id(self.idArreglo) is not True:
            return RetornoType()


        insArreglo = InstanciaArreglo(None,None,None)
        arreglo = ts.ObtenerSimbolo(self.idArreglo)

        Expression = self.valor.Obtener3D(controlador, ts)
        codigo += Expression.codigo

        for x in self.listaExpresiones:
            valor = x.Obtener3D(controlador,ts)
            self.temporales.append(valor.temporal)
            codigo += valor.codigo

        retronoA = None

        if arreglo.mut:
            retronoA = insArreglo.SetValor(arreglo.direccion,controlador,self.temporales,arreglo)
            codigo += retronoA.codigo

        codigo += f'\tHeap[(int){retronoA.temporal}] = {Expression.temporal};\n'
        return codigo

    def Obtener3D(self, controlador, ts:TablaDeSimbolos) -> RetornoType:
        print("Llego a accesoL ",self.idArreglo, " lista dimensiones: ",self.listaExpresiones)

        if ts.Existe_id(self.idArreglo) is not True:
            return RetornoType()

        insArreglo = InstanciaArreglo(None, None, None)
        arreglo = ts.ObtenerSimbolo(self.idArreglo)



        if not isinstance(arreglo, InstanciaVector):
            #if len(self.listaExpresiones) > len(arreglo.dimensiones):
            #    return RetornoType()

            dimensiones = self.compilarDimensiones(controlador, ts)
            if not self.opcion:
                valor = insArreglo.Obtener3D(arreglo.direccion,controlador,self.temporales,arreglo)
            else:
                valor = insArreglo.Obtener3DV2(arreglo.direccion, controlador,self.temporales,arreglo)
            valor.codigo = self.codigo + valor.codigo
            valor.tipo = arreglo.tipo
            return valor

        else:
            #dimensiones = self.compilarDimensiones(controlador, ts)
            valor = arreglo.ObtenerValor(arreglo.direccion,controlador,self.temporales,arreglo)
            valor.codigo = self.codigo + valor.codigo
            valor.tipo = arreglo.tipo
            return valor

    def compilarDimensiones(self,controlador, ts ):
        listaDimensiones = []

        for dim in self.listaExpresiones:
            dimVal = dim.Obtener3D(controlador, ts)
            self.codigo += dimVal.codigo
            self.temporales.append(dimVal.temporal)
            # operador ternario      hacer_si_true if condicion else hacer_si_false
            if dimVal.tipo != tipo.ENTERO and dimVal.tipo != tipo.USIZE:
                return
            else:
                listaDimensiones.append(dimVal.valor)

        return listaDimensiones


