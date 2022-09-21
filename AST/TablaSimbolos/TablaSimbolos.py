from AST.TablaSimbolos.Simbolos import Simbolos
from Analizador.Gramatica import E_list

class TablaDeSimbolos():

    def __init__(self, padre, name):
        self.padre = padre
        self.name = name
        self.tabla = {}

        # Solo para reportes
        self.siguiente = []
        if padre != None:
            bandera = True
            for x in padre.siguiente:
                if x.name == self.name:
                    bandera = False
                    break
            if bandera:
                padre.siguiente.append(self)

    def Agregar_Simbolo(self, id, simbolo):
        print("Agregando: ", id, " con simbolo: ", simbolo, " en: ", self.name)
        if not self.Existe_id(id):
            self.tabla[id] = simbolo
        else:
            print("Ya existe la variable, no se pudo actualizar: ",simbolo," Con valor ",simbolo.valor)


    def Existe_id(self, id):
        ts = self
        while ts is not None:
            existe = ts.tabla.get(id)

            if existe is not None:
                print("Si existe el simbolo: ", id)
                return True

            ts = ts.padre

        return False

    def ObtenerSimbolo(self, id):
        ts = self
        while ts is not None:
            #print(ts.tabla)
            existe = ts.tabla.get(id)

            if existe is not None:
                return existe

            ts = ts.padre

        return None

    def Actualizar_Simbolo(self,id, tipo,valor,ambito):
        ts = self
        while ts is not None:
            existe = ts.tabla.get(id)

            if existe is not None:

                if existe.tipo == tipo and existe.mut:
                    ts.tabla[id].valor = valor
                    break
                else:
                    if not existe.mut:
                        E_list.agregar_error("Se intento actulizar la varible inmutable : " + str(id), 2, ambito, 0,
                                             0)
                        E_list.print_errores()

                    if existe.tipo != tipo:
                        E_list.agregar_error(
                            "Se intento actulizar la varible " + str(id) + " a distinto tipo de: " + str(
                                existe.tipo) + " a " + str(tipo), 2, ambito, 0, 0)
                        E_list.print_errores()
                    print("Los tipos no coinciden o la varible es inmutable")


            ts = ts.padre

    def Print_Table(self):
        print("Tabla de simbolos: ",self.name)
        print(self.tabla)