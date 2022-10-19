
struct Apuntadores {
    right : i64,
    left : i64
}

struct Node {
    idx : i64,
    val : i64,
    point : Apuntadores
}

struct StructValores{
    first: i64,
    last:i64,
    count:i64
}


fn InsertFirst(val : i64, actualDL : &mut Vec<Node>, valores: &mut StructValores){


    
    if (valores.first !=  -1) {
    
        let indice = actualDL[valores.first as usize].idx;
    
        valores.first = valores.count;

        actualDL[valores.first as usize].val = val;
        actualDL[valores.first as usize].idx = valores.first;
        
        
        actualDL[valores.first as usize].point.left = -1;
        actualDL[valores.first as usize].point.right = indice;
        

        actualDL[indice as usize].point.left = valores.first ;
    
    } else{
        valores.first = valores.count;
        valores.last = valores.first;
        
            
        //let ind:usize = valores.count as usize;
        actualDL[valores.count as usize].idx = valores.count;
        actualDL[valores.count as usize].val = val;
        actualDL[valores.count as usize].point.left = -1;
        actualDL[valores.count as usize].point.right = -1;
        
    }
    
    
    
    
    valores.count = valores.count + 1;
	

}


fn InsertLast(val : i64, actualDL : &mut Vec<Node>, valores: &mut StructValores){


    
    if (valores.first !=  -1) {
    
        let indice = actualDL[valores.last as usize].idx;
    
        valores.last = valores.count;

        actualDL[valores.last as usize].val = val;
        actualDL[valores.last as usize].idx = valores.last;
        
        
        actualDL[valores.last as usize].point.left = indice;
        actualDL[valores.last as usize].point.right = -1;
        

        actualDL[indice as usize].point.right = valores.count ;
    
    } else{
        valores.first = valores.count;
        valores.last = valores.first;
        
            
        //let ind:usize = valores.count as usize;
        actualDL[valores.count as usize].idx = valores.count;
        actualDL[valores.count as usize].val = val;
        actualDL[valores.count as usize].point.left = -1;
        actualDL[valores.count as usize].point.right = -1;
        
    }
    
    
    
    
    valores.count = valores.count + 1;
	

}



fn InsertInto(val : i64, pos:i64, actualDL : &mut Vec<Node>, valores: &mut StructValores){

 
    let mut i : i64 = 0;

    if (valores.first == -1) || (pos == 0){
        InsertFirst(val,actualDL,valores);
    }else if ((valores.count - 1) == pos) {
        InsertLast(val,actualDL,valores);
    } else{
        
        // root = actualDL[first];
        
        //root
        let mut indice:i64 = actualDL[valores.first as usize].idx;
        let mut auxIndice = 0;
        let mut rootIndice:i64 = indice;
        

        loop {
            
            auxIndice = actualDL[rootIndice as usize].idx;
            let otro:i64 = actualDL[rootIndice as usize].point.right;
            rootIndice = actualDL[otro as usize].idx;
            i = i + 1;
            if i == pos {
                break
            }
        }
        
       
        let posicionNueva = valores.count;
 
        actualDL[auxIndice as usize].point.right = posicionNueva;

 
        actualDL[rootIndice as usize].point.left = posicionNueva ;

        actualDL[valores.count as usize].idx = valores.count;
        actualDL[valores.count as usize].val = val;
        actualDL[valores.count as usize].point.left = auxIndice;
        actualDL[valores.count as usize].point.right = rootIndice;
        
        valores.count = valores.count + 1;
    }
}




fn PrintListNormal(actualDL : &mut Vec<Node>, valores: &mut StructValores){


    if (valores.first !=  -1){
        let mut i = valores.first;
        let mut actual = 0;
        loop{
            actual = actualDL[i as usize].idx;
            println!("Val|| de nodo: {} ", actualDL[actual as usize].val);
            i = actualDL[actual as usize].point.right;
            
            
            if actual == valores.last{
                break;
            }
            
        }
    }
    
}


fn PrintListBack(actualDL : &mut Vec<Node>, valores: &mut StructValores){


    if (valores.first !=  -1){
        let mut i = valores.last;
        let mut actual = 0;
        loop{
            actual = actualDL[i as usize].idx;
            println!("Val|| de nodo: {} ", actualDL[actual as usize].val);
            i = actualDL[actual as usize].point.left;
            
            
            if actual == valores.first{
                break;
            }
            
        }
    }
    
}



fn main(){


    let mut actualDL: Vec<Node> = Vec::with_capacity(10);
    
    actualDL.push(Node{idx :0,val:0, point:Apuntadores{left:0,right:0}});
    actualDL.push(Node{idx :0,val:0, point:Apuntadores{left:0,right:0}});
    actualDL.push(Node{idx :0,val:0, point:Apuntadores{left:0,right:0}});
    actualDL.push(Node{idx :0,val:0, point:Apuntadores{left:0,right:0}});
    actualDL.push(Node{idx :0,val:0, point:Apuntadores{left:0,right:0}});
    actualDL.push(Node{idx :0,val:0, point:Apuntadores{left:0,right:0}});
    actualDL.push(Node{idx :0,val:0, point:Apuntadores{left:0,right:0}});
    actualDL.push(Node{idx :0,val:0, point:Apuntadores{left:0,right:0}});
    actualDL.push(Node{idx :0,val:0, point:Apuntadores{left:0,right:0}});
    actualDL.push(Node{idx :0,val:0, point:Apuntadores{left:0,right:0}});

        
    let mut refs: StructValores = StructValores{first:-1,count:0,last:-1};
    
    
    println!("Primero: {},  Ultimo: {}, Tamaño: {}",  refs.first,refs.last, refs.count);
    
    println!("---Insertar al inicio---");
    InsertFirst(133, &mut actualDL, &mut refs);
    println!("---Insertar al final---");
    InsertLast(1, &mut actualDL, &mut refs);
    println!("---Insertar al inicio---");
    InsertFirst(3, &mut actualDL, &mut refs);
    println!("---Insertar en posicion 2---");
    InsertInto(35,2, &mut actualDL, &mut refs);
    println!("---Insertar al inicio---");
    InsertFirst(66, &mut actualDL, &mut refs);
    println!("---Insertar al final---");
    InsertLast(53, &mut actualDL, &mut refs);
    println!("---Insertar al inicio---");
    InsertFirst(78, &mut actualDL, &mut refs);
    println!("---Insertar en posicion 4---");
    InsertInto(100,4, &mut actualDL, &mut refs);
    
    println!("Primero: {},  Ultimo: {}, Tamaño: {}",  refs.first,refs.last, refs.count);
    
    
    println!("val: {} indice: {} right: {} left: {}",actualDL[0].val, actualDL[0].idx,actualDL[0].point.right, actualDL[0].point.left);
    println!("val: {} indice: {} right: {} left: {}",actualDL[1].val, actualDL[1].idx,actualDL[1].point.right, actualDL[1].point.left);
    println!("val: {} indice: {} right: {} left: {}",actualDL[2].val, actualDL[2].idx,actualDL[2].point.right, actualDL[2].point.left);
    println!("val: {} indice: {} right: {} left: {}",actualDL[3].val, actualDL[3].idx,actualDL[3].point.right, actualDL[3].point.left);
    println!("val: {} indice: {} right: {} left: {}",actualDL[4].val, actualDL[4].idx,actualDL[4].point.right, actualDL[4].point.left);
    println!("val: {} indice: {} right: {} left: {}",actualDL[5].val, actualDL[5].idx,actualDL[5].point.right, actualDL[5].point.left);
    println!("val: {} indice: {} right: {} left: {}",actualDL[6].val, actualDL[6].idx,actualDL[6].point.right, actualDL[6].point.left);
    println!("val: {} indice: {} right: {} left: {}",actualDL[7].val, actualDL[7].idx,actualDL[7].point.right, actualDL[7].point.left);
    
    
    
    println!("");
    println!("Imprimir desde inicio");
    PrintListNormal(&mut actualDL, &mut refs);
    
    println!("");
    println!("Imprimir desde fin");
    PrintListBack(&mut actualDL, &mut refs);
    
    

}


/*
Primero: -1,  Ultimo: -1, Tamaño: 0
---Insertar al inicio---
---Insertar al final---
---Insertar al inicio---
---Insertar en posicion 2---
---Insertar al inicio---
---Insertar al final---
---Insertar al inicio---
---Insertar en posicion 4---
Primero: 6,  Ultimo: 5, Tamaño: 8
val: 133 indice: 0 right: 7 left: 2
val: 1 indice: 1 right: 3 left: 7
val: 3 indice: 2 right: 0 left: 4
val: 35 indice: 3 right: 5 left: 1
val: 66 indice: 4 right: 2 left: 6
val: 53 indice: 5 right: -1 left: 3
val: 78 indice: 6 right: 4 left: -1
val: 100 indice: 7 right: 1 left: 0

Imprimir desde inicio
Val|| de nodo: 78 
Val|| de nodo: 66 
Val|| de nodo: 3 
Val|| de nodo: 133 
Val|| de nodo: 100 
Val|| de nodo: 1 
Val|| de nodo: 35 
Val|| de nodo: 53 

Imprimir desde fin
Val|| de nodo: 53 
Val|| de nodo: 35 
Val|| de nodo: 1 
Val|| de nodo: 100 
Val|| de nodo: 133 
Val|| de nodo: 3 
Val|| de nodo: 66 
Val|| de nodo: 78 

*/