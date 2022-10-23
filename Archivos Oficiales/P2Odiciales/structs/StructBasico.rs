struct StructArr {
    datos: [i64; 10]
}

struct CentroTuristico {
    nombre:String
}

struct Carro {
    placa: String,
    color: String,
    tipo: String
}

struct Personaje {
    nombre: String,
    edad: i64,
    descripcion: String,
    carro_: Carro,
    numeros : StructArr
}
// Struct



fn main(){

    println!("*******************VECTOR CON STRUCTS");
    
    let mut v: Vec<CentroTuristico> = Vec::with_capacity(8);
    
    v.push(CentroTuristico{nombre:"Cascada los amantes".to_string()} );
    v.push(CentroTuristico{nombre:"Biotopo del quetzal".to_string()} );
    v.push(CentroTuristico{nombre:"Tikal".to_string()} );
    v.push(CentroTuristico{nombre:"Rio dulce".to_string()} );
    v.push(CentroTuristico{nombre:"Laguna ROJA".to_string()} );
    v.push(CentroTuristico{nombre:"Playa Blanca".to_string()} );
    v.push(CentroTuristico{nombre:"Antigua Guatemala".to_string()} );
    v.push(CentroTuristico{nombre:"Lago de Atitlan".to_string()} );
    
    for valor in v {
        println!("El nombre del Centro turistico es: {}",valor.nombre);
    }
        
    
    println!("*******************STRUCT CON ARRAY"); 
    
    let mut da = StructArr {
        datos: [10; 10]
    };
    
    println!(" valor {:?} ",da.datos);
    
    
    println!("*******************CREANDO STRUCTS ");
    
    let mut p1 = Personaje { 
        nombre:"Fer".to_string(),
        edad:18,
        descripcion:"No hace nada".to_string(),
        carro_: Carro { placa:"150PLO".to_string(),
                        color:"Rojo".to_string(), 
                        tipo:"Automatico".to_string() 
            
        },
        numeros: da
    };
    
    let per1 = CreandoPersonaje(200,2,true);
    let per2 = CreandoPersonaje(201,1,true);
    let per3 = CreandoPersonaje(300,3,false);
    
    
    println!("Persona <<per1>> nombre: {}, edad: {}, carroTipo: {}, carroColor: {} ",per1.nombre, per1.edad, per1.carro_.tipo,per1.carro_.color);
    println!("Persona <<per2>> nombre: {}, edad: {}, carroTipo: {}, carroColor: {} ",per2.nombre, per2.edad, per2.carro_.tipo,per2.carro_.color);
    println!("Persona <<per3>> nombre: {}, edad: {}, carroTipo: {}, carroColor: {} ",per3.nombre, per3.edad, per3.carro_.tipo,per3.carro_.color);


}

fn CreandoPersonaje (anio: i64, color: i64, mecanico: bool) -> Personaje{

    let mut datos = StructArr {
        datos: [10; 10]
    };

    let mut car = CreandoStruct(anio,color,mecanico);
    
    let mut p1 = Personaje { 
        nombre:"Fer".to_string(),
        edad:18,
        descripcion:"No hace nada".to_string(),
        carro_: car,
        numeros:datos
    };
    
    return p1;
}


fn CreandoStruct ( anio: i64, color: i64, mecanico: bool) ->  Carro{

    let mut placa_: String = "".to_string();

    /* Ejemplo 1: Match como instrucción */
    // Después del match sigue una expresión
    match anio {
        // 1 | 2 | 3 estas son coincidencias
        1200 | 2001 | 3002 => {
            placa_ = "20012PLO0".to_string();
        } //esto se conoce como brazo
        
        4003 | 204 | 5005 => placa_ = "200345LO0".to_string(),//esto se conoce como brazo
        7006 =>  placa_ = "290PLO0".to_string(), // esto es un error!
        _ => println!("Resto de casos"), //brazo por defecto
    }
    
    /*  Match como expresión */
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
*******************VECTOR CON STRUCTS
El nombre del Centro turistico es: Cascada los amantes
El nombre del Centro turistico es: Biotopo del quetzal
El nombre del Centro turistico es: Tikal
El nombre del Centro turistico es: Rio dulce
El nombre del Centro turistico es: Laguna ROJA
El nombre del Centro turistico es: Playa Blanca
El nombre del Centro turistico es: Antigua Guatemala
El nombre del Centro turistico es: Lago de Atitlan
*******************STRUCT CON ARRAY
 valor [10, 10, 10, 10, 10, 10, 10, 10, 10, 10] 
*******************CREANDO STRUCTS 
Resto de casos
Resto de casos
Resto de casos
Persona <<per1>> nombre: Fer, edad: 18, carroTipo: mecanico, carroColor: verde 
Persona <<per2>> nombre: Fer, edad: 18, carroTipo: mecanico, carroColor: amarillo 
Persona <<per3>> nombre: Fer, edad: 18, carroTipo: Automatico, carroColor: rojo 
*/