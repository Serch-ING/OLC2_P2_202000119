class Simbolos() :

    def __init__(self):
        self.linea = 0
        self.columna = 0
        self.id = ""
        self.valor = 0
        self.tipo =  None
        self.mut = False

        self.parametros= []
        self.instrucciones = []

        # simbolo instancia
        self.idClase = ""
        self.entornoInstancia = None

        # simbolo arreglo
        self.valores = []
        self.dimensiones = []

        self.referencia = False

        #simbolo arreglo
        self.withcapacity = 0

    def SimboloPremitivo(self,id,valor,tipo,mut):
        self.id = id
        self.valor = valor
        self.tipo = tipo
        self.mut = mut

    def SimboloFuncion(self,id,parametros,instrucciones,tipo):
        self.id = id
        self.tipo = tipo
        self.parametros = parametros
        self.instrucciones = instrucciones

    def iniciarSimboloClase(self, idClase, listaInstrucciones):
        self.id = idClase
        self.instrucciones = listaInstrucciones

    def iniciarSimboloInstancia(self, idClase, idInstancia, entornoInstancia, tipo):
        self.idClase = idClase
        self.id = idInstancia
        self.entornoInstancia = entornoInstancia
        self.tipo = tipo

    def iniciarSimboloArreglo(self, tipo, dimensiones, valores):
        self.dimensiones = dimensiones
        self.valores = valores
        self.tipo = tipo

    def iniciarSimboloVector(self, tipo, dimensiones, valores):
        self.dimensiones = dimensiones
        self.valores = valores
        self.tipo = tipo

    def Asignar_valor(self, valor):
        self.valor = valor