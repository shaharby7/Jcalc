# -*- coding: utf-8 -*-
"""
Created on Tue May  7 20:40:12 2019

@author: shahar
"""

from ply import lex
import re
from .__throwToken import throwToken
from general_utils import read_config, escape_metacharacters
from Juggling import JugglingException

SYNTAX_CONFIG = read_config("syntax_config")
THROW_TYPES = SYNTAX_CONFIG["THROW_TYPES"]
WHITE_SPACES = list("\t ")

tokens = ['THROW',
          'L_PARENTHESIS',
          'R_PARENTHESIS',
          'HANDS_ASSIGNMENT'
          ]

literals = "!"

t_ignore = r"".join([str(throw_params["SEP"]) for throw_params in THROW_TYPES.values()] + WHITE_SPACES)


def get_parenthesis_regex(L_or_R):
    list_of_chars = []
    for throw_type, throw_parameters in THROW_TYPES.items():
        char = throw_parameters[L_or_R]
        char = str(char)
        char = escape_metacharacters(char)
        list_of_chars.append(char)
    return "|".join(list_of_chars)


t_L_PARENTHESIS = get_parenthesis_regex("L_PAREN")

t_R_PARENTHESIS = get_parenthesis_regex("R_PAREN")


def t_THROW(t):
    r"[0-9|a-z]x?(p[0-9]|p)?(h[R|L]|h)?"
    is_hand_spec = False
    is_pass = False
    pass_to = None
    hand_to = None
    crossed = __is_throw_crossed(t)
    beats_number = __calculate_beats_number_of_throwtoken(t)
    dst_match = re.match(r"(p[0-9])?(p)?(h[L|R])?(h)?", t.value[1:])
    is_pass, pass_to = ___get_passing_parameters_for_token(dst_match, is_pass, pass_to)
    hand_to, is_hand_spec = __get_hand_specifications_for_token(dst_match, hand_to, is_hand_spec)
    t.value = throwToken(beats_number=beats_number, crossed=crossed, is_pass=is_pass, is_hand_spec=is_hand_spec,
                         pass_to=pass_to, hand_to=hand_to)
    return t


def __get_hand_specifications_for_token(dst_match, hand_to, is_hand_spec):
    if dst_match.group(3):
        is_hand_spec = True
        hand_to = dst_match.group(3)[1]
    if dst_match.group(4):
        is_hand_spec = True
    return hand_to, is_hand_spec


def ___get_passing_parameters_for_token(dst_match, is_pass, pass_to):
    if dst_match.group(1):
        is_pass = True
        pass_to = dst_match.group(1)[1]
    if dst_match.group(2):
        is_pass = True
    return is_pass, pass_to


def __is_throw_crossed(t):
    if "x" in t.value and not t.value.startswith("x"):
        crossed = True
    else:
        crossed = False
    return crossed


def __calculate_beats_number_of_throwtoken(token):
    beats_char = token.value[0]
    if re.match(r'[0-9]', beats_char):
        beats_number = int(beats_char)
    else:
        beats_number = ord(beats_char) - 96 + 9
    return beats_number


def t_HANDS_ASSIGNMENT(t):
    r"\<([L|R]\|)*[R|L]\>"
    hands = list(t.value.replace("<", "").replace(">", "").replace("|", ""))
    t.value = throwToken(throw_type="hands_assignment", sub_throws=hands)
    return t


def t_error(t):
    raise JugglingException(message="Illegal character '%s'" % t.value[0],
                            problematic_beat=-1)


lexer = lex.lex()
