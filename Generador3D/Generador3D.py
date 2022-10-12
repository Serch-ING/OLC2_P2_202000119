
class Generador3D:
    def __init__(self):
        self.temporales =0
        self.etiquetas =0
        self.codigo = ""
        self.main = ""
        self.funciones = ""
        self.listafunciones = []

    def obtenerTemporal(self):
        #retorna cadena
        temp = "t"+str(self.temporales)
        self.temporales +=1
        return temp

    def addIntruccion(self,codigo):
        self.codigo  += codigo + '\n'

    def obtenerEtiqueta(self):
        et = "L"+str(self.etiquetas)
        self.etiquetas += 1
        return et

    def generarEncabezado(self):
        encabezado = ""
        encabezado += """
#include <iostream>
#include <cmath>
using namespace std; // Quitar luego
void mostarlista(float pDouble[10000]); // Quitar luego
float Stack[10000];
float Heap[10000];

int SP = 0;
int HP = 0;\n"""
        if self.temporales > 0:
            encabezado += "float "
        for i in range(0, self.temporales):
            if i % 15 == 0 and i > 0:
                encabezado += "\n"
            encabezado += f"t{i}"
            if i < self.temporales - 1:
                encabezado += ","

        if self.temporales > 0:
            encabezado += "; \n\n"

        return encabezado

    def agregarInstruccion(self, codigo):
        self.main += codigo + '\n'
        print(self.main)

    def generarMain(self):
        codigo_SALIDA = self.generarEncabezado()
        codigo_SALIDA += self.codigo + '\n'
        codigo_SALIDA += self.declararfuciones() + "\n\n\n"
        codigo_SALIDA += self.funciones
        codigo_SALIDA += "int main(){ \n" \
                         f"{self.main} \n" \
                         f"\treturn 0;" \
                         "\n}"
        return codigo_SALIDA

    def declararfuciones(self):
        codigo = ""
        for x in self.listafunciones:
            codigo += f'void {x}();\n'
        return  codigo

    def agregarFuncion(self, codigo,identificador):
        self.listafunciones.append(identificador)
        self.funciones += f'void {identificador}()'
        self.funciones += "{\n"
        self.funciones += codigo+"\n"
        self.funciones += "return;\n}"
        self.funciones += "\n\n\n"

    def reiniciarGenerador(self):
        self.etiquetas =0
        self.codigo = ""
        self.temporales = 0
        self.funciones = ""
        self.main = ""
