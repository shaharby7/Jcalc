# -*- coding: utf-8 -*-
"""
Created on Tue May  7 21:45:21 2019

@author: shahar
"""

from ply import yacc
from __SSlexer import tokens

THROW_TYPE = "throw_type"
CONTENT = "content"


def p_sequence_f_sequence_throw(p):
    '''sequence : sequence throw
                | throw'''
    if len(p)==2:
        p[0] = [p[1]]
    elif len (p)==3:
        p[0] = p[1] + [p[2]]


def p_throw(p):
    'throw : THROW'
    throw = p[1].copy()
    throw.update({THROW_TYPE:"basic throw"})
    p[0] = throw 

def p_spetial_throws(p):
    'throw : L_PARENTHESIS sequence R_PARENTHESIS'
    throw_type = "INVALID!"
    
    
def p_error(p):
    print (p, "INVALID SYNTAX!")

SSparser = yacc.yacc(debug=True)