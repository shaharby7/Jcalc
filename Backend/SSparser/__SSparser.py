# -*- coding: utf-8 -*-
"""
Created on Tue May  7 21:45:21 2019

@author: shahar
"""

from ply import yacc
from __SSlexer import tokens

THROW_TYPE = "throw_type"
CONTENT = "content"

def create_parenthesis_handler(l_paren_symbol, r_paren_symbol, meaning):
    def func (p):
        "throw : {} sequence {}".format(l_paren_symbol, r_paren_symbol)
        p[0] = {THROW_TYPE:meaning, CONTENT:p[2]}
    return func

def p_throw(p):
    'throw : THROW'
    throw = p[1].copy()
    throw.update({THROW_TYPE:"basic throw"})
    p[0] = throw 

def p_sequence_f_throw (p):
    'sequence : throw'
    p[0] = [p[1]]

def p_sequence_f_sequence_throw(p):
    'sequence : sequence throw'
    p[0] = p[1] + [p[2]]

p_multiplex = create_parenthesis_handler("[","]","multiplex")
p_synch = create_parenthesis_handler("(",")","synch")
p_passing = create_parenthesis_handler("<",">","passing")
    
def p_error(p):
    print (p, "INVALID SYNTAX!")

SSparser = yacc.yacc(debug=True)