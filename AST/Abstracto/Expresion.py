from abc import ABC,abstractmethod

class Expresion():

    @abstractmethod
    def ObtenerValor(self,controlador,ts):
        pass

    @abstractmethod
    def ObtenerTipo(self,controlador,ts):
        pass
