# -*- coding: utf-8 -*-
"""
Created on Tue May  7 21:45:21 2019

@author: shahar
"""

from ply import yacc
from __SSlexer import tokens

def p_throw_THROW ():
    "throw : THROW"
    p[0] = p[1].value[0]

def p_pattern():
    "pattern : pattern throw"
    p[0] =  p[1] + p[2].value[0]

SSparser = yacc.yacc()