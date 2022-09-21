from abc import ABC,abstractmethod

class Intruccion:

    @abstractmethod
    def EjecutarInstruccion(self,controlador,ts):
        pass