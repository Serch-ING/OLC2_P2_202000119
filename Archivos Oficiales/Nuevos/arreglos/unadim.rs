/* intercambio */
fn intercambiar(a: &mut [i64], i: usize, j: usize) {
    let aux: i64 = a[i];
    a[i] = a[j];
    a[j] = aux;
}

/* algoritmo de intercambio */
fn ordIntercambio(arr: &mut [i64]) {
    let mut i: usize = 0;
    let mut j: usize = 0;
    
    while i < (arr.len() - 1) {
        j = i + 1;
        while j < arr.len() {
            if arr[i] > arr[j] {
                intercambiar(arr, i, j)
            }
            j = j + 1;
        }
        i = i + 1;
    }
}

/* algoritmo de seleccion */
fn ordSeleccion(arr: &mut [i64]) {
    let mut indiceMenor: usize = 0;
    let mut i: usize = 0;
    let mut j: usize = 0;
    let mut n: usize = arr.len();

    while i < (n - 1) {
        /* comienzo de exploracion indice i */
        indiceMenor = i;
        /* j explora la sublista */
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

/* algoritmo insercion */
fn ordInsercion(arr: &mut [i64]) {
    let mut i: usize = 0;
    let mut j: usize = 0;
    let mut aux: i64 = 0;

    i = 1;
    while (i < arr.len()) {
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
    /*
        Ordenamiento de intercambio
        entrada: [25, 2, 17, 30, 1]
        salida: [1, 2, 17, 25, 30]
    */
    let mut arr1: [i64; 5] = [25, 2, 17, 30, 1];
    ordIntercambio(&mut arr1);
    println!("{:?}", arr1);

    /*
        Ordenamiento de seleccion
        entrada: [5, 20, 8, 17, 65, 2, 40, 4, 35, 90];
        salida: [2, 4, 5, 8, 17, 20, 35, 40, 65, 90]
    */
    let mut arr2: [i64; 10] = [5, 20, 8, 17, 65, 2, 40, 4, 35, 90];
    ordSeleccion(&mut arr2);
    println!("{:?}", arr2);

    /*
        Ordenamiento de insercion
        entrada: [90, 3, 40, 10];
        salida: [3, 10, 40, 90]
    */
    let mut arr3: [i64; 4] = [90, 3, 40, 10];
    ordInsercion(&mut arr3);
    println!("{:?}", arr3);
}

/*
[1, 2, 17, 25, 30]
[2, 4, 5, 8, 17, 20, 35, 40, 65, 90]
[3, 10, 40, 90]
*/