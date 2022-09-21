
struct Carro {
    placa: String,
    color: String,
    tipo: String
}

struct Personaje {
    nombre: String,
    edad: i64,
    descripcion: String,
    carro_: Carro
}
// Struct



fn main (){

    
    println!("*******************CREANDO STRUCTS ");
    
    let mut p1 = Personaje { 
        nombre:"Fer".to_string(),
        edad:18,
        descripcion:"No hace nada".to_string(),
        carro_: Carro { placa:"090PLO".to_string(),
                        color:"gris".to_string(), 
                        tipo:"mecanico".to_string() 
            
        }
    };
    
    let per1 = CreandoPersonaje(2000,2,true);
    let per2 = CreandoPersonaje(2007,2,true);
    let per3 = CreandoPersonaje(2000,3,false);
    
    
    println!("Persona <<per1>> nombre: {}, edad: {}, carroTipo: {}, carroColor: {} ",per1.nombre, per1.edad, per1.carro_.tipo,per1.carro_.color);
    println!("Persona <<per2>> nombre: {}, edad: {}, carroTipo: {}, carroColor: {} ",per2.nombre, per2.edad, per2.carro_.tipo,per2.carro_.color);
    println!("Persona <<per3>> nombre: {}, edad: {}, carroTipo: {}, carroColor: {} ",per3.nombre, per3.edad, per3.carro_.tipo,per3.carro_.color);


}

fn CreandoPersonaje (anio: i64, color: i64, mecanico: bool) -> Personaje{


    let mut car = CreandoStruct(anio,color,mecanico);
    
    let mut p1 = Personaje { 
        nombre:"Fer".to_string(),
        edad:18,
        descripcion:"No hace nada".to_string(),
        carro_: car
    };
    
    return p1;
}


fn CreandoStruct ( anio: i64, color: i64, mecanico: bool) ->  Carro{

    let mut placa_: String = "".to_string();

    // Ejemplo 1: Match como instrucción 
    // Después del match sigue una expresión
    match anio {
        // 1 | 2 | 3 estas son coincidencias
        2000 | 2001 | 2002 => {
            placa_ = "20012PLO0".to_string();
        } //esto se conoce como brazo
        
        2003 | 2004 | 2005 => placa_ = "200345LO0".to_string(),//esto se conoce como brazo
        2006 =>  placa_ = "20090PLO0".to_string(), // esto es un error!
        _ => println!("Resto de casos"), //brazo por defecto
    }
    
    //  Match como expresión 
    let colorAuto = match color {
        1 => "amarillo",
        2 => "verde",
        3 => "rojo",
        4 => "azul",
        5 => "negro",
        _ => "N/A",
    };

    let mut tipo : String = "".to_string();
    if mecanico {
        tipo = "mecanico".to_string(); 
    }
    else{
        tipo = "Automatico".to_string();
    }

    return Carro { placa: placa_,
                    color:colorAuto.to_string(), 
                    tipo:tipo
        
    };
}



/*
*******************CREANDO STRUCTS 
Resto de casos
Persona <<per1>> nombre: Fer, edad: 18, carroTipo: mecanico, carroColor: verde 
Persona <<per2>> nombre: Fer, edad: 18, carroTipo: mecanico, carroColor: verde 
Persona <<per3>> nombre: Fer, edad: 18, carroTipo: Automatico, carroColor: rojo 



*/