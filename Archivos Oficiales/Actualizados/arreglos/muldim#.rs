// imprime los puntos por curso de cada estudiante 
fn imprimir_punteo(ests: &mut [String; 4], cursos: &mut [&str; 3], notas: &mut [[[i64;5];3];4]) {
    let ponderacion: [&str; 5] = ["1er parcial", "2do parcial", "3er parcial", "Lab", "Examen final"];
    println!("{:?}", ponderacion);
    println!("");
    for i in 0..ests.len() {
        println!("Estudinte: ");
        println!("{}", ests[i]);
        for j in 0..cursos.len() {
            let cad: String = "Curso: ".to_string() + cursos[j];
            println!("{}", cad);
            println!("{:?}", notas[i][j]);
        }
        println!("");
    }
}

// imprime la nota total por curso de cada estudiante
// parciales 43, lab sobre 32 y examen final 25
fn imprimir_nota_final(ests: &mut [String; 4], cursos: &mut [&str; 3], notas: &mut [[[i64;5];3];4]) {
    for i in 0..ests.len() {
        for j in 0..cursos.len() {
            let mut nota_final: f64 = 0.0;
            for k in 0..notas[i][j].len() {
                let nota: f64 = 
                    if notas[i][j].len() - 1  ==  k{
                        let efinal: f64 = 25.0 / 100.0;
                        (notas[i][j][k] as f64) * efinal
                    } else if notas[i][j].len() - 2  == k {
                        let lab: f64 = 32.0 / 100.0;
                        (notas[i][j][k] as f64) * lab
                    } else {
                        let parcial: f64 = (43.0 / 3.0) / 100.0;
                        (notas[i][j][k] as f64) * parcial
                    };
                nota_final = nota_final + nota;
            }

            let cad: String = ests[i].clone().to_string() + " -> Curso: " + cursos[j];
            println!("{}", cad);
            println!("{}", nota_final);
        }
        println!("");
    }
}

// correccion de notas 
fn corregir_notas(corregir: &mut [[i64;5];3], notas: &mut [[[i64;5];3];4]) {
    for i in 0..notas.len() {
        for j in 0..notas[i].len() {
            for k in 0..notas[i][j].len() {
                notas[i][j][k] = corregir[j][k];
            }
        }
    }
}

fn main () {
    let mut estudiantes: [String; 4] = ["Lorenza".to_string(), "Rosendo".to_string(), "Fermina".to_string(), "Markel".to_string()];
    
    let mut cursos: [&str; 3] = ["Arqui1", "Archivos", "Compi2"];

    let mut notas_buenas: [[i64;5];3] = [
        [53,88,95,89,75],
        [81,51,57,67,93],
        [94,74,58,84,100]
    ];

    let mut notas: [[[i64;5];3];4] = [
        [[37,49,61,29,44],[56,60,51,68,70],[47,15,39,17,74]],
        [[69,74,52,34,36],[24,44,50,18,76],[74,60,32,63,78]],
        [[78,14,23,52,33],[28,79,77,55,24],[23,79,47,62,44]],
        [[73,53,11,49,52],[29,16,65,34,12],[72,69,30,44,37]]
    ];

    println!("\nImprimir notas por curso y estudiantes\n");
    imprimir_punteo(&mut estudiantes, &mut cursos, &mut notas);
    println!("\nImprimir nota final por curso y estudiantes\n");
    imprimir_nota_final(&mut estudiantes, &mut cursos, &mut notas);
    println!("\nMejorar notas de todos los cursos\n");
    corregir_notas(&mut notas_buenas, &mut notas);
    println!("\nImprimir nota final actualizada por curso y estudiantes\n");
    imprimir_nota_final(&mut estudiantes, &mut cursos, &mut notas);
}




/*


Imprimir notas por curso y estudiantes

["1er parcial", "2do parcial", "3er parcial", "Lab", "Examen final"]

Estudinte: 
Lorenza
Curso: Arqui1
[37, 49, 61, 29, 44]
Curso: Archivos
[56, 60, 51, 68, 70]
Curso: Compi2
[47, 15, 39, 17, 74]

Estudinte: 
Rosendo
Curso: Arqui1
[69, 74, 52, 34, 36]
Curso: Archivos
[24, 44, 50, 18, 76]
Curso: Compi2
[74, 60, 32, 63, 78]

Estudinte: 
Fermina
Curso: Arqui1
[78, 14, 23, 52, 33]
Curso: Archivos
[28, 79, 77, 55, 24]
Curso: Compi2
[23, 79, 47, 62, 44]

Estudinte: 
Markel
Curso: Arqui1
[73, 53, 11, 49, 52]
Curso: Archivos
[29, 16, 65, 34, 12]
Curso: Compi2
[72, 69, 30, 44, 37]


Imprimir nota final por curso y estudiantes

Lorenza -> Curso: Arqui1
41.35
Lorenza -> Curso: Archivos
63.19666666666667
Lorenza -> Curso: Compi2
38.41666666666667

Rosendo -> Curso: Arqui1
47.830000000000005
Rosendo -> Curso: Archivos
41.67333333333333
Rosendo -> Curso: Compi2
63.45333333333333

Fermina -> Curso: Arqui1
41.373333333333335
Fermina -> Curso: Archivos
49.973333333333336
Fermina -> Curso: Compi2
52.19666666666667

Markel -> Curso: Arqui1
48.31666666666667
Markel -> Curso: Archivos
29.64666666666667
Markel -> Curso: Compi2
47.84


Mejorar notas de todos los cursos


Imprimir nota final actualizada por curso y estudiantes

Lorenza -> Curso: Arqui1
81.05666666666667
Lorenza -> Curso: Archivos
71.78
Lorenza -> Curso: Compi2
84.27333333333334

Rosendo -> Curso: Arqui1
81.05666666666667
Rosendo -> Curso: Archivos
71.78
Rosendo -> Curso: Compi2
84.27333333333334

Fermina -> Curso: Arqui1
81.05666666666667
Fermina -> Curso: Archivos
71.78
Fermina -> Curso: Compi2
84.27333333333334

Markel -> Curso: Arqui1
81.05666666666667
Markel -> Curso: Archivos
71.78
Markel -> Curso: Compi2
84.27333333333334

*/