# -*- coding: utf-8 -*-
"""
Created on Tue May  7 20:40:12 2019

@author: shahar
"""

from ply import lex
import re

tokens = ['THROW'
        ]
literals = "(),<>|xLR"

def t_THROW(t):
    r"[0-9|a-z]x{0,1}"
    crossed =False
    if t.value.endswith("x"):
        crossed=True
    beats_char = t.value[0]
    if re.match(r'[0-9]', beats_char):
        beats_number = int(beats_char)
    else:
        beats_number = ord(beats_char)- 96 +9
    t.value = (beats_number, crossed)
    return t

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
    
lexer = lex.lex()