from AST.Abstracto.Instruccion import Intruccion
from AST.Abstracto.Expresion import Expresion
from AST.TablaSimbolos.TablaSimbolos import TablaDeSimbolos, Simbolos
from AST.Instruccion import Funcion
from AST.TablaSimbolos.Tipos import RetornoType
from AST.Expresion.Identificador import Identificador
from Analizador.Gramatica import E_list

class Llamada(Intruccion, Expresion):

    def __init__(self, identificador, parametos):
        self.identificador = identificador
        self.parametos = parametos

    def EjecutarInstruccion(self, controlador, ts: TablaDeSimbolos):
        print("====Funcion=== como intruccion")
        self.ObtenerValor(controlador,ts)


    def ObtenerValor(self, controlador, ts: TablaDeSimbolos):
        print("Se ejecuto llamada de: ", self.identificador, " desde: ", ts.name)

        if ts.Existe_id(self.identificador):
            if self.identificador == "main":
                ts_local = TablaDeSimbolos(ts, self.identificador)
            else:
                bandera = True
                #bandera = False
                pointer = ts
                #while pointer is not None:
                #    if pointer.name == self.identificador:
                #        bandera = True
                #    pointer = pointer.padre

                if bandera:
                    apuntador = ts
                    while apuntador.padre is not None:
                        apuntador = apuntador.padre

                    ts_local = TablaDeSimbolos(apuntador, self.identificador)
                else:
                    ts_local = TablaDeSimbolos(ts.padre, self.identificador)

            simbolo_funcion: Funcion = ts.ObtenerSimbolo(self.identificador)

            if self.validar_parametros(self.parametos, simbolo_funcion.parametros, controlador, ts, ts_local):

                retorno = simbolo_funcion.EjecutarInstruccion(controlador, ts_local)

                if retorno is not None:
                    if isinstance(retorno,RetornoType):
                        return retorno
            else:
                print("Aqui fallo2")
        else:
            print("Aqui fallo1")


    def validar_parametros(self, parametros_llamada, parametros_funcion, controlador, ts, ts_loca):

        if len(parametros_llamada) == len(parametros_funcion):

            for i in range(0, len(parametros_llamada)):
                aux = parametros_funcion[i]
                aux_id = aux.identificador.id
                aux_tipo = aux.tipo
                aux_mut = aux.mut
                aux_referencia = aux.referencia
                print("Parametro de la funcion")
                print("aux id: ",aux_id)
                print("aux tipo: ", aux_tipo)

                aux_exp = parametros_llamada[i]
                if not aux_referencia:

                    aux_get_data:RetornoType = aux_exp.ObtenerValor(controlador, ts)
                    aux_exp_valor = aux_get_data.valor
                    aux_exp_tipo = aux_get_data.tipo

                    print("Parametro de la llamada")
                    print("aux valor: ", aux_exp_valor)
                    print("aux tipo: ", aux_exp_tipo)

                    if aux_tipo == aux_exp_tipo:
                        simbolo = Simbolos()
                        simbolo.SimboloPremitivo(aux_id, aux_exp_valor, aux_tipo, aux_mut)
                        print("= Simbolo id: ", aux_id, " valor: ",aux_exp_valor, " tipo ",aux_tipo)
                        ts_loca.Agregar_Simbolo(aux_id, simbolo)
                    else:
                        E_list.agregar_error("Se intento asigar un dato: "+ str(aux_exp_tipo) + " a un parametro: " + str(aux_tipo), 2, ts.name,
                                             0, 0)
                        E_list.print_errores()
                        return False
                else:
                    print("Se llego")
                    print(aux_id)
                    if( isinstance(aux_tipo,list)):
                        if len(aux_tipo) != 1:
                            tipo_array = aux_tipo[0]

                            aux_exp_data: Simbolos = ts.ObtenerSimbolo(aux_exp.id)
                            aux_tipo.reverse()
                            for x in range(0,len(aux_tipo)-1):
                                if aux_tipo[x].valor != aux_exp_data.dimensiones[x]:
                                    E_list.agregar_error("No se cumplio con los parametros" , 2, ts.name,0, 0)
                                    E_list.print_errores()
                                    return False
                            aux_tipo.reverse()
                            if tipo_array != aux_exp_data.tipo:
                                E_list.agregar_error(
                                    "Se intento asigar un dato: " + str(aux_exp_data.tipo) + " a un parametro: " + str(
                                        aux_tipo), 2, ts.name,
                                    0, 0)
                                E_list.print_errores()
                                return False

                            if (aux_exp.referencia or aux_exp_data.referencia) and aux_mut:
                                aux_exp_data.referencia = True
                                ts_loca.Agregar_Simbolo(aux_id, aux_exp_data)


                            print("Llego: ",tipo_array, " - ")
                        else:

                            tipo_array = aux_tipo[0]

                            aux_exp_data: Simbolos = ts.ObtenerSimbolo(aux_exp.id)
                            if isinstance(tipo_array ,Identificador):
                                tipo_array = ts.ObtenerSimbolo(tipo_array.id).tipo
                            try:
                                if isinstance(tipo_array,str):
                                    tipo_array = ts.ObtenerSimbolo(tipo_array).tipo
                            except:
                                pass


                            if tipo_array != aux_exp_data.tipo:
                                E_list.agregar_error(
                                    "Se intento asigar un dato: " + str(tipo_array) + " a un parametro: " + str(
                                        aux_exp_data.tipo), 2, ts.name,
                                    0, 0)
                                E_list.print_errores()
                                return False

                            if (aux_exp.referencia or aux_exp_data.referencia)and aux_mut:
                                aux_exp_data.referencia = True
                                ts_loca.Agregar_Simbolo(aux_id, aux_exp_data)

                            print("Llego: ", tipo_array, " - ")

                    print("Es por memoeria ")

            return True
        else:
            print(" Validacion parametros size")
            return False
