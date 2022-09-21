mod continental_motores {//Base de datos

    pub mod unidades {//Tabla unidades

        pub struct Unidad {
            pub id: i64,
            pub chasis: String,
            pub placa: String,
            pub color: String,
            pub cliente_id: i64
        }
       
        // Definición del método de creación de la tabla
        pub fn crear_tabla(mut _tabla: Vec<Unidad>, tamanio: usize) -> Vec<Unidad> {
            _tabla = Vec::with_capacity(tamanio);
            println!("La tabla unidades ha sido creada");
            return _tabla;
        }



        //Definición de la inserción de datos en la tabla
        pub fn insertar_tabla(mut _tabla: Vec<Unidad>, id: i64, chasis: String, placa: String, color: String, cliente_id: i64) -> Vec<Unidad> {
            if _tabla.len() < _tabla.capacity() {
                //Insertar un valor nuevo
                let valor: Unidad = Unidad {
                    id: id,
                    chasis: chasis,
                    placa: placa,
                    color: color,
                    cliente_id: cliente_id
                };
                _tabla.push(valor);
                println!("Valor nuevo agregado a tabla unidades");
            }
            else {
                println!("La tabla ha llegado a su maxima capacidad");
            }
            return _tabla;
        }

        // Definición de la obtención de un dato según su índice
        pub fn select_unidad_por_id(mut _tabla: &Vec<Unidad>, id: usize) {
            println!("{} | {} | {} | {} | {}", _tabla[id].id, _tabla[id].chasis, _tabla[id].placa, _tabla[id].color, _tabla[id].cliente_id);
        }

        // Definición de la obtención de un dato según su placa
        pub fn select_unidad_por_placa(mut _tabla: &Vec<Unidad>, placa: String) {
            for valor in _tabla {
                if valor.placa == placa {
                    println!("{} | {} | {} | {} | {}", valor.id, valor.chasis, valor.placa, valor.color, valor.cliente_id);
                }
            }     
        }

        // Definición de la eliminación de un dato según su índice
        pub fn eliminar_elemento(mut _tabla: Vec<Unidad>, id: usize) -> Vec<Unidad> {
            if id >= 0 {
                _tabla.remove(id);
                println!("Valor eliminado: {}", id);
            }
            else {
                println!("El id debe ser mayor o igual a 0");
            }
            return _tabla
        }

        // Definición de la edición de un dato según su índice
        pub fn editar_elemento(mut _tabla: Vec<Unidad>, id: usize, chasis: String, placa: String, color: String, cliente_id: i64) -> Vec<Unidad> {
            if id >= 0 {
                _tabla[id].chasis = chasis;
                _tabla[id].placa = placa;
                _tabla[id].color = color;
                _tabla[id].cliente_id = cliente_id;
                println!("Valor editado: {}", id);
            }
            else {
                println!("El id debe ser mayor o igual a 0");
            }
            return _tabla
        }
    }

    pub mod clientes {//Tabla unidades

        pub struct Cliente {
            pub id: i64,
            pub nombre: String,
            pub telefono: String,
        }
       
        // Definición del método de creación de la tabla
        pub fn crear_tabla(mut _tabla: Vec<Cliente>, tamanio: usize) -> Vec<Cliente> {
            _tabla = Vec::with_capacity(tamanio);
            println!("La tabla clientes ha sido creada");
            return _tabla;
        }

        //Definición de la inserción de datos en la tabla
        pub fn insertar_tabla(mut _tabla: Vec<Cliente>, id: i64, nombre: String, telefono: String) -> Vec<Cliente> {
            if _tabla.len() < _tabla.capacity() {
                //Insertar un valor nuevo
                let valor: Cliente = Cliente {
                    id: id,
                    nombre: nombre,
                    telefono: telefono,
                };
                _tabla.push(valor);
                println!("Valor nuevo agregado a tabla clientes");
            }
            else {
                println!("La tabla ha llegado a su maxima capacidad");
            }
            return _tabla;
        }
    }
}

// Definición de la obtención de un dato según su placa
pub fn select_unidades_por_cliente(mut _tabla: &Vec<continental_motores::clientes::Cliente>, mut _tabla2: &Vec<continental_motores::unidades::Unidad>) {
    for valor_cliente in _tabla {
        println!("{} | {} | {}", valor_cliente.id, valor_cliente.nombre, valor_cliente.telefono);
        for valor_unidad in _tabla2 {
            if valor_cliente.id == valor_unidad.cliente_id {
                println!("    {} | {} | {} | {}", valor_unidad.id, valor_unidad.chasis, valor_unidad.placa, valor_unidad.color);
            }
        }
    }     
}

fn main() {
    let mut vector_clientes: Vec<continental_motores::clientes::Cliente> = Vec::new();
    let mut vector_unidades: Vec<continental_motores::unidades::Unidad> = Vec::new();

    //Iniciar la tabla
    vector_clientes = continental_motores::clientes::crear_tabla(vector_clientes,5);
    vector_unidades = continental_motores::unidades::crear_tabla(vector_unidades,100);

    //Insertar valores
    vector_clientes = continental_motores::clientes::insertar_tabla(vector_clientes,1,"Alex".to_string(),"12234421".to_string());
    vector_clientes = continental_motores::clientes::insertar_tabla(vector_clientes,2,"Jhonny".to_string(),"65445538".to_string());
    vector_clientes = continental_motores::clientes::insertar_tabla(vector_clientes,3,"Pablo".to_string(),"48729776".to_string());

    vector_unidades = continental_motores::unidades::insertar_tabla(vector_unidades,1,"3FK874JKJFSN7".to_string(),"P-018DZK".to_string(),"Azul".to_string(),3);
    vector_unidades = continental_motores::unidades::insertar_tabla(vector_unidades,2,"GGREGEH345BDH".to_string(),"P-219HJL".to_string(),"Rojo metalico".to_string(),2);
    vector_unidades = continental_motores::unidades::insertar_tabla(vector_unidades,3,"TRETEERHRTH76".to_string(),"P-421DHK".to_string(),"Verde".to_string(),1);
    vector_unidades = continental_motores::unidades::insertar_tabla(vector_unidades,4,"FGGEE3553NNM8".to_string(),"P-020XCK".to_string(),"Blanco".to_string(),3);
    vector_unidades = continental_motores::unidades::insertar_tabla(vector_unidades,5,"NVCMDU839NDJC".to_string(),"P-021DHY".to_string(),"Azul".to_string(),2);
    vector_unidades = continental_motores::unidades::insertar_tabla(vector_unidades,6,"123345BDGEGGH".to_string(),"P-022NHT".to_string(),"Negro".to_string(),1);
    vector_unidades = continental_motores::unidades::insertar_tabla(vector_unidades,7,"987654EGEGWRT".to_string(),"P-023GJW".to_string(),"Amarillo".to_string(),2);
    vector_unidades = continental_motores::unidades::insertar_tabla(vector_unidades,8,"NAMNDY642FBNH".to_string(),"P-024ZZZ".to_string(),"Cafe".to_string(),2);
    vector_unidades = continental_motores::unidades::insertar_tabla(vector_unidades,9,"SFGTGRHT67654".to_string(),"P-025FGD".to_string(),"Celeste".to_string(),1);
    vector_unidades = continental_motores::unidades::insertar_tabla(vector_unidades,10,"RFEHR834VSFFF".to_string(),"P-026VZY".to_string(),"Plateado".to_string(),3);

    select_unidades_por_cliente(&vector_clientes, &vector_unidades);

    
}
