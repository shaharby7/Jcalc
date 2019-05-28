# -*- coding: utf-8 -*-
"""
Created on Tue May  7 20:40:12 2019

@author: shahar
"""

from ply import lex
import re
from .__throwToken import throwToken
from general_utils import read_config, escape_metacharacters

SYNTAX_CONFIG = read_config("syntax_config")
THROW_TYPES = SYNTAX_CONFIG["THROW_TYPES"]
WHITE_SPACES = list("\t ")

tokens = ['THROW',
          'L_PARENTHESIS',
          'R_PARENTHESIS',
          'HANDS_ASSIGNMENT'
          ]

literals = "LR"

t_ignore = r"".join([str(throw_type["SEP"]) for throw_type in THROW_TYPES] + WHITE_SPACES)


def get_parenthesis_regex(L_or_R):
    list_of_chars = []
    for thorw_type in THROW_TYPES:
        char = thorw_type[L_or_R]
        char = str(char)
        char = escape_metacharacters(char)
        list_of_chars.append(char)
    return "|".join(list_of_chars)


t_L_PARENTHESIS = get_parenthesis_regex("L_PAREN")

t_R_PARENTHESIS = get_parenthesis_regex("R_PAREN")


def t_THROW(t):
    r"[0-9|a-z]x?(p[0-9]|p)?(h[R|L]|h)?"
    crossed = False
    is_hand_spec = False
    is_pass = False
    pass_to = None
    hand_to = None
    beats_char = t.value[0]
    if "x" in t.value and not t.value.startswith("x"):
        crossed = True
    if re.match(r'[0-9]', beats_char):
        beats_number = int(beats_char)
    else:
        beats_number = ord(beats_char) - 96 + 9
    dst_match = re.match(r"(p[0-9])?(p)?(h[L|R])?(h)?", t.value[1:])
    if dst_match.group(1):
        is_pass = True
        pass_to = dst_match.group(1)[1]
    if dst_match.group(2):
        is_pass = True
    if dst_match.group(3):
        is_hand_spec = True
        hand_to = dst_match.group(3)[1]
    if dst_match.group(4):
        is_hand_spec = True
    t.value = throwToken(beats_number=beats_number, crossed=crossed, is_pass=is_pass, is_hand_spec=is_hand_spec,
                         pass_to=pass_to, hand_to=hand_to)
    return t


def t_HANDS_ASSIGNMENT(t):
    r"\<([L|R]\|)*[R|L]\>"
    hands = list(t.value.replace("<", "").replace(">", "").replace("|", ""))
    t.value = throwToken(throw_type="hands_assignment", sub_throws=hands)
    return t


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()
