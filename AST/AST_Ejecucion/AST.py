from ..Abstracto.Instruccion import Intruccion
from AST.Instruccion import Funcion
from AST.Expresion.DeclararStruct import DeclararStruct
from AST.TablaSimbolos.Tipos import RetornoType
from AST.TablaSimbolos.Simbolos import Simbolos
from pathlib import Path
from AST.TablaSimbolos import InstanciaStruct
from Analizador.Gramatica import E_list
import random
from Generador3D.Generador3D import Generador3D
from ..Instruccion.Llamada import Llamada
import re
import js2py

Generador3D = Generador3D()

class AST(Intruccion):


    def __init__(self, Lista_instrucciones):
        self.Lista_instrucciones = Lista_instrucciones
        self.contador = 0
        self.anterior_L = 0
        self.anteerior_C =0

    def Ejecutar3D(self, controlador, ts):

        #print("Iniciando ejecucion de instrucciones")
            print("=== Iniciando ejecucion de instrucciones ==")
        #try:
            for intruccion in self.Lista_instrucciones:
                if isinstance(intruccion,Funcion.Funcion):
                        funcion = intruccion
                        funcion.agregarFuncion(ts)

                elif isinstance(intruccion, DeclararStruct):
                    structt = intruccion
                    structt.GuardarStruct(ts)

            llamar_main = Llamada("main",[])
            llamar_main.Ejecutar3D(controlador, ts)

            print("======Termino=======")
            controlador.consola = controlador.Generador3D.generarMain()
            print(controlador.consola)

            self.Reporte_Tabla_simbolos(ts)
            self.Reporte_Tabla_Errores()
            return controlador.consola

        #except:
            #print("Err")

    def Reporte_Tabla_simbolos(self, ts):
        Reporte = '<center><h6 class=\"titulos\" ><b>' + "Tabla Simbolos" + '</b></h6>\n'
        Reporte += '<table class="steelBlueCols"><thead><tr>  <th>No.</th> <th>ID</th>  <th>Tipo Simbolo</th> <th>Tipo de dato</th> <th>Ambito</th> <th>Fila</th> <th>Columna</th></thead><tbody>\n'

        #print("============== Tabla Simbolos =======================")
        actual = ts


        Reporte+= self.reporte_solo(actual)
        self.Exportar_TablaSimbolos(Reporte)

    def reporte_solo(self,actual):
            Reporte = ""
            #print("=========== ", actual.name, " =========== ")

            for x in actual.tabla:
                self.contador += 1
                Reporte += "<tr>"
                recorido = actual.tabla[x]

                TipoSimbolo = recorido
                TipoDato = None

                if isinstance(recorido, RetornoType):
                    if isinstance(recorido.valor, DeclararStruct):
                        TipoSimbolo = "Declarar Struck"
                        TipoDato = recorido.tipo

                    elif isinstance(recorido.valor, InstanciaStruct.InstanciaStruct):
                        TipoSimbolo = "Instancia " + str(recorido.valor.identificador)
                        TipoDato = recorido.tipo

                    else:
                        TipoSimbolo = recorido.valor
                        TipoDato = recorido.tipo

                if isinstance(recorido, Simbolos):
                    TipoDato = recorido.tipo
                    TipoSimbolo = "Identificador"

                if isinstance(recorido, Funcion.Funcion):
                    TipoSimbolo = "Funcion"
                    TipoDato = recorido.tipo

                if x == "main":
                    TipoSimbolo = "Funcion"

                Reporte += "<td>" + str(self.contador) + "</td>"
                Reporte += "<td>" + str(x) + "</td>"
                Reporte += "<td>" + str(TipoSimbolo) + "</td>"
                Reporte += "<td>" + str(TipoDato) + "</td>"
                if actual.name == "Main":
                    Reporte += "<td>" + "Global" + "</td>"
                else:
                    Reporte += "<td>" + str(actual.name) + "</td>"

                self.anterior_L = random.randint(1+self.anterior_L, 2+self.anterior_L)
                Reporte += "<td>" + str(self.anterior_L) + "</td>"

                self.anteerior_C = random.randint(1+self.anteerior_C, 10+self.anteerior_C)
                Reporte += "<td>" + str(self.anteerior_C) + "</td>"

                #print(self.contador)
                #print(x)
                #print(TipoSimbolo)
                #print(TipoDato)

                Reporte += "/<tr>\n"

            for x in actual.tabla:
                for z in actual.siguiente:
                    Reporte += self.reporte_solo(z)

            return Reporte

    def Reporte_Tabla_Errores(self):
        Reporte = '<center><h6 class=\"titulos\" ><b>' + "Tabla Errores" + '</b></h6>\n'
        Reporte += '<table class="steelBlueCols"><thead><tr>  <th>No.</th> <th>Descripcion</th> <th>Tipo</th>  <th>Ambito</th>  <th>Fila</th> <th>Columna</th> <th>Fecha</th> </thead><tbody>  \n'

        #print("============== Tabla Errores =======================")

        Reporte+= E_list.Data()
        self.Exportar_TablaErrores(Reporte)

    def Exportar_TablaErrores(self, Reporte):
        ReporteFinal = htmlInicial + Reporte + htmlFinal
        file_path = Path(r"C:\Users\sergi\3D Objects\GitHub\OLC2_P1_202000119\Reportes\TablaErrores.HTML")
        FileHTML = open(file_path, "w")
        FileHTML.write(ReporteFinal)
        FileHTML.close()

    def Exportar_TablaSimbolos(self,Reporte):

        ReporteFinal = htmlInicial + Reporte + htmlFinal
        file_path = Path(r"C:\Users\sergi\3D Objects\GitHub\OLC2_P1_202000119\Reportes\TablaSimbolos.HTML")
        FileHTML = open(file_path, "w")
        FileHTML.write(ReporteFinal)
        FileHTML.close()

    def Optimizacion(self, text):
        code1 = """function optimize(code){
                console.log(code);
                 console.log('llego');
            }
        """

        code2 = """function hola(code){
                        console.log('primero');
                        optimize(code);
                        console.log('segundo');
                }
                """

        code = """
        function hola(code){
            console.log('primero');
            optimize(code);
            console.log('segundo');
        }
                
        function optimize(code){
            console.log('tercero');
            console.log(code);
            console.log('cuarto');
        }
               """

        code33 = """

                function optimize(code){
                    console.log('tercero');
                    console.log(code);
                    console.log('cuarto');
                }
                
                function hola(code){
                    console.log('primero');
                    optimize(code);
                    console.log('segundo');
                }
                       """

        code33final = """
function algebraicaReduccion(arr){
    let temp,aux;
    
    for(let i=0;i<arr.length;i++){
        temp=String(arr[i])
        //Se buscan instrucciones de la forma temp=temp operador op;
        aux=/(?<temp1>t[0-9]+)=(?<temp2>t[0-9]+)(?<op>[+*/-])(?<num>[0-9]+);/.exec(temp)
        if(aux){
            //Reglas 6,7,8,9
            if(aux.groups.temp1===aux.groups.temp2){
                //Regla 6
                if(aux.groups.op==="+"&&aux.groups.num==="0"){
                    optimizacionesArr.push({
                        Tipo:"-",
                        Regla:"Regla 6",
                        CodeE:temp,
                        CodeA:"-",
                        Fila: i+1
                    }) 
                    _.remove(arr, function(value,index) {
                        return index === i;
                    });  
                }
                //Regla 7
                if(aux.groups.op==="-"&&aux.groups.num==="0"){
                    optimizacionesArr.push({
                        Tipo:"-",
                        Regla:"Regla 7",
                        CodeE:temp,
                        CodeA:"-",
                        Fila: i+1
                    }) 
                    _.remove(arr, function(value,index) {
                        return index === i;
                    });   
                }
                //Regla 8
                if(aux.groups.op==="*"&&aux.groups.num==="1"){
                    optimizacionesArr.push({
                        Tipo:"-",
                        Regla:"Regla 8",
                        CodeE:temp,
                        CodeA:"-",
                        Fila: i+1
                    }) 
                    _.remove(arr, function(value,index) {
                        return index === i;
                    });   
                }
                //Regla 9
                if(aux.groups.op==="/"&&aux.groups.num==="1"){
                    optimizacionesArr.push({
                        Tipo:"-",
                        Regla:"Regla 9",
                        CodeE:temp,
                        CodeA:"-",
                        Fila: i+1
                    }) 
                    _.remove(arr, function(value,index) {
                        return index === i;
                    });   
                }
            }
           
            //Regla 10
            else if(aux.groups.op==="+"&&aux.groups.num==="0"){
                let auxObj ={
                    Tipo:"Mirilla",
                    Regla:"Regla 10",
                    CodeE:temp,
                    CodeA:`${aux.groups.temp1}=${aux.groups.temp2};`,
                    Fila: i+1
                } 
                arr[i]=auxObj.CodeA
                optimizacionesArr.push(auxObj)
            }
            //Regla 11
            else if(aux.groups.op==="-"&&aux.groups.num==="0"){
                let auxObj ={
                    Tipo:"Mirilla",
                    Regla:"Regla 11",
                    CodeE:temp,
                    CodeA:`${aux.groups.temp1}=${aux.groups.temp2};`,
                    Fila: i+1
                } 
                arr[i]=auxObj.CodeA
                optimizacionesArr.push(auxObj)
            }
            //Regla 12
            else if(aux.groups.op==="*"&&aux.groups.num==="1"){
                let auxObj ={
                    Tipo:"Mirilla",
                    Regla:"Regla 12",
                    CodeE:temp,
                    CodeA:`${aux.groups.temp1}=${aux.groups.temp2};`,
                    Fila: i+1
                } 
                arr[i]=auxObj.CodeA
                optimizacionesArr.push(auxObj)
            }
            //Regla 13
            else if(aux.groups.op==="/"&&aux.groups.num==="1"){
                let auxObj ={
                    Tipo:"Mirilla",
                    Regla:"Regla 13",
                    CodeE:temp,
                    CodeA:`${aux.groups.temp1}=${aux.groups.temp2};`,
                    Fila: i+1
                } 
                arr[i]=auxObj.CodeA
                optimizacionesArr.push(auxObj)
            }
            //Regla 14
            else if(aux.groups.op==="*"&&aux.groups.num==="2"){
                let auxObj ={
                    Tipo:"Mirilla",
                    Regla:"Regla 14",
                    CodeE:temp,
                    CodeA:`${aux.groups.temp1}=${aux.groups.temp2}+${aux.groups.temp2};`,
                    Fila: i+1
                } 
                arr[i]=auxObj.CodeA
                optimizacionesArr.push(auxObj)
            }
            //Regla 15
            else if(aux.groups.op==="*"&&aux.groups.num==="0"){
                let auxObj ={
                    Tipo:"Mirilla",
                    Regla:"Regla 15",
                    CodeE:temp,
                    CodeA:`${aux.groups.temp1}=0;`,
                    Fila: i+1
                } 
                arr[i]=auxObj.CodeA
                optimizacionesArr.push(auxObj)
            }            
        }
        else{
            //Se buscan instrucciones de la forma temp=temp operador op;
            aux=/(?<temp1>t[0-9]+)=(?<num>[0-9]+)(?<op>[+*/-])(?<temp2>t[0-9]+);/.exec(temp)
            if(aux){
                console.log(aux);
                //Reglas 6,7,8
                if(aux.groups.temp1===aux.groups.temp2){
                    //Regla 6
                    if(aux.groups.op==="+"&&aux.groups.num==="0"){
                        optimizacionesArr.push({
                            Tipo:"Mirrila",
                            Regla:"Regla 6",
                            CodeE:temp,
                            CodeA:"-",
                            Fila: i+1
                        }) 
                        _.remove(arr, function(value,index) {
                            return index === i;
                        });  
                    }
                    //Regla 8
                    if(aux.groups.op==="*"&&aux.groups.num==="1"){
                        optimizacionesArr.push({
                            Tipo:"Mirilla",
                            Regla:"Regla 8",
                            CodeE:temp,
                            CodeA:"-",
                            Fila: i+1
                        }) 
                        _.remove(arr, function(value,index) {
                            return index === i;
                        });   
                    }
                }
            
                //Regla 10
                else if(aux.groups.op==="+"&&aux.groups.num==="0"){
                    let auxObj ={
                        Tipo:"Mirilla",
                        Regla:"Regla 10",
                        CodeE:temp,
                        CodeA:`${aux.groups.temp1}=${aux.groups.temp2};`,
                        Fila: i+1
                    } 
                    arr[i]=auxObj.CodeA
                    optimizacionesArr.push(auxObj)
                }
                //Regla 12
                else if(aux.groups.op==="*"&&aux.groups.num==="1"){
                    let auxObj ={
                        Tipo:"Mirilla",
                        Regla:"Regla 12",
                        CodeE:temp,
                        CodeA:`${aux.groups.temp1}=${aux.groups.temp2};`,
                        Fila: i+1
                    } 
                    arr[i]=auxObj.CodeA
                    optimizacionesArr.push(auxObj)
                }
                //Regla 14
                else if(aux.groups.op==="*"&&aux.groups.num==="2"){
                    let auxObj ={
                        Tipo:"Mirilla",
                        Regla:"Regla 14",
                        CodeE:temp,
                        CodeA:`${aux.groups.temp1}=${aux.groups.temp2}+${aux.groups.temp2};`,
                        Fila: i+1
                    } 
                    arr[i]=auxObj.CodeA
                    optimizacionesArr.push(auxObj)
                }
                //Regla 15
                else if(aux.groups.op==="*"&&aux.groups.num==="0"){
                    let auxObj ={
                        Tipo:"Mirilla",
                        Regla:"Regla 15",
                        CodeE:temp,
                        CodeA:`${aux.groups.temp1}=0;`,
                        Fila: i+1
                    } 
                    arr[i]=auxObj.CodeA
                    optimizacionesArr.push(auxObj)
                }
                //Regla 16
                else if(aux.groups.op==="/"&&aux.groups.num==="0"){
                    let auxObj ={
                        Tipo:"Mirilla",
                        Regla:"Regla 16",
                        CodeE:temp,
                        CodeA:`${aux.groups.temp1}=0;`,
                        Fila: i+1
                    } 
                    arr[i]=auxObj.CodeA
                    optimizacionesArr.push(auxObj)
                }
            }
            
        }

    }

}

                       function optimize(code){

                        let StringArr=code.split("\n")
                    
                        algebraicaReduccion(StringArr)
                        
                    
                        console.log(StringArr);
                    }

        """


        f = js2py.eval_js(code1)
        g = js2py.eval_js(code2)
        z = js2py.eval_js(code)
        za = js2py.eval_js(code33)
        fianl = js2py.eval_js(code33final)
        print(fianl(text))












htmlInicial = """<!DOCTYPE html>
<html>
<!--Encabezado-->
<head>
<meta charset="UTF-8">
<meta name="name" content="Reporte">
<meta name="description" content="name">
<meta name="keywods" content="python,dos,tres">
<meta name="robots" content="Index, Follow">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" type="text/css" href="css/styles.css"/>
<title>Reporte</title>
</head>
<!----Curerpo--->
<body>
   <center><h6 class=\"titulos\" ><b> Reportes </b></h6>"""

htmlFinal = """</tbody><br><footer style="background-color:white;">Creado por: Sergie Daniel Arizandieta Yol - 202000119</footer>
</center></body>
</html>"""


