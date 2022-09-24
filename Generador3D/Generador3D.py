
class Generador3D:
    def __init__(self):
        self.temporales =0
        self.etiquetas =0
        self.codigo = ""

    def obtenerTemporal(self):
        #retorna cadena
        temp = "t"+str(self.temporales)
        self.temporales +=1
        return temp

    def obtenerEtiqueta(self):
        et = "L"+str(self.etiquetas)
        self.etiquetas += 1
        return et

    def genrarEncabezado(self):
        encabezado = ""
        encabezado += """
        
            #include <iostream>
            float stack[10000];
            float heap[10000];
            
            int sp = 0;
            int hp = 0;

        """

    def genrarMain(self):
        pass

    def reiniciarGenerador(self):
        self.etiquetas =0
        self.codigo = ""
        self.temporales = 0