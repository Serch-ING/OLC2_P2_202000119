mod tienda {//Base de datos

    pub mod ventas {//Tabla ventas

        pub struct Venta {
            total: i64,
            cliente: String
        }
       
        // Definición del método de creación de la tabla
        pub fn crear_tabla(mut _tabla: Vec<Venta>, tamanio: usize) -> Vec<Venta> {
            _tabla = Vec::with_capacity(tamanio);
            println!("La tabla ventas ha sido creada");
            return _tabla;
        }



        //Definición de la inserción de datos en la tabla
        pub fn insertar_tabla(mut _tabla: Vec<Venta>, total: i64, cliente: String) -> Vec<Venta> {
            if _tabla.len() < _tabla.capacity() {
                //Insertar un valor nuevo
                let valor: Venta = Venta {
                    total: total,
                    cliente: cliente.to_string()
                };
                _tabla.push(valor);
                println!("Valor nuevo agregado a tabla ventas");
            }
            else {
                println!("La tabla ha llegado a su maxima capacidad");
            }
            return _tabla;
        }

        // Definición de la obtención de un dato según su índice
        pub fn select_venta_por_id(mut _tabla: &Vec<Venta>, id: usize) {
            println!("total: {} cliente: {}", _tabla[id].total, _tabla[id].cliente);
        }

        // Definición de la eliminación de un dato según su índice
        pub fn eliminar_elemento(mut _tabla: Vec<Venta>, id: usize) -> Vec<Venta> {
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
        pub fn editar_elemento(mut _tabla: Vec<Venta>, id: usize, total: i64, cliente: String) -> Vec<Venta> {
            if id >= 0 {
                _tabla[id].total = total;
                _tabla[id].cliente = cliente;
                println!("Valor editado: {}", id);
            }
            else {
                println!("El id debe ser mayor o igual a 0");
            }
            return _tabla
        }
    }
}

fn main() {
    let mut vector: Vec<tienda::ventas::Venta> = Vec::new();

    //Iniciar la tabla
    vector = tienda::ventas::crear_tabla(vector,20);

    //Insertar valores
    vector = tienda::ventas::insertar_tabla(vector,15,"Hector".to_string());
    vector = tienda::ventas::insertar_tabla(vector,54,"Andres".to_string());
    vector = tienda::ventas::insertar_tabla(vector,85,"Luisa".to_string());
    vector = tienda::ventas::insertar_tabla(vector,223,"Pablo".to_string());
    vector = tienda::ventas::insertar_tabla(vector,0864,"Roberto".to_string());
    vector = tienda::ventas::insertar_tabla(vector,12,"Lucia".to_string());
    vector = tienda::ventas::insertar_tabla(vector,1,"Analu".to_string());
    vector = tienda::ventas::insertar_tabla(vector,986,"Maria".to_string());
    vector = tienda::ventas::insertar_tabla(vector,82,"Elizabeth".to_string());
    vector = tienda::ventas::insertar_tabla(vector,67,"Juan".to_string());
    vector = tienda::ventas::insertar_tabla(vector,34,"Sergio".to_string());
    vector = tienda::ventas::insertar_tabla(vector,3,"Lidia".to_string());
    vector = tienda::ventas::insertar_tabla(vector,8200,"Rony".to_string());

    tienda::ventas::select_venta_por_id(&vector,0);
    tienda::ventas::select_venta_por_id(&vector,12);
    tienda::ventas::select_venta_por_id(&vector,4);
    tienda::ventas::select_venta_por_id(&vector,10);
    tienda::ventas::select_venta_por_id(&vector,8);

    vector = tienda::ventas::eliminar_elemento(vector,1);
    vector = tienda::ventas::eliminar_elemento(vector,11);

    tienda::ventas::select_venta_por_id(&vector,0);
    tienda::ventas::select_venta_por_id(&vector,10);
    tienda::ventas::select_venta_por_id(&vector,3);
    tienda::ventas::select_venta_por_id(&vector,9);
    tienda::ventas::select_venta_por_id(&vector,7);

    vector = tienda::ventas::editar_elemento(vector,3,7*3,"Haroldo".to_string());
    vector = tienda::ventas::editar_elemento(vector,2,1234,"Sara".to_string());

    tienda::ventas::select_venta_por_id(&vector,3);
    tienda::ventas::select_venta_por_id(&vector,2);
    tienda::ventas::select_venta_por_id(&vector,5);
    tienda::ventas::select_venta_por_id(&vector,6);
}


/*
La tabla ventas ha sido creada
Valor nuevo agregado a tabla ventas
Valor nuevo agregado a tabla ventas
Valor nuevo agregado a tabla ventas
Valor nuevo agregado a tabla ventas
Valor nuevo agregado a tabla ventas
Valor nuevo agregado a tabla ventas
Valor nuevo agregado a tabla ventas
Valor nuevo agregado a tabla ventas
Valor nuevo agregado a tabla ventas
Valor nuevo agregado a tabla ventas
Valor nuevo agregado a tabla ventas
Valor nuevo agregado a tabla ventas
Valor nuevo agregado a tabla ventas
total: 15 cliente: Hector
total: 8200 cliente: Rony
total: 864 cliente: Roberto
total: 34 cliente: Sergio
total: 82 cliente: Elizabeth
Valor eliminado: 1
Valor eliminado: 11
total: 15 cliente: Hector
total: 3 cliente: Lidia
total: 864 cliente: Roberto
total: 34 cliente: Sergio
total: 82 cliente: Elizabeth
Valor editado: 3
Valor editado: 2
total: 21 cliente: Haroldo
total: 1234 cliente: Sara
total: 1 cliente: Analu
total: 986 cliente: Maria

*/