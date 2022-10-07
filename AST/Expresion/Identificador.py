from AST.Abstracto.Expresion import Expresion
from AST.TablaSimbolos.Simbolos import Simbolos
from AST.TablaSimbolos.Tipos import RetornoType,tipo


class Identificador(Expresion):

    def __init__(self, id, referencia =False):
        self.id = id
        self.referencia = referencia

    def Obtener3D(self, controlador, ts):
        existe_id: Simbolos = ts.ObtenerSimbolo(self.id)
        codigo = ""

        if existe_id is not None:
            print("!!=== tratando de recuperar dato : ", existe_id, " id buscado: ", self.id)
            print("Tabla donde se busca el valor : ", ts.name)

            temp1 = controlador.Generador3D.obtenerTemporal()
            temp2 = controlador.Generador3D.obtenerTemporal()
            codigo += "/* ACCEDER ID */\n"
            codigo += f'\t{temp1} = SP + {existe_id.direccion};\n'
            codigo += f'\t{temp2} = Stack[(int){temp1}];\n'
            controlador.Generador3D.agregarInstruccion(codigo)
            retorno = RetornoType()
            retorno.iniciarRetorno(codigo,"",temp2,existe_id.tipo)
            return  retorno
        else:
            return RetornoType("No se encontro valor", tipo.ERROR)
