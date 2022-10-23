
fn main(){
    println!("{}",1+"cadena");
    println!("{}",x);

    if 3 * 6 + 7 {
        println!("Mal");
    }

    if 5 < 6 {
        break;
    }

    parametros_invalidos("Prueba");

    let mut variable1: i64 = 23;
    let mut variable1: f64 = 23.98;

    let mut prueba_tipo: &str = "Cadena";
    prueba_tipo = 87;

    

    let no_mutable: i64 = 7;
    no_mutable = 8;

    //Comprobación dinámica
    let mut arr3: [i64; 4] = [90, 3, 40, 10];
    println!('{}',arr[8]);
    println!('{}',arr[-1]);
    println!('{}',9/0);
    println!('{}',(4 + 7 * 9)/0);
}

fn parametros_invalidos(x: i64) {
    println!("{}",x)
}