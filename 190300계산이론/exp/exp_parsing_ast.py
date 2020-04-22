# -----------------------------------------------------------------------------
# Interpreter for expressions through AST
#  1. Lexing with regular expression
#  2. Parsing with context-free grammar
#  3. Generating an AST (Abstact Syntax Tree) with tuples
#  4. Evaluating an AST
# -----------------------------------------------------------------------------

########### Lexing ##################################
tokens = ('NAME','NUMBER')
literals = ['=', '+', '-', '*', '/', '(', ')']

t_NAME   = r'[a-zA-Z_][a-zA-Z0-9_]*'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Ignored characters
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
    
# Build the lexer
import ply.lex as lex
lexer = lex.lex()

######## Parsing and Interpreting ######@###########

precedence = (
    ('left', '+', '-'),
    ('left', '*', '/'),
    ('right', 'UMINUS'),
)

# CFG Definition

def p_statement_assign(p):
    'statement : NAME "=" expr'
    p[0] = ('=', p[1], p[3])
    
def p_statement_expr(p):
    'statement : expr'
    p[0] = p[1]

def p_expr_N(p):
    "expr : NUMBER"
    p[0] = ('V', p[1])

def p_expr_name(p):
    "expr : NAME"
    p[0] = ('NAME', p[1])

def p_expr_uminus(p):
    "expr : '-' expr %prec UMINUS"
    p[0] = ('UMINUS', p[2])
    
def p_expr_binop(p):
    '''expr : expr '+' expr
            | expr '-' expr
            | expr '*' expr
            | expr '/' expr '''
    if p[2] == '+':
        p[0] = ('+', p[1], p[3])
    elif p[2] == '-':
        p[0] = ('-', p[1], p[3])
    elif p[2] == '*':
        p[0] = ('*', p[1], p[3])
    elif p[2] == '/':
        p[0] = ('/', p[1], p[3])
 
def p_expr_group(p):
    "expr : '(' expr ')'"
    p[0] = p[2]

def p_error(p):
    if p:
        print("Syntax error at '%s'" % p.value)
    else:
        print("Syntax error at EOF")

import ply.yacc as yacc
yacc.yacc()

###############  Test Code  ##################
prog_exp1 = ''' 10 + 20 * 3 '''              # 70
prog_exp2 = ''' 10 - (2 + 3) * 3 + 10'''     # 5
prog_exp3 = ''' 2 * -(1 + 2) + 2'''          # -4           
prog_assign1 = ''' x = 10 '''                # x = 10
prog_assign2 = '''x = (1+2) * 3 '''          # print(names) = {'x' : 9}
prog_exp4 = '''x = x + 10 '''                # x = x + 10
# The Lvalue is different from the Rvalue    #
#############################################

# lexer.input(data)

ast = yacc.parse(prog_exp1)
print(ast)

# dictionary of names
names = {}

def eval(tree):
    if not tree:          return 0      # tree == None
    opr = tree[0]
    if opr == '+':        return eval(tree[1]) +  eval(tree[2])
    elif opr == '-':      return eval(tree[1]) - eval(tree[2])
    elif opr == '*':      return eval(tree[1]) *  eval(tree[2])
    elif opr == '/':      return eval(tree[1]) /  eval(tree[2])
    elif opr == 'UMINUS': return - eval(tree[1])
    elif opr == 'V':      return tree[1]
    elif opr == 'NAME':   return names[tree[1]]
    elif opr == '=':      names[tree[1]] = eval(tree[2])
    else:                 print("unexpeced case : ", tree)

print(eval(ast))


















        

    
