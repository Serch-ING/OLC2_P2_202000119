class Controlador:
    consola= None

    def __init__(self):
        self.consola = ""
        self.errores = []

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