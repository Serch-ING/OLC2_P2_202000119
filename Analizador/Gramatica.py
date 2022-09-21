from AST.Expresion.Casteo.Casteo import Casteo
from AST.TablaErrores import TablaErrores
E_list = TablaErrores()

reservadas = {
    # ACCESO
    'pub': 'PUBLICO',
    # TIPOS
    'i64': 'TIPOINT',
    'f64': 'TIPOFLOAT',
    'bool': 'TIPOBOOL',
    'char': 'TIPOCHAR',
    'String': 'TIPOSTRING',
    '&str': 'DIRSTRING',
    'usize': 'TIPOUSIZE',
    # CASTEO
    'as': 'AS',
    # IMPRIMIR
    'println!': 'PRINTLN',
    'print!': 'PRINT',
    # DECLARAR
    'let': 'LET',
    'mut': 'MUT',
    # FUNCIONES
    'fn': 'FUNCION',
    'main': 'MAIN',
    # FUNCIONES NATIVAS
    'abs()': 'ABS',
    'sqrt()': 'SQRT',
    'to_string()': 'TOSTRING',
    'to_owned()': 'TOOWNED',
    'clone()': 'CLONE',
    # VECTORES
    'Vec': 'VECTOR',
    'vec!': 'VECT',
    # FUNCIONES NATIVAS VECTORES
    '::new()': 'NEW',
    'len()': 'LEN',
    'push': 'PUSH',
    'remove': 'REMOVE',
    'contains': 'CONTAINS',
    'insert': 'INSERT',
    'capacity()': 'CAPACITY',
    '::with_capacity': 'WCAPACITY',
    # SENTENCIAS
    'if': 'IF',
    'else': 'ELSE',
    'match': 'MATCH',
    # CICLOS
    'loop': 'LOOP',
    'while': 'WHILE',
    'for': 'FOR',
    'in': 'IN',
    # SENTENCIAS DE RETORNO
    'break': 'BREAK',
    'continue': 'CONTINUE',
    'return': 'RETURN',
    # STRUCT
    'struct': 'STRUCT',
    # MODULO
    'mod': 'MOD',
    # POTENCIAS
    '::pow': 'POW',
    '::powf': 'POWF',
    # BOOLS
    'true': 'TRUE',
    'false': 'FALSE',
    #
    '&mut': 'REFERENCE'
}

tokens = [
             # ** ** ** ** ** OPERACION MATEMATICA ** ** ** ** **
             'SUMA',
             'RESTA',
             'MULTI',
             'DIVI',
             'MODULO',
             # ** ** ** ** ** OPERACION RELACIONAL ** ** ** ** **
             'MENORIGUAL',
             'MAYORIGUAL',
             'IGUALDAD',
             'DESIGUALDAD',
             'MENOR',
             'MAYOR',
             # ** ** ** ** ** OPERACION LOGICA ** ** ** ** **
             'OR',
             'AND',
             'NOT',
             # ** ** ** ** ** SIMBOLOS LENGUAJE ** ** ** ** **
             'LI',
             'LD',
             'CI',
             'CD',
             'PI',
             'PD',
             'PYC',
             'DP',
             'COMA',
             'PUNTO',
             'IGUAL',
             'BARRA',
             'GBAJO',
             'REFER',
             # ********** EXPRESIONES REGUALES **********
             'FLOAT',
             'ENTERO',
             'CADENA',
             'CARACTER',
             'ID',
             'ERR'
         ] + list(reservadas.values())

# Tokens
# ********** OPERACION MATEMATICA **********
t_SUMA = r'\+'
t_RESTA = r'-'
t_MULTI = r'\*'
t_DIVI = r'/'
t_MODULO = r'%'
# ********** OPERACION RELACIONAL **********
t_MENORIGUAL = r'<='
t_MAYORIGUAL = r'>='
t_IGUALDAD = r'=='
t_DESIGUALDAD = r'!='
t_MENOR = r'<'
t_MAYOR = r'>'
# ********** OPERACION LOGICA **********
t_OR = r'\|\|'
t_AND = r'&&'
t_NOT = r'!'
# ********** SIMBOLOS LENGUAJE **********
t_LI = r'\{'
t_LD = r'\}'
t_CI = r'\['
t_CD = r'\]'
t_PI = r'\('
t_PD = r'\)'
t_PYC = r';'
t_DP = r':'
t_COMA = r','
t_PUNTO = r'\.'
t_IGUAL = r'='
t_BARRA = r'\|'
t_GBAJO = r'_'
t_REFER = r'&'



def t_FLOAT(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
        print("Se reconcio FLOAT ", t.value)
    except ValueError:
        print("Float value too large %d", t.value)
        t.value = 0
    return t


def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
        print("Se reconcio ENTERO ", t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t


def t_Especiales_0(t):
    r'::[a-zA-Z_][a-zA-Z_0-9]*\(\)'
    return revicion_reservadas(t)


def t_Especiales_1(t):
    r'[a-zA-Z][a-zA-Z_0-9]*\(\)'
    return revicion_reservadas(t)


def t_Especiales_2(t):
    r'::[a-zA-Z][a-zA-Z_0-9]*'
    return revicion_reservadas(t)


def t_Especiales_3(t):
    r'[a-zA-Z][a-zA-Z_0-9]*!'
    return revicion_reservadas(t)


def t_Especiales_4(t):
    r'&[a-zA-Z][a-zA-Z_0-9]*'
    return revicion_reservadas(t)


# [a-zA-Z_][a-zA-Z_0-9]*
def t_ID(t):
    r'[a-zA-Z][a-zA-Z_0-9]*'
    t.type = reservadas.get(t.value, 'ID')
    print("Se reconcio: ", t.type, ": ", t.value)
    return t


def revicion_reservadas(t):
    t.type = reservadas.get(t.value, 'ERR')
    print("Se reconcio: ", t.type, ": ", t.value)
    return t


def t_CADENA(t):
    r'\".*?\"'
    t.value = t.value[1:-1]  # remuevo las comillas
    print("Se reconcio cadena: ", t.value)
    return t


def t_CARACTER(t):
    r'\'.?\''
    t.value = t.value[1:-1]  # remuevo las comillas
    print("Se reconcio caracter: ", t.value)
    return t


# Comentario simple // ...
def t_COMENTARIO(t):
    r'//.*\n'
    print("Se reconcio comentario: ", t.value.replace('\n', ''))
    t.lexer.lineno += 1


# Caracteres ignorados
t_ignore = " \t\r"


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


def t_error(t):
    E_list.agregar_error("El caracter" + str(t.value[0]) +" no es aceptado por analizador", 0, " Lectura de entrada ", t.lexer.lineno,find_column(t.value, t))
    E_list.print_errores()
    print("Error lexico ", t.value[0])
    t.lexer.skip(1)

def find_column(input, token):
    line_start = input.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1

# Construyendo el analizador léxico
import ply.lex as lex

lexer = lex.lex()
precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('left', 'ABS', 'SQRT', 'TOSTRING', 'TOOWNED', 'CLONE','LEN'),
    ('left', 'MAYORIGUAL', 'MAYOR', 'MENORIGUAL', 'MENOR', 'IGUALDAD', 'DESIGUALDAD'),
    ('left', 'SUMA', 'RESTA'),
    ('left', 'MULTI', 'DIVI'),
    ('left', 'MODULO'),
    ('right', 'POWF', 'POW'),
    ('right', 'NOT', 'UMENOS')
)



# Definición de la gramática
def p_init(t):
    'init            : instrucciones'
    t[0] = t[1]


def p_instrucciones_lista(t):
    '''instrucciones    : instrucciones instruccion
                        | instruccion'''

    if len(t) > 2:
        t[1].append(t[2])
        t[0] = t[1]

    else:
        t[0] = [t[1]]


def p_instruccion(t):
    '''instruccion  : funcion
                    | declaracion
                    | asignacion
                    | declaracion_arreglo
                    | star_struct
                    '''

    t[0] = t[1]


def p_lista_bloque(t):
    ''' lista_bloque : lista_bloque bloque
                    | bloque'''
    if len(t) > 2:
        t[1].append(t[2])
        t[0] = t[1]

    else:
        t[0] = [t[1]]

def p_bloque(t):
    '''bloque : impresiones PYC
                | declaracion
                | asignacion PYC
                | llamada PYC
                | start_match
                | start_if
                | start_while
                | return_ins PYC
                | break_ins PYC
                | continue_ins PYC
                | start_loop
                | declaracion_arreglo
                | asignacion_arreglo
                | start_for
                | funcion_nativa PYC
                | '''

    if len(t) > 1:
        t[0] = t[1]
    else:
        t[0] = None

def p_bloque_match(t):
    '''bloque_match : impresiones
                    | asignacion
                    | llamada
                    | start_match
                    | start_if
                    | start_while
                    | return_ins
                    | start_loop
                    | declaracion_arreglo
                    | start_for
                    |
                    '''
    if len(t) >1 :
        t[0]=t[1]
    else:
        t[0]= None

'''xxx'''
from AST.Expresion import Identificador
from AST.Instruccion import Declaracion, Asignacion, Funcion, Llamada, DeclaracionArreglo,DeclaracionVector
from AST.TablaSimbolos.Tipos import tipo
from AST.Expresion.Nativas import Nativas, NativasVectores
from AST.Expresion.Operaciones import Logica
from AST.Instruccion.Match import Match, BloqueMatch
from AST.Expresion import Primitivo
from AST.Instruccion import Imprimir
from AST.Expresion.Operaciones import Aritmetica, Relacional
from AST.Instruccion.SentenciasControl import Ifs
from AST.Instruccion.SentenciasCiclicas import While,Loop,For
from AST.Instruccion.SentenciasTranferencia import Return,Break,Continue
from AST.Expresion.Arreglo import ArregloData, AccesoArreglo
from AST.Expresion.Casteo import  Casteo
from AST.Expresion.Vector import VectorData
from AST.TablaSimbolos import InstanciaStruct
from AST.Expresion.Struct import AccesoStruct
from AST.Expresion import DeclararStruct, Repeticiones
'''zzz'''
def p_star_struct(t):
    ''' star_struct :  STRUCT definition_strct'''
    t[0]= t[2]

def p_definition_strct(t):
    ''' definition_strct :  ID LI list_struct_var LD'''
    t[0] = DeclararStruct.DeclararStruct(t[1], t[3])

def p_definition_strct_v2(t):
    ''' definition_strct_v2 :  ID LI list_struct_var LD'''
    t[0] = InstanciaStruct.InstanciaStruct(t[1], t[3])

def p_list_declaracion_coma(t):
    '''list_struct_var  : list_struct_var COMA  struct_var
                        | struct_var  '''
    if len(t) > 2:
        t[1].append(t[3])
        t[0] = t[1]

    else:
        t[0] = [t[1]]

def p_struct_var(t):
    '''struct_var : ID DP tipo_datos
                |  ID DP definition_strct_v2
                | ID DP expresiones
                '''
    t[0] = Declaracion.Declaracion(t[1], t[3], None, None)

def p_start_for(t):
    '''start_for : FOR ID IN opciones_for LI lista_bloque LD '''
    t[0]= For.For(t[2],t[4],t[6])

def p_opciones_for(t):
    '''opciones_for :  expresiones
                    | expresiones PUNTO PUNTO expresiones'''

    if len(t) == 2:
        t[0]= [1,t[1]]
    else:
        t[0]= [2,t[1],t[4]]

def p_asignacion_arreglo(t):
    ''' asignacion_arreglo : acceso_arreglo IGUAL expresiones PYC '''
    t[1].valor = t[3]
    t[0] = t[1]

def p_declaracion_arreglo(t):
    '''declaracion_arreglo : LET mutable ID validacion_dimension IGUAL expresiones PYC '''
    t[0]= DeclaracionArreglo.DeclaracionArreglo(t[2],t[3],t[4],t[6])

def p_validacion_dimension(t):
    '''validacion_dimension : DP dimensiones_def'''

    if len(t) > 1:
        t[0] = t[2]
    else:
        t[0] = None

def p_dimensiones_def(t):
    '''dimensiones_def :  CI dimensiones_def PYC expresiones CD
                        | CI tipo_datos PYC expresiones CD '''


    if t.slice[2].type == 'dimensiones_def':
        print("Dimension: Se detcto expresion: ", t[2], " dimensiones: ", t[4])
        t[2].append(t[4])
        t[0] = t[2]

    elif t.slice[2].type == 'tipo_datos':
        print("Definicion: Se detcto tipo: ", t[2], " dimensiones: ",t[4])
        if  t[0] is None:
            t[0] = [t[2],t[4]]
        else:
            t[0].append(t[2])
            t[0].append(t[4])

def p_acceso_arreglo(t):
    '''acceso_arreglo : ID dimensiones '''
    print("Deberia ser id: ", t[1], " dimensiones: ",t[2])
    t[0] = AccesoArreglo.AccesoArreglo(t[1], t[2])

def p_dimensiones(t):
    '''dimensiones : dimensiones dimension
                    | dimension'''
    if len(t) > 2:
        t[1].append(t[2])
        t[0] = t[1]

    else:
        t[0] = [t[1]]

def p_dimension(t):
    '''dimension : CI expresiones CD  '''
    t[0] = t[2]

def p_start_loop(t):
    '''start_loop : LOOP LI lista_bloque LD'''
    t[0] = Loop.Loop(t[3])

def p_continue_ins(t):
    '''continue_ins : CONTINUE'''
    t[0] = Continue.Continue()

def p_break_ins(t):
    '''break_ins : BREAK
                    | BREAK expresiones'''
    if len(t) == 2:
        t[0] = Break.Break(None)
    else:
        t[0] = Break.Break(t[2])

def p_return_ins(t):
    '''return_ins : RETURN
                    | RETURN definition_strct_v2
                    | RETURN expresiones'''
    if len(t) == 2:
        t[0] = Return.Return(None)
    else:
        t[0] = Return.Return(t[2])

def p_start_while(t):
    '''start_while : WHILE expresiones LI lista_bloque LD '''
    t[0] = While.While(t[2],t[4])

def p_list_exp_ins(t):
    '''list_exp_ins : list_exp_ins bloque_exp
                | bloque_exp '''
    if len(t) > 2:
        t[1].append(t[2])
        t[0] = t[1]

    else:
        t[0] = [t[1]]

def p_start_if(t):
    '''start_if : IF expresiones LI list_exp_ins LD
                | IF expresiones LI list_exp_ins LD ELSE LI list_exp_ins LD
                | IF expresiones LI list_exp_ins LD lista_elif
                | IF expresiones LI list_exp_ins LD lista_elif ELSE LI list_exp_ins LD '''

    print('Llego if gramatica ', len(t))
    if len(t) == 6:
        t[0]= Ifs.Ifs(t[2],t[4],None,None)
    elif len(t)==10:
        t[0] = Ifs.Ifs(t[2], t[4], t[8],None)
    if len(t) == 7:
        t[0]= Ifs.Ifs(t[2],t[4],None,t[6])
    if len(t) == 11:
        t[0]= Ifs.Ifs(t[2],t[4],t[9],t[6])

def p_lista_if(t):
    ''' lista_elif : lista_elif else_if
                    | else_if'''
    if len(t) > 2:
        t[1].append(t[2])
        t[0] = t[1]

    else:
        t[0] = [t[1]]

def p_else_if(t):
    ''' else_if : ELSE IF expresiones  LI list_exp_ins LD '''
    t[0] = Ifs.Ifs(t[3], t[5], None,None)

def p_start_match(t):
    '''start_match : MATCH expresiones LI matches LD '''
    print("Llego a match")
    t[0] = Match.Match(t[2], t[4])

def p_matches(t):
    '''matches : matches bloque_match
                | bloque_match'''
    if len(t) > 2:
        t[1].append(t[2])
        t[0] = t[1]

    else:
        t[0] = [t[1]]

def p_list_match(t):
    '''bloque_match :  varios_match IGUAL MAYOR simple_bloque_exp COMA
                    | varios_match IGUAL MAYOR LI list_exp_ins LD '''

    if len(t) == 6:
        print("Llego con coma =")
        print(t[4])
        t[0] = BloqueMatch.BloqueMatch(t[1], [t[4]],False)
    elif len(t) == 7:
        t[0] = BloqueMatch.BloqueMatch(t[1], t[5],True
                                       )

def p_simple_bloque_exp(t):
    ''' simple_bloque_exp : expresiones
                        | bloque_match'''
    t[0] = t[1]
    print("Llego con coma = a un simeple ")
    print(t[1])

def p_bloque_exp(t):
    ''' bloque_exp : bloque
                        | expresiones  '''
    t[0] = t[1]

def p_varios_match(t):
    '''varios_match : varios_match BARRA expresiones
                    | expresiones
                    | GBAJO '''

    if len(t) > 2:
        t[1].append(t[3])
        t[0] = t[1]

    else:
        t[0] = [t[1]]

def p_llamada(t):
    '''llamada  : ID PI PD
                | ID PI lista_expres PD'''

    if len(t) == 4:
        print("=== llamda tipo 1")
        t[0] = Llamada.Llamada(t[1], [])
    else:
        print("=== llamda tipo 2")
        t[0] = Llamada.Llamada(t[1], t[3])

def p_lista_expres(t):
    '''lista_expres : lista_expres COMA  expresiones
                    | expresiones '''

    if len(t) > 2:
        t[1].append(t[3])
        t[0] = t[1]

    else:
        t[0] = [t[1]]

def p_funciones(t):
    '''funcion  : FUNCION MAIN PI PD LI lista_bloque LD
                |  FUNCION ID PI PD tipo_funcion LI lista_bloque LD
                |  FUNCION ID PI parametros PD tipo_funcion LI lista_bloque LD'''

    if len(t) == 8:
        t[0] = Funcion.Funcion(t[2], None, [], t[6])
    elif len(t) == 9:
        t[0] = Funcion.Funcion(t[2], t[5], [], t[7])
    elif len(t) == 10:
        t[0] = Funcion.Funcion(t[2], t[6], t[4], t[8])

def p_parametros(t):
    '''parametros : parametros COMA definiciones
                  | definiciones'''

    if len(t) > 2:
        t[1].append(t[3])
        t[0] = t[1]

    else:
        t[0] = [t[1]]

def p_definiciones(t):
    """ definiciones : MUT ID tipado
                    | ID tipado
                    | ID  tipados_tipos  """


    print("Llego a definiciones, ",len(t))

    if len(t) == 4 :
        t[0] = Declaracion.Declaracion(Identificador.Identificador(t[2]), None, t[3],True)

    elif len(t) == 3:
        if t.slice[2].type == 'tipado':
            t[0] = Declaracion.Declaracion(Identificador.Identificador(t[1]), None, t[2], False)
        else:
            t[0] = Declaracion.Declaracion(Identificador.Identificador(t[1]), None, t[2], True,True)

def p_tipados_tipos(t):
    '''tipados_tipos :  DP REFERENCE dimensiones_def
                    |  DP REFERENCE CI tipo_datos CD
                    | DP REFERENCE  tipado_vector
                    | DP REFERENCE ID'''

    if len(t)==4:
        if t.slice[3].type == 'dimensiones_def':
            t[0] = t[3]
        else:
            t[0] = [t[3]]
    else:

        t[0]= [t[4]]

def p_referencias(t):
    '''referencias : REFER
                    | '''

    if len(t) > 1:
        t[0] = True

    else:
        t[0] = False

def p_accceso(t):
    '''acceso   : PUBLICO
                |'''
    if len(t) > 1:
        t[0] = True

    else:
        t[0] = False

def p_tipo_funcion(t):
    '''tipo_funcion : RESTA MAYOR tipo_datos
                    | RESTA MAYOR VECTOR MENOR tipo_datos MAYOR
                    |'''

    if len(t) == 4:
        t[0] = t[3]
    elif len(t) == 1:
        t[0] = None

def p_declaracion(t):
    '''declaracion  : LET mutable ID tipado PYC
                        | LET mutable ID tipado IGUAL expresiones PYC
                        | LET mutable ID DP  tipado_vector IGUAL expresiones PYC
                        | LET mutable ID tipado IGUAL definition_strct_v2 PYC'''

    if len(t) == 6:
        t[0] = Declaracion.Declaracion(Identificador.Identificador(t[3]), None, t[4], t[2])

    elif len(t) == 8:

        t[0] = Declaracion.Declaracion(Identificador.Identificador(t[3]), t[6], t[4], t[2])
    else:
        if  t.slice[6].type == 'definition_strct_v2':
            t[0] = Declaracion.Declaracion(Identificador.Identificador(t[3]), t[6], tipo.STRUCT, t[2])
        else:
            t[0] = DeclaracionVector.DeclaracionVector(t[3],t[7],t[5],t[2])

def p_tipado_vect(t):
    '''tipado_vector : VECTOR MENOR tipado_vector MAYOR
                    |  VECTOR MENOR tipo_datos MAYOR'''

    if len(t) == 1:
        t[0]= t[3]
    else:
        t[0]=t[3]

def p_asignacio(t):
    '''asignacion      : ID IGUAL expresiones
                        '''
    t[0] = Asignacion.Asignacion(t[1], t[3])

def p_mutable(t):
    '''mutable      : MUT
                        | '''
    if len(t) > 1:
        t[0] = True

    else:
        t[0] = False

def p_tipado(t):
    '''tipado      : DP tipo_datos
                     |'''
    if len(t) > 1:

        t[0] = t[2]
    else:
        t[0] = None

def p_tipo_datos(t):
    '''tipo_datos     : TIPOINT
                      | TIPOFLOAT
                      | TIPOCHAR
                      | TIPOSTRING
                      | DIRSTRING
                      | TIPOBOOL
                      | TIPOUSIZE
                      | ID'''

    if t[1] == "i64":
        t[0] = tipo.ENTERO
    elif t[1] == "f64":
        t[0] = tipo.DECIMAL
    elif t[1] == "char":
        t[0] = tipo.CARACTER
    elif t[1] == "String":
        t[0] = tipo.STRING
    elif t[1] == "&str":
        t[0] = tipo.DIRSTRING
    elif t[1] == "bool":
        t[0] = tipo.BOOLEANO
    elif t[1] == "usize":
        t[0] = tipo.USIZE
    else:
        t[0] = Identificador.Identificador(t[1])

def p_instruccion_imprimir(t):
    '''impresiones     : PRINTLN PI CADENA PD
                       | PRINT PI CADENA PD
                       | PRINTLN PI CADENA COMA impresion_valores PD
                       | PRINT PI CADENA COMA  impresion_valores PD '''

    if len(t) == 5:

        if t[1] == 'println!':
            t[0] = Imprimir.Imprimir(Primitivo.Primitivo(t[3], 'STRING'), True, [])
            # print("\nRe reocnocio: println! con el token: ", t[3], "\n")
        elif t[1] == 'print!':
            t[0] = Imprimir.Imprimir(Primitivo.Primitivo(t[3], 'STRING'), False, [])
            # print("\nRe reocnocio: print! con el token: ", t[3], "\n")

    else:

        if t[1] == 'println!':
            t[0] = Imprimir.Imprimir(t[3], True, t[5])
            # print("\nRe reocnocio: println! con el token: ", t[5], "\n")

        elif t[1] == 'print!':
            t[0] = Imprimir.Imprimir(t[3], False, t[5])
            # print("\nRe reocnocio: print! con el token: ", t[5], "\n")

def p_imprimir_lista_valores(t):
    '''impresion_valores     :  impresion_valores COMA expresiones
                         | expresiones '''

    if len(t) > 2:
        t[1].append(t[3])
        t[0] = t[1]

    else:
        t[0] = [t[1]]

'''yyy'''
def p_expresiones(t):
    '''expresiones  : funcion_nativa
                    | expre_logica
                    | expre_relacional
                    | expre_aritmetica
                    | expre_valor
                    '''

    t[0] = t[1]

def p_expre_valor(t):
    '''expre_valor : datos_cast
                    | start_match
                    | start_if
                    | start_loop
                    | llamada
                    | arreglo_init
                    | acceso_arreglo
                    | iniciando_vector
                    | repeticiones
                    '''
    t[0] = t[1]

def p_repeticiones(t):
    '''repeticiones : CI expresiones PYC expresiones CD
                    | CI tipo_datos PYC expresiones CD '''
    if  t.slice[2].type == 'expresiones':
        t[0] = Repeticiones.Repeticiones(t[2],t[4])
    else:
        t[0] = Repeticiones.Repeticiones(t[2], t[4],True)

def p_iniciando_vector(t):
    ''' iniciando_vector : VECTOR NEW
                        | VECTOR WCAPACITY PI expresiones PD
                        | VECT CI lista_Expresiones CD
                        | VECT CI expresiones PYC expresiones CD'''
    if t.slice[2].type == 'NEW':
        t[0]= []
    elif t.slice[2].type == 'WCAPACITY':
        t[0]= [t[4]]
    elif t.slice[2].type == 'CI':
        if t.slice[3].type == 'lista_Expresiones':
            t[0] = VectorData.VectorData(t[3])
        else:
            t[0] = VectorData.VectorData(t[3],t[5])

def p_arreglo_init(t):
    '''arreglo_init : CI lista_Expresiones CD '''
    t[0] = ArregloData.ArregloData(t[2])

def p_lista_expresiones(t):
    '''lista_Expresiones : lista_Expresiones COMA expresiones
                        | expresiones'''

    if len(t) > 2:
        t[1].append(t[3])
        t[0] = t[1]

    else:
        t[0] = [t[1]]

def p_funcion_nativa(t):
    '''funcion_nativa : expresiones PUNTO nativas'''
#
    print("Llego a nativas")

    if isinstance(t[3],NativasVectores.NativasVectores):
        nativa = t[3]
        nativa.expresion = t[1]
        print("Llego a nativa vectores", nativa)
        t[0] = nativa

    elif  isinstance(t[3],AccesoStruct.AccesoStruct):
        print(t[3])
        print(t[1])
        t[3].identificador = t[1]
        t[0]= t[3]
    else:

        t[0] = Nativas.Nativas(t[1], t[3])

def p_nativas_vectores(t):
    '''nativas_vectores : PUSH PI expresiones PD
                        | PUSH PI definition_strct_v2 PD
                        | REMOVE PI expresiones PD
                        | CONTAINS PI expresiones PD
                        | INSERT PI expresiones COMA expresiones PD
                        | CAPACITY '''

    if len(t)==5:
        t [0] = NativasVectores.NativasVectores(t[3],t[1].lower())
    elif len(t) == 7:
        t[0] = NativasVectores.NativasVectores(t[3], t[1].lower(),t[5])
    else:
        t[0] = NativasVectores.NativasVectores(None, t[1].lower())

def p_nativas(t):
    '''nativas      : ABS
                    | SQRT
                    | TOSTRING
                    | TOOWNED
                    | CLONE
                    | LEN
                    | nativas_vectores
                    | acceso_struct '''

    t[0] = t[1]

def p_acceso_struct(t):
    '''acceso_struct : ID list_acceso_struck
                        | ID list_acceso_struck IGUAL expresiones '''

    aux= [Identificador.Identificador(t[1])]
    for x in t[2]:
        aux.append(x)

    if len(t) == 3:
        t[0] = AccesoStruct.AccesoStruct(None, aux, None)
    else:
        t[0] = AccesoStruct.AccesoStruct(None, aux, t[4])


def p_list_acceso_struck(t):
    '''list_acceso_struck : list_acceso_struck PUNTO  ID
                        | PUNTO ID
                        | '''
    if len(t) > 3:
        t[1].append(Identificador.Identificador(t[3]))
        t[0] = t[1]

    elif len(t)>1:
        t[0] = [Identificador.Identificador(t[2])]
    else:
        t[0] = []

def p_expre_logica(t):
    ''' expre_logica : expresiones OR expresiones
                    | expresiones AND expresiones
                    | NOT  expresiones'''
    if len(t) == 3:
        if t.slice[1].type == 'NOT':
            t[0] = Logica.Logica(t[2], "!", None, True)
    elif len(t) == 4:
        if t.slice[2].type == 'OR':
            t[0] = Logica.Logica(t[1], "||", t[3], False)
        elif t.slice[2].type == 'AND':
            t[0] = Logica.Logica(t[1], "&&", t[3], False)

def p_expre_relacional(t):
    '''expre_relacional : expresiones MAYORIGUAL expresiones
                    | expresiones MAYOR expresiones
                    | expresiones MENORIGUAL expresiones
                    | expresiones MENOR expresiones
                    | expresiones IGUALDAD expresiones
                    | expresiones DESIGUALDAD expresiones'''

    if len(t) == 4:
        if t[2] == ">=":
            t[0] = Relacional.Relacional(t[1], ">=", t[3], False)
        elif t[2] == ">":
            t[0] = Relacional.Relacional(t[1], ">", t[3], False)
        elif t[2] == "<=":
            t[0] = Relacional.Relacional(t[1], "<=", t[3], False)
        elif t[2] == "<":
            t[0] = Relacional.Relacional(t[1], "<", t[3], False)
        elif t[2] == "==":
            t[0] = Relacional.Relacional(t[1], "==", t[3], False)
        elif t[2] == "!=":
            t[0] = Relacional.Relacional(t[1], "!=", t[3], False)

def p_expre_aritmetica(t):
    '''expre_aritmetica : RESTA expresiones %prec UMENOS
                    | PI expresiones PD
                    | expresiones RESTA expresiones
                    | expresiones SUMA expresiones
                    | expresiones MULTI expresiones
                    | expresiones DIVI expresiones
                    | expresiones MODULO expresiones
                    | TIPOFLOAT POWF PI expresiones COMA expresiones PD
                    | TIPOINT POW PI expresiones COMA expresiones PD '''

    if len(t) == 3:
        if t[1] == "-":
            t[0] = Aritmetica.Aritmetica(t[2], "-", 0, True)
    elif len(t) == 4:
        if t[2] == "+":
            t[0] = Aritmetica.Aritmetica(t[1], "+", t[3], False)
        elif t[2] == "-":
            t[0] = Aritmetica.Aritmetica(t[1], "-", t[3], False)
        elif t[2] == "*":
            t[0] = Aritmetica.Aritmetica(t[1], "*", t[3], False)
        elif t[2] == "/":
            t[0] = Aritmetica.Aritmetica(t[1], "/", t[3], False)
        elif t[2] == "%":
            t[0] = Aritmetica.Aritmetica(t[1], "%", t[3], False)
        elif t[1] == "(" and t[3] == ")":
            t[0] = t[2]
    elif len(t) == 8:

        if t[2] == "::pow":
            t[0] = Aritmetica.Aritmetica(t[4], "^", t[6], False)
        elif t[2] == "::powf":
            t[0] = Aritmetica.Aritmetica(t[4], "^f", t[6], False)


def p_datos_cast(t):
    ''' datos_cast : datos
                   | expresiones AS tipo_datos'''

    if len(t) == 2:
        t[0] = t[1]
    else:
        t[0]= Casteo.Casteo(t[1],t[3])



def p_datos(t):
    '''datos : ENTERO
            | FLOAT
            | CADENA
            | CARACTER
            | ID
            | TRUE
            | FALSE
            | REFERENCE ID
            | REFER CADENA'''

    if t.slice[1].type == 'ENTERO':
        t[0] = Primitivo.Primitivo(t[1], 'ENTERO')
    elif t.slice[1].type == 'FLOAT':
        t[0] = Primitivo.Primitivo(t[1], 'DECIMAL')
    elif t.slice[1].type == 'CADENA':
        t[0] = Primitivo.Primitivo(t[1], 'DIRSTRING')
    elif t.slice[1].type == 'TRUE':
        t[0] = Primitivo.Primitivo(True, 'BOOLEANO')
    elif t.slice[1].type == 'FALSE':
        t[0] = Primitivo.Primitivo(False, 'BOOLEANO')
    elif t.slice[1].type == 'CARACTER':
        t[0] = Primitivo.Primitivo(t[1], 'CARACTER')
    elif t.slice[1].type == 'ID':
        t[0] = Identificador.Identificador(t[1])
    elif t.slice[1].type == 'REFERENCE':
        t[0] = Identificador.Identificador(t[2], True)
    else:
        t[0] = Primitivo.Primitivo(t[2], 'DIRSTRING')

def p_error(t):
    try:
        print("\n========================= Error sintáctico en '%s'" % t.value, " =========================")
        E_list.agregar_error("No se esperaba el caracter: " + str(t.value) + ", se ignoro", 1, " Lectura de entrada ",
                             t.lexer.lineno, t.lexer.lexpos)
        E_list.print_errores()
    except:
        print("")

    if t:
        print("Token: ", t, "\n")
        parser.errok()
    else:
        print("Syntax error at EOF")


import ply.yacc as yacc

parser = yacc.yacc()


def parse(input):
    return parser.parse(input)
