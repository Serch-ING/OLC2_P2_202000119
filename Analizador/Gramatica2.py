from AST.Expresion.Casteo.Casteo import Casteo

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
    r'[a-zA-Z_][a-zA-Z_0-9]*'
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
    print("Error lexico ", t.value[0])
    t.lexer.skip(1)



# Construyendo el analizador léxico
import ply.lex as lex

lexer = lex.lex()
precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
   # ('left', 'ABS', 'SQRT', 'TOSTRING', 'TOOWNED', 'CLONE','LEN'),
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



def p_instrucciones_lista(t):
    '''instrucciones    : instrucciones instruccion
                        | instruccion'''


def p_instruccion(t):
    '''instruccion  : funcion
                    | declaracion
                    | asignacion
                    | declaracion_arreglo
                    | star_struct'''

def p_lista_bloque(t):
    ''' lista_bloque : lista_bloque bloque
                    | bloque'''

def p_bloque(t):
    '''bloque : asignacion PYC
                | impresiones PYC
                | declaracion
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


def p_star_struct(t):
    ''' star_struct :  STRUCT ID LI list_struct_var LD'''

def p_list_declaracion_coma(t):
    '''list_struct_var  : list_struct_var COMA  struct_var
                        | struct_var  '''

def p_struct_var(t):
    '''struct_var : ID DP tipo_datos
                | ID DP expresiones   '''

def p_start_for(t):
    '''start_for : FOR ID IN opciones_for LI lista_bloque LD '''

def p_opciones_for(t):
    '''opciones_for :  expresiones
                    | expresiones PUNTO PUNTO expresiones'''

def p_asignacion_arreglo(t):
    ''' asignacion_arreglo : acceso_arreglo IGUAL expresiones PYC '''

def p_declaracion_arreglo(t):
    '''declaracion_arreglo : LET mutable ID validacion_dimension IGUAL expresiones PYC '''


def p_validacion_dimension(t):
    '''validacion_dimension : DP dimensiones_def'''


def p_dimensiones_def(t):
    '''dimensiones_def :  CI dimensiones_def PYC expresiones CD
                        | CI tipo_datos PYC expresiones CD '''


def p_acceso_arreglo(t):
    '''acceso_arreglo : ID dimensiones '''


def p_dimensiones(t):
    '''dimensiones : dimensiones dimension
                    | dimension'''


def p_dimension(t):
    '''dimension : CI expresiones CD  '''


def p_start_loop(t):
    '''start_loop : LOOP LI lista_bloque LD'''


def p_continue_ins(t):
    '''continue_ins : CONTINUE'''


def p_break_ins(t):
    '''break_ins : BREAK
                    | BREAK expresiones'''


def p_return_ins(t):
    '''return_ins : RETURN
                    | RETURN expresiones'''

def p_start_while(t):
    '''start_while : WHILE expresiones LI lista_bloque LD '''


def p_list_exp_ins(t):
    '''list_exp_ins : list_exp_ins bloque_exp
                | bloque_exp '''


def p_start_if(t):
    '''start_if : IF noseque_pasa LI list_exp_ins LD
                | IF noseque_pasa LI list_exp_ins LD ELSE LI list_exp_ins LD
                | IF noseque_pasa LI list_exp_ins LD lista_elif
                | IF noseque_pasa LI list_exp_ins LD lista_elif ELSE LI list_exp_ins LD '''



def p_noseque_pasa(t):
    ''' noseque_pasa : datos
                    | expresiones'''


def p_lista_if(t):
    ''' lista_elif : lista_elif else_if
                    | else_if'''



def p_else_if(t):
    ''' else_if : ELSE IF expresiones  LI list_exp_ins LD '''


def p_start_match(t):
    '''start_match : MATCH  datos LI matches LD '''



def p_matches(t):
    '''matches : matches bloque_match_val
                | bloque_match_val'''


def p_list_match(t):
    '''bloque_match_val :  varios_match IGUAL MAYOR simple_bloque_exp COMA
                    | varios_match IGUAL MAYOR LI list_exp_ins LD '''



def p_simple_bloque_exp(t):
    ''' simple_bloque_exp : bloque_match
                        | expresiones'''


def p_bloque_exp(t):
    ''' bloque_exp : bloque
                        | expresiones
                       '''
    t[0] = t[1]

def p_varios_match(t):
    '''varios_match : varios_match BARRA expresiones
                    | expresiones
                    | GBAJO'''


def p_llamada(t):
    '''llamada  : ID PI PD
                | ID PI lista_expres PD'''



def p_lista_expres(t):
    '''lista_expres : lista_expres COMA  expresiones
                    | expresiones '''


def p_funciones(t):
    '''funcion  : FUNCION MAIN PI PD LI lista_bloque LD
                |  FUNCION ID PI PD tipo_funcion LI lista_bloque LD
                |  FUNCION ID PI parametros PD tipo_funcion LI lista_bloque LD'''



def p_parametros(t):
    '''parametros : parametros COMA definiciones
                  | definiciones'''



def p_definiciones(t):
    """ definiciones : MUT ID tipado
                    | ID tipado
                    | ID  tipados_tipos  """


def p_tipados_tipos(t):
    '''tipados_tipos :  DP REFERENCE dimensiones_def
                    |  DP REFERENCE CI tipo_datos CD
                    | DP REFERENCE  tipado_vector'''


def p_referencias(t):
    '''referencias : REFER
                    | '''


def p_accceso(t):
    '''acceso   : PUBLICO
                |'''

def p_tipo_funcion(t):
    '''tipo_funcion : RESTA MAYOR tipo_datos
                    | RESTA MAYOR VECTOR MENOR tipo_datos MAYOR
                    | RESTA MAYOR ID
                    |'''

def p_declaracion(t):
    '''declaracion  : LET mutable ID tipado PYC
                        | LET mutable ID tipado IGUAL expresiones PYC
                        | LET mutable ID DP  tipado_vector IGUAL expresiones PYC'''


def p_tipado_vect(t):
    '''tipado_vector : VECTOR MENOR tipado_vector MAYOR
                    |  VECTOR MENOR tipo_datos MAYOR'''



def p_asignacio(t):
    '''asignacion      : ID IGUAL expresiones  '''



def p_mutable(t):
    '''mutable      : MUT
                        | '''


def p_tipado(t):
    '''tipado      : DP tipo_datos
                     |'''


def p_tipo_datos(t):
    '''tipo_datos     : TIPOINT
                      | TIPOFLOAT
                      | TIPOCHAR
                      | TIPOSTRING
                      | DIRSTRING
                      | TIPOBOOL
                      | TIPOUSIZE
                      '''




def p_instruccion_imprimir(t):
    '''impresiones     : PRINTLN PI CADENA PD
                       | PRINT PI CADENA PD
                       | PRINTLN PI CADENA COMA impresion_valores PD
                       | PRINT PI CADENA COMA  impresion_valores PD '''

def p_imprimir_lista_valores(t):
    '''impresion_valores     :  impresion_valores COMA expresiones
                         | expresiones '''


'''yyy'''
def p_expresiones(t):
    '''expresiones  : expre_valor
                    | funcion_nativa
                    | expre_logica
                    | expre_relacional
                    | expre_aritmetica
                    '''




def p_expre_valor(t):
    '''expre_valor : datos_cast
                    | start_match
                    | start_if
                    | start_loop
                    | llamada
                    | arreglo_init
                    | acceso_arreglo
                    | iniciando_vector
                    | iniciando_struct
                    '''


def p_iniciando_struct(t):
    '''iniciando_struct : ID  LI list_struct_var LD'''

def p_iniciando_vector(t):
    ''' iniciando_vector : VECTOR NEW
                        | VECTOR WCAPACITY PI expresiones PD
                        | VECT CI lista_Expresiones CD
                        | VECT CI expresiones PYC expresiones CD'''

def p_arreglo_init(t):
    '''arreglo_init : CI lista_Expresiones CD '''

def p_lista_expresiones(t):
    '''lista_Expresiones : lista_Expresiones COMA expresiones
                        | expresiones'''

def p_funcion_nativa(t):
    '''funcion_nativa : expresiones PUNTO nativas
                        | expresiones  PUNTO  list_acceso_struck IGUAL expresiones
                        | expresiones  PUNTO  list_acceso_struck '''

def p_nativas_vectores(t):
    '''nativas_vectores : PUSH PI expresiones PD
                        | REMOVE PI expresiones PD
                        | CONTAINS PI expresiones PD
                        | INSERT PI expresiones COMA expresiones PD
                        | CAPACITY '''

def p_nativas(t):
    '''nativas      : ABS
                    | SQRT
                    | TOSTRING
                    | TOOWNED
                    | CLONE
                    | LEN
                    | nativas_vectores
                   '''

def p_list_acceso_struck(t):
    '''list_acceso_struck : list_acceso_struck PUNTO  expresiones
                        | expresiones '''

def p_expre_logica(t):
    ''' expre_logica : expresiones OR expresiones
                    | expresiones AND expresiones
                    | NOT  expresiones'''

def p_expre_relacional(t):
    '''expre_relacional : expresiones MAYORIGUAL expresiones
                    | expresiones MAYOR expresiones
                    | expresiones MENORIGUAL expresiones
                    | expresiones MENOR expresiones
                    | expresiones IGUALDAD expresiones
                    | expresiones DESIGUALDAD expresiones'''

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

def p_datos_cast(t):
    ''' datos_cast : datos
                   | expresiones AS tipo_datos'''

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

def p_error(t):
    try:
        print("\n========================= Error sintáctico en '%s'" % t.value, " =========================")
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
