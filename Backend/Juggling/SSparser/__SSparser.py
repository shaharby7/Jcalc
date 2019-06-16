# -*- coding: utf-8 -*-
"""
Created on Tue May  7 21:45:21 2019

@author: shahar
"""

from ply import yacc
from .__SSlexer import tokens
from general_utils import read_config
from .__throwToken import throwToken
from copy import deepcopy

SYNTAX_CONFIG = read_config("syntax_config")
THROW_TYPES = SYNTAX_CONFIG["THROW_TYPES"]


def p_sequence_f_sequence_throw(p):
    """sequence : sequence throw
                | throw"""
    if len(p) == 2:
        p[0] = [p[1]]
    elif len(p) == 3:
        p[0] = p[1] + [p[2]]


def p_throw_THROW(p):
    """throw : THROW
             | HANDS_ASSIGNMENT"""
    p[0] = deepcopy(p[1])


def p_spetial_throws(p):
    """throw : L_PARENTHESIS sequence R_PARENTHESIS"""
    throw_type = None
    has_defined = False
    for throw_type in THROW_TYPES:
        if p[1] == throw_type["L_PAREN"] and p[3] == throw_type["R_PAREN"]:
            has_defined = True
            break
    if not has_defined:
        raise Exception()
    p[0] = throwToken(throw_type=throw_type["TYPE"], sub_throws=p[2])


def p_error(p):
    print(p, "INVALID SYNTAX!")


SSparser = yacc.yacc(debug=True)
