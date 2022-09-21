from AST.Abstracto.Expresion import Expresion
from AST.TablaSimbolos.Tipos import RetornoType,tipo
from AST.Expresion.Arreglo import ArregloData
from AST.TablaSimbolos.InstanciaArreglo import InstanciaArreglo
class Repeticiones(Expresion):
    def __init__(self,valor,numero,tipo = False):
        self.valor=valor
        self.numero=numero
        self.tipo =tipo

    def ObtenerValor(self, controlador, ts):
        if not self.tipo:
            valor: RetornoType = self.valor.ObtenerValor(controlador, ts)
            ValorExpresion = valor.valor
            TipoExpresion = valor.tipo

            numero: RetornoType = self.numero.ObtenerValor(controlador, ts)
            ValorEnumero = numero.valor
            Tiponumero = numero.tipo


            retorno = []
            for x in range(0,ValorEnumero):
                retorno.append(valor.valor)

            valorf = InstanciaArreglo(Tiponumero, 1, retorno)
            return  RetornoType(valorf,tipo.ARRAY)
        else:
            return RetornoType( self.valor, tipo.ARRAY)