# -*- coding: utf-8 -*-
"""
Created on Tue May  7 20:40:12 2019

@author: shahar
"""

from ply import lex
import re
from throwToken import throwToken
from general_utils import read_config

SYNTAX_CONFIG = read_config("syntax_config")
THROW_TYPES = SYNTAX_CONFIG["THROW_TYPES"]
WHITE_SPACES = list ("\t ")

tokens = ['THROW',
          'L_PARENTHESIS',
          'R_PARENTHESIS'
         ]

literals = "LR"

t_ignore = r"".join([str(throw_type["SEP"]) for throw_type in THROW_TYPES] +WHITE_SPACES)

t_L_PARENTHESIS =r"|".join([str(throw_type["L_PAREN"]) for throw_type in THROW_TYPES])

t_R_PARENTHESIS = r"|".join([str(throw_type["R_PAREN"]) for throw_type in THROW_TYPES])


def t_THROW(t):
    r"[0-9|a-z]x{0,1}"
    crossed =False
    if len(t.value)==2:
        crossed=True
    beats_char = t.value[0]
    if re.match(r'[0-9]', beats_char):
        beats_number = int(beats_char)
    else:
        beats_number = ord(beats_char)- 96 +9
    t.value = throwToken(beats_number=beats_number, crossed=crossed)
    return t

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
    
lexer = lex.lex()