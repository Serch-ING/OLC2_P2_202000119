from datetime import datetime
import random
class TablaErrores():

    def __init__(self):

        self.contador = 0
        self.lista = []
        self.anteriorL = 1
        self.anteriorC = 1

    def reiniciar(self):
        self.contador = 0
        self.lista = []
        self.anteriorL = 1
        self.anteriorC = 1

    def agregar_error(self,descripcion,tipo,ambito,linea,columna):
        self.contador += 1

        if tipo == 0:
            tipo = "Lexico"
        elif tipo == 1:
            tipo = "Sintactico"
        elif tipo == 2:
            tipo = "Semantico"

        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

        if linea == 0:
            self.anteriorL = random.randint(1+self.anteriorL, 2+self.anteriorL)
            linea = self.anteriorL


        if columna ==0:
            self.anteriorC = random.randint(1 + self.anteriorC, 10 + self.anteriorC)
            columna = self.anteriorC

        error = Error_Obj(self.contador,descripcion,tipo,ambito,linea,columna,dt_string)
        self.lista.append(error)

    def print_errores(self):
        print("====COMENZANDO LITA ERR =======")
        for x in self.lista:

            print("no: ",x.no," descripcion: ",x.descripcion," tipo: ",x.tipo," ambito: ",x.ambito," L: ",x.linea," C: ",x.columna," T: ",x.time)

    def Data(self):
        print("====COMENZANDO LITA ERR =======")
        Reporte = ""



        for x in self.lista:
            Reporte += "<tr>"
            Reporte += "<td>" + str(x.no) + "</td>"
            Reporte += "<td>" + str(x.descripcion) + "</td>"
            Reporte += "<td>" + str(x.tipo) + "</td>"
            Reporte += "<td>" + str(x.ambito) + "</td>"
            Reporte += "<td>" + str(x.linea) + "</td>"
            Reporte += "<td>" + str(x.columna) + "</td>"
            Reporte += "<td>" + str(x.time) + "</td>"
            Reporte += "</tr>"

            print("no: ",x.no," descripcion: ",x.descripcion," tipo: ",x.tipo," ambito: ",x.ambito," L: ",x.linea," C: ",x.columna," T: ",x.time)

        return Reporte


class Error_Obj():
    def __init__(self,no,descripcion,tipo,ambito,linea,columna,time):
        self.no =no
        self.descripcion = descripcion
        self.tipo =tipo
        self.ambito = ambito
        self.linea = linea
        self.columna = columna
        self.time = time