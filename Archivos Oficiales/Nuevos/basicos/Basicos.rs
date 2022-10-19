



fn main() {
    
    println!("-----------------------------------");
    println!("----ARCHIVO BASICO SALIDA EN 3D----");
    println!("-----------------------------------");
        
    
    let bo1: bool = false;
    let bol21: bool = !bo1;
    let cad1: String = "imprimir".to_string();
    let cad21: String = "cadena valida".to_string();
    let letra1: char = 'c';
    
    
    let val11 = 10 - (5 + 10 * (9 + 4 * (1 + 2 * 3)) - 8 * 3 * 6) + 5 * (2 * 2);
    let val21 = (2 * 9 * 2 * 2) - 9 - (8 - 16 + (3 * 3 - 6 * 5 - 7 - (9 + 7 * 7 * 7) + 10) - 5) + 8 - (6 - 5 * (2 * 3));
    let val31 = val11 + ((2 + val21 * 3) + 1 - ((2 * 2 * 2) - 2) * 2) - 2;
	
	
    
    let a:i64 = 100;
    let b:i64 = 100;
    let c:i64 = 7;
    let f:bool = true;
    let j:f64 = 10.0;
    let k:f64 = 10.0;
    
	
    let val1:i64 = 5;
    let resp:i64 = 5;
    let mut valorVerdadero : i64 = 100;
	
	
    let x1: i64 = 15;
	
	


    let abs1:i64 = 7-11;
    let abs2:f64 = 10.0;
    let raiz1:i64 = 9;
    let raiz2:f64 = 100.0;
    
    

    
    println!("El valor de val11 es:              {}",val11);
    println!("El valor de val21 es:              {}",val21);
    println!("El valor de val31 es:              {}",val31);
    println!("El resultado de la operación es:  {}",val31);
    println!("El valor de bo1 es:                {}",bo1);
    println!("El valor de cad1 es:               {}",cad1);
    println!("El valor de cad21 es:               {}",cad21);
    println!("El valor de letra1 es:             {}",letra1);
    println!("El valor de bol21:            {}",bol21);
    println!("");
    

    println!("");
    println!("");
    if (a > b || b < c ){
        println!(">>>>>> Esto no debería de imprimirse");
    }else{
        println!(">>>>>> Esto debería de imprimirse")
    }
    
    
    if (a == b && j == k || 14 != c) {
        println!(">>>>>> Esto debería de imprimirse")
    }else{
        println!(">>>>>> Esto no debería de imprimirse");
    }
    
    
    if((valorVerdadero == (50 + 50 + (val1 - val1))) && ! ! ! ! ! ! ! ! ! ! true) {
        println!(">>>>>> En este lugar deberia de entrar :)");
        valorVerdadero = 50;
    }
    else if (f || (valorVerdadero > 50)) && ((resp != 100) && ! ! ! ! ! f){
        println!(">>>>>> Aca no deberia de entrar :ccc");
        valorVerdadero = 70;
    }
    else{
        println!(">>>>>> Aca no deberia de entrar :cccc");
    }

    if x1 % 2 == 0 {
        println!(">>>>> numeroPar ingreso a if verdadero, {} es par",x1);
    }
    else {
        println!(">>>>> numeroPar ingreso a if falso, {} no es par",x1);
    }

    println!("");
    println!("*************PRUEBA DE NATIVAS");
    println!(" valor de b: {:?}",b);
    
    println!(" valor absoluto1: {}",abs1.abs());
    println!(" valor absoluto2: {}",abs2.abs());
    println!(" valor raiz1: {}",(raiz1 as f64).sqrt());
    println!(" valor raiz2: {}",raiz2.sqrt());
    
}


/*

-----------------------------------
----ARCHIVO BASICO SALIDA EN 3D----
-----------------------------------
El valor de val11 es:              -201
El valor de val21 es:              478
El valor de val31 es:              1222
El resultado de la operación es:  1222
El valor de bo1 es:                false
El valor de cad1 es:               imprimir
El valor de cad21 es:               cadena valida
El valor de letra1 es:             c
El valor de bol21:            true



>>>>>> Esto debería de imprimirse
>>>>>> Esto debería de imprimirse
>>>>>> En este lugar deberia de entrar :)
>>>>> numeroPar ingreso a if falso, 15 no es par

*************PRUEBA DE NATIVAS
 valor de b: 100
 valor absoluto1: 4
 valor absoluto2: 10
 valor raiz1: 3
 valor raiz2: 10
*/