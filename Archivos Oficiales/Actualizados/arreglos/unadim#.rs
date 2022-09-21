// intercambio 
fn intercambiar(a: &mut [i64], i: usize, j: usize) {
    let aux: i64 = a[i];
    a[i] = a[j];
    a[j] = aux;
}

// algoritmo de intercambio 
fn ordIntercambio(arr: &mut [i64]) {
    let mut i: usize = 0;
    let mut j: usize = 0;
    
    while i < (arr.len() - 1) {
        j = i + 1;
        while j < (arr.len()) {
            if arr[i] > arr[j] {
                intercambiar(arr, i, j);
            }
            j = j + 1;
        }
        i = i + 1;
    }
}

// algoritmo de seleccion 
fn ordSeleccion(arr: &mut [i64]) {
    let mut indiceMenor: usize = 0;
    let mut i: usize = 0;
    let mut j: usize = 0;
    let mut n: usize = arr.len();

    while i < (n - 1) {
        // comienzo de exploracion indice i 
        indiceMenor = i;
        // j explora la sublista 
        j = i + 1;
        while j < n {
            if arr[j] < arr[indiceMenor] {
                indiceMenor = j;
            }
            j = j + 1;
        }

        if i != indiceMenor {
            intercambiar(arr, i, indiceMenor);
        }

        i = i + 1;
    }
}

// algoritmo insercion 
fn ordInsercion(arr: &mut [i64]) {
    let mut i: usize = 0;
    let mut j: usize = 0;
    let mut aux: i64 = 0;

    i = 1;
    while (i < (arr.len())) {
        j = i;
        aux = arr[i];

        while j > 0 && aux < arr[j-1] {
            arr[j] = arr[j - 1];
            j = j - 1;
        }
        
        arr[j] = aux;
        i = i + 1;
    }
}

fn main () {
    
    //    Ordenamiento de intercambio
    //    entrada: [8, 4, 6, 2]
    //    salida: [2, 4, 6, 8]
    
    let mut arr1: [i64; 4] = [8, 4, 6, 2];
    ordIntercambio(&mut arr1);
    println!("{:?}", arr1);

    
    //    Ordenamiento de seleccion
    //    entrada: [40, 21, 1, 3, 14, 4];
    //    salida: [1, 3, 4, 14, 21, 40]
    
    let mut arr2: [i64; 6] = [40, 21, 1, 3, 14, 4];
    ordSeleccion(&mut arr2);
    println!("{:?}", arr2);

    
    //    Ordenamiento de insercion
    //    entrada: [90, 3, 40, 10, 8, 5];
    //    salida: [3, 5, 8, 10, 40, 90]
    
    let mut arr3: [i64; 6] = [90, 3, 40, 10, 8, 5];
    ordInsercion(&mut arr3);
    println!("{:?}", arr3);
}


/*

[2, 4, 6, 8]
[1, 3, 4, 14, 21, 40]
[3, 5, 8, 10, 40, 90]

*/