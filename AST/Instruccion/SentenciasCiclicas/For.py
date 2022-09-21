from AST.Abstracto.Instruccion import Intruccion
from AST.TablaSimbolos.Tipos import tipo
from AST.TablaSimbolos.Tipos import RetornoType
from AST.TablaSimbolos.TablaSimbolos import TablaDeSimbolos,Simbolos
from AST.TablaSimbolos.InstanciaArreglo import InstanciaArreglo
class For(Intruccion):
    def __init__(self,ID_Iterable,elementos,lista_instrucciones):
        self.ID_Iterable = ID_Iterable
        self.elementos = elementos
        self.lista_instrucciones = lista_instrucciones

    def EjecutarInstruccion(self, controlador, ts):
        print("Con iteracion: ",self.ID_Iterable)
        tipo_for = self.elementos[0]

        if tipo_for == 1:
                array = self.elementos[1].ObtenerValor(controlador,ts)
                if not isinstance(array.valor,InstanciaArreglo):
                    array = ts.ObtenerSimbolo(self.elementos[1].id)
                    valores = array.valores
                    tipo_array = array.tipo
                else:
                    valores = array.valor.valores
                    tipo_array = array.valor.tipo
                for i in valores:
                    print("iteracion: ", i)
                    ts_local = TablaDeSimbolos(ts, "for" + str(id(self)))
                    newSimbolo = Simbolos()
                    newSimbolo.SimboloPremitivo(self.ID_Iterable, i,tipo_array , False)
                    ts_local.Agregar_Simbolo(self.ID_Iterable, newSimbolo)

                    for instruccion in self.lista_instrucciones:
                        retorno = instruccion.EjecutarInstruccion(controlador, ts_local)

                        if retorno is not None:
                            if isinstance(retorno, RetornoType):
                                if retorno.final == tipo.BREAK:
                                    if retorno.tipo != tipo.UNDEFINED:
                                        print("Se intento regresar dato con break")

                                    return None

                                if retorno.final == tipo.CONTINUE:
                                    break

                                return retorno

                print("Termino con iteracion: ", self.ID_Iterable)



        elif tipo_for == 2:
            parametro1 = self.elementos[1].ObtenerValor(controlador,ts)
            parametro2 = self.elementos[2].ObtenerValor(controlador,ts)
            parametro1_valor = parametro1.valor
            parametro2_valor = parametro2.valor
            for i in range(parametro1_valor,parametro2_valor):
                print("iteracion: ", i)
                ts_local = TablaDeSimbolos(ts, "for" + str(id(self)))
                newSimbolo = Simbolos()
                newSimbolo.SimboloPremitivo(self.ID_Iterable, i, tipo.ENTERO, False)
                ts_local.Agregar_Simbolo(self.ID_Iterable,newSimbolo)

                for instruccion in self.lista_instrucciones:
                    retorno = instruccion.EjecutarInstruccion(controlador, ts_local)

                    if retorno is not None:
                        if isinstance(retorno, RetornoType):
                            if retorno.final == tipo.BREAK:
                                if retorno.tipo != tipo.UNDEFINED:
                                    print("Se intento regresar dato con break")

                                return None

                            if retorno.final == tipo.CONTINUE:
                                break

                            return retorno

            print("Termino con iteracion: ", self.ID_Iterable)