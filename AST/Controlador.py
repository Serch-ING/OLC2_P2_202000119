from Generador3D.Generador3D import Generador3D

class Controlador:
    consola= None

    def __init__(self):
        self.consola = ""
        self.errores = []
        self.Generador3D = Generador3D()

    def imprimir(self,cadena, tipo):
        if tipo:
            self.consola += cadena + " \r\n"
        else:
            self.consola += cadena

    #def ObtenerValor(self,simbolo):
        #return str(simbolo.valor)

    #def ObtenerTipo(self,simbolo):
     #   pass

    #def ObtenerRol(self,simbolo):
     #   pass

    #def ObtenerAmbit(self,ts):
     #   pass