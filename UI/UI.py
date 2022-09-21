from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import Analizador.Gramatica as g
from AST.AST_Ejecucion.AST import AST
from AST.Controlador import Controlador
from AST.TablaSimbolos.TablaSimbolos import TablaDeSimbolos
import io
import webbrowser
import os
from AST.TablaErrores import TablaErrores
opcion = ["No data"]
def ventanas():
        global opcion

        ventana = Tk()
        ventana.title('Proyecto 1')
        ventana.geometry("1500x900")


        def cerrar():
            exit()

        def Run_code():
            g.E_list.reiniciar()
            ConsoleTxt.configure(state='normal')
            ConsoleTxt.delete('1.0', END)
            ConsoleTxt.configure(state='disabled')

            f = io.open("../Analizador/entrada.txt", mode="r", encoding="utf-8")
            entrada = f.read()
            # instrucciones = g.parse(entrada)

            CodeText = CodeTxt.get("1.0", 'end-1c')

            #CodeText = entrada
            instrucciones = g.parse(CodeText)


            #messagebox.showinfo(title="Error", message="Ingrese un valor")




            ts = TablaDeSimbolos(None,"Main")
            controlador= Controlador()
            AST_ej = AST(instrucciones)

            consola = AST_ej.EjecutarInstruccion(controlador,ts)
            #print(consola)

            ConsoleTxt.configure(state='normal')
            ConsoleTxt.insert("1.0",consola)
            ConsoleTxt.configure(state='disabled')


        notebook = ttk.Notebook(ventana)
        notebook.pack(fill=BOTH, expand=1)

        s = ttk.Style()
        s.configure('TFrame', background='#949393')

        pes1 = ttk.Frame(notebook)

        notebook.add(pes1, text='Generar Reportes')

        # Pestana 4 ------------------------------------------------------------------------------------
        Label(pes1, text="------------------------------------------------------", font=("Popins", 12)).place(x=10, y=50)

        Button(pes1, text="Salir", command=cerrar).place(x=1400, y=0)

        Label(pes1, text="Codigo", font=("Popins", 12)).place(x=300, y=25)

        Label(pes1, text="Consola",  font=("Popins", 12)).place(x=300, y=575)

        CodeTxt = Text(pes1, width=130, height=30)
        CodeTxt.grid(row=1, column=0)
        CodeTxt.place(x=300, y=60)

        ConsoleTxt = Text(pes1, width=130, height=15)
        ConsoleTxt.grid(row=1, column=0)
        ConsoleTxt.place(x=300, y=600)
        ConsoleTxt.configure(state='disabled')

        Button(pes1, text="💎RUN💎", command=Run_code).place(x=10, y=80)

        def Open_TablaSimbolos():
            filename = '../Reportes/TablaSimbolos.HTML'
            webbrowser.open('file://' + os.path.realpath(filename))

        Button(pes1, text="Tabla de simbolos", command=Open_TablaSimbolos).place(x=10, y=120)

        def Open_TablaErrores():
            filename = '../Reportes/TablaErrores.HTML'
            webbrowser.open('file://' + os.path.realpath(filename))

        Button(pes1, text="Tabla de errores", command=Open_TablaErrores).place(x=10, y=160)


        Button(pes1, text="Tabla de base de datos", command=Run_code).place(x=10, y=200)




        # Terminar ------------------------------------------------------------------------------------

        ventana.mainloop()



if __name__ == "__main__":

    ventanas()
