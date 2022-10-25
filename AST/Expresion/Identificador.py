from AST.Abstracto.Expresion import Expresion
from AST.TablaSimbolos.Simbolos import Simbolos
from AST.TablaSimbolos.Tipos import RetornoType,tipo


class Identificador(Expresion):

    def __init__(self, id, referencia =False):
        self.id = id
        self.referencia = referencia
        self.etiquetaV = ""
        self.etiquetaF = ""

    def Obtener3D(self, controlador, ts):
        existe_id: Simbolos = ts.ObtenerSimbolo(self.id)

        codigo = ""

        if existe_id is not None:
           # while existe_id.referencia:
           #     existe_id = existe_id.tsproviene.ObtenerSimbolo(existe_id.idproviene)
            print("!!=== tratando de recuperar dato : ", existe_id, " id buscado: ", self.id)
            print("Tabla donde se busca el valor : ", ts.name)

            temp1 = controlador.Generador3D.obtenerTemporal()
            temp2 = controlador.Generador3D.obtenerTemporal()

            if not existe_id.referencia:
                codigo += "/* ACCEDER ID */\n"
                codigo += f'\t{temp1} = SP + {existe_id.direccion};\n'
                codigo += f'\t{temp2} = Stack[(int){temp1}];\n'
            else:
                while existe_id.referencia:
                    codigo += "/* ACCEDER ID Referencia */\n"
                    codigo += f'\t{temp2} = SP + {existe_id.direccion};\n'
                    codigo += f'\t{temp1} = Stack[(int){temp2}];\n'
                    codigo += f'\t{temp2} = Stack[(int){temp1}];\n'
                    existe_id = existe_id.tsproviene.ObtenerSimbolo(existe_id.idproviene)

            retorno = RetornoType(existe_id.valor)

            if existe_id.tipo is tipo.BOOLEANO and self.etiquetaV != "":
                codigo += f"\tif ( {temp2} == 1 ) goto {self.etiquetaV};\n"
                codigo += f"\tgoto {self.etiquetaF}; \n"
                retorno.etiquetaV = self.etiquetaV
                retorno.etiquetaF = self.etiquetaF

            retorno.iniciarRetorno(codigo,"",temp2,existe_id.tipo)
            retorno.diccionario = existe_id.diccionario
            if retorno.tipo == tipo.STRUCT:
                try:
                    retorno.Objeto = existe_id.objeto
                except:
                    pass
            return retorno
        else:
            return RetornoType("No se encontro valor", tipo.ERROR)
