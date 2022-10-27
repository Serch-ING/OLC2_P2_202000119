from AST.Abstracto.Instruccion import Intruccion
from AST.Abstracto.Expresion import Expresion
from AST.TablaSimbolos.TablaSimbolos import TablaDeSimbolos, Simbolos
from AST.Instruccion import Funcion
from AST.TablaSimbolos.Tipos import RetornoType
from AST.Expresion.Identificador import Identificador
from Analizador.Gramatica import E_list
from AST.TablaSimbolos.InstanciaArreglo import InstanciaArreglo
from AST.TablaSimbolos.InstanciaVector import InstanciaVector
from AST.TablaSimbolos.Tipos import tipo as t
class Llamada(Intruccion, Expresion):

    def __init__(self, identificador, parametos):
        self.identificador = identificador
        self.parametos = parametos
        self.codigo = ""
        self.intruccion = False

    def Ejecutar3D(self, controlador, ts: TablaDeSimbolos):
        print("====Funcion=== como intruccion")
        self.intruccion = True
        return self.Obtener3D(controlador, ts).codigo


    def Obtener3D(self, controlador, ts: TablaDeSimbolos):
        print("Se ejecuto llamada de: ", self.identificador, " desde: ", ts.name)
        codigo = ""
        if ts.Existe_id(self.identificador):
            if self.identificador == "main":
                ts_local = TablaDeSimbolos(ts, self.identificador)
            else:
                bandera = True

                if bandera:
                    apuntador = ts
                    while apuntador.padre is not None:
                        apuntador = apuntador.padre

                    ts_local = TablaDeSimbolos(apuntador, self.identificador)
                else:
                    ts_local = TablaDeSimbolos(ts.padre, self.identificador)

            simbolo_funcion: Funcion = ts.ObtenerSimbolo(self.identificador)

            if self.validar_parametros(self.parametos, simbolo_funcion.parametros, controlador, ts, ts_local):
                retorno = RetornoType()
                tabla = ts
                if tabla.name != "Main":
                    while tabla.padre.name != "Main":
                        tabla = tabla.padre

                if not controlador.Generador3D.FuncionEjecutado(self.identificador):
                    if self.identificador != "main":
                        controlador.Generador3D.agregaridfuncion(self.identificador)
                    retorno = simbolo_funcion.Ejecutar3D(controlador, ts_local)
                else:
                    tablapadre = tabla.padre
                    tsbusqueda = ""
                    for x in tablapadre.siguiente:
                        if self.identificador == x.name:
                            tsbusqueda = x
                    identificador = Identificador("return")

                    retorno = identificador.Obtener3D(controlador,tsbusqueda)
                    funcionTemp = ts.ObtenerSimbolo(self.identificador)
                    if isinstance(funcionTemp.tipo, Identificador):
                        retorno.NombreStruck = funcionTemp.tipo.id

                funcion = ts.ObtenerSimbolo(self.identificador)


                if funcion.tipo is not None:
                    retorno.codigo = self.codigo + retorno.codigo

                    if funcion.tipo == t.BOOLEANO:
                        retorno.etiqueta = "a"


                else:
                    retorno = RetornoType()
                    retorno.iniciarRetorno(self.codigo,"","",None)


                retorno.codigo += f'\tSP = SP - {tabla.size};\n'
                return retorno

            else:
                print("Aqui fallo2")
        else:
            print("Aqui fallo1")


    def validar_parametros(self, parametros_llamada, parametros_funcion, controlador, ts, ts_local):
        print(self.identificador)
        codigo = "/*Llamada*/\n"
        if ts.name != "Main":
            while ts.padre.name != "Main":
                ts = ts.padre

        if len(parametros_llamada) == len(parametros_funcion):

            for i in range(0, len(parametros_llamada)):
                aux_fun = parametros_funcion[i]
                aux_lla = parametros_llamada[i]


                if not aux_fun.referencia:
                    return_lla:RetornoType = aux_lla.Obtener3D(controlador,ts)


                    #if return_lla.tipo == aux_fun.tipo:
                    temp1 = controlador.Generador3D.obtenerTemporal()
                    temp2 = controlador.Generador3D.obtenerTemporal()

                    codigo += return_lla.codigo
                    codigo += f'\n\t{temp1} = SP + {ts.size};\n'
                    codigo += f'\t{temp2} = {temp1} + {ts_local.size};/*P simulado*/\n'
                    codigo += f'\tStack[(int){temp2}]= {return_lla.temporal};\n'

                    simbolo = Simbolos()
                    simbolo.SimboloPremitivo(aux_fun.identificador.id, None, aux_fun.tipo, aux_fun.mut,ts_local.size)
                    ts_local.Agregar_Simbolo(aux_fun.identificador.id, simbolo)
                    ts_local.size += 1

                else:
                    return_lla = ts.ObtenerSimbolo(aux_lla.id)
                    #return_lla: RetornoType = aux_lla.Obtener3D(controlador, ts)

                    if (isinstance(aux_fun.tipo, list)):
                        if len(aux_fun.tipo) != 1:
                            aux_fun.tipo = aux_fun.tipo[0]

                            if return_lla.tipo == aux_fun.tipo:
                                tempReferencia = controlador.Generador3D.obtenerTemporal()
                                temp1 = controlador.Generador3D.obtenerTemporal()
                                temp2 = controlador.Generador3D.obtenerTemporal()

                                codigo += f'\n\t{tempReferencia} = SP + {return_lla.direccion};\n'
                                codigo += f'\t{temp1} = SP + {ts.size};\n'
                                codigo += f'\t{temp2} = {temp1} + {ts_local.size};/*P simulado*/\n'
                                codigo += f'\tStack[(int){temp2}]= {tempReferencia};\n'

                                simbolo = Simbolos()
                                simbolo.SimboloPremitivo(aux_fun.identificador.id, None, aux_fun.tipo, aux_fun.mut,ts_local.size)
                                simbolo.referencia = True
                                simbolo.idproviene = aux_lla.id
                                simbolo.tsproviene = ts
                                ts_local.Agregar_Simbolo(aux_fun.identificador.id, simbolo)
                                ts_local.size += 1
                        else:
                            aux_fun.tipo = aux_fun.tipo[0]

                            try:
                                simbolotemp = ts.ObtenerSimbolo(aux_lla.id)
                                if isinstance(simbolotemp,InstanciaVector):
                                    temporalTipo = simbolotemp.tipo
                                    temporal = simbolotemp.objeto
                                else:
                                    temporalTipo = simbolotemp.tipo
                                    temporal = simbolotemp.NombreStruck
                            except:
                                temporal = None
                                temporalTipo = None
                            if return_lla.tipo == aux_fun.tipo or return_lla.tipo == temporalTipo:
                                tempReferencia = controlador.Generador3D.obtenerTemporal()
                                temp1 = controlador.Generador3D.obtenerTemporal()
                                temp2 = controlador.Generador3D.obtenerTemporal()

                                codigo += f'\n\t{tempReferencia} = SP + {return_lla.direccion}/*Referencia*/;\n'
                                codigo += f'\t{temp1} = SP + {ts.size};\n'
                                codigo += f'\t{temp2} = {temp1} + {ts_local.size};/*P simulado*/\n'
                                codigo += f'\tStack[(int){temp2}]= {tempReferencia};\n'

                                simbolo = Simbolos()
                                simbolo.SimboloPremitivo(aux_fun.identificador.id, None, aux_fun.tipo, aux_fun.mut,ts_local.size)
                                simbolo.referencia = True
                                simbolo.idproviene = aux_lla.id
                                simbolo.tsproviene = ts
                                try:
                                    if temporalTipo == t.STRUCT:
                                        simbolo.NombreStruck = temporal
                                        simbolo.objeto = temporal
                                except:
                                    pass
                                ts_local.Agregar_Simbolo(aux_fun.identificador.id, simbolo)
                                ts_local.size += 1
                    else:
                        try:
                            simbolotemp = ts.ObtenerSimbolo(aux_lla.id)
                            if isinstance(simbolotemp, InstanciaVector):
                                temporalTipo = simbolotemp.tipo
                                temporal = simbolotemp.objeto
                            else:
                                temporalTipo = simbolotemp.tipo
                                temporal = simbolotemp.NombreStruck
                        except:
                            temporal = None
                            temporalTipo = None
                        if return_lla.tipo == aux_fun.tipo or return_lla.tipo == temporalTipo:
                            tempReferencia = controlador.Generador3D.obtenerTemporal()
                            temp1 = controlador.Generador3D.obtenerTemporal()
                            temp2 = controlador.Generador3D.obtenerTemporal()

                            codigo += f'\n\t{tempReferencia} = SP + {return_lla.direccion};/*Referencia*/\n'
                            codigo += f'\t{temp1} = SP + {ts.size};\n'
                            codigo += f'\t{temp2} = {temp1} + {ts_local.size};/*P simulado*/\n'
                            codigo += f'\tStack[(int){temp2}]= {tempReferencia};\n'

                            simbolo = Simbolos()
                            simbolo.SimboloPremitivo(aux_fun.identificador.id, None, aux_fun.tipo, aux_fun.mut,ts_local.size)
                            simbolo.referencia = True
                            simbolo.idproviene = aux_lla.id
                            simbolo.tsproviene = ts
                            try:
                                if temporalTipo == t.STRUCT:
                                    simbolo.NombreStruck = temporal
                                    simbolo.objeto = temporal
                            except:
                                pass
                            ts_local.Agregar_Simbolo(aux_fun.identificador.id, simbolo)
                            ts_local.size += 1
            codigo += f'\tSP = SP + {ts.size};\n'
            codigo += f'\t{self.identificador}();\n'
            self.codigo += codigo
            return True
        else:
            print(" Validacion parametros size")
            return False
