# -*- coding: utf-8 -*-
"""
Created on Tue May  7 22:17:10 2019

@author: shahar
"""

import unittest
from SSparser.__SSlexer import lexer
from SSparser import SSparser
import logging
import os

try:
    os.remove("parselog.txt")
except:
    logging.shutdown()
    

logging.basicConfig(
    level = logging.DEBUG,
    filename = "parselog.txt",
    filemode = "w",
    format = "%(filename)10s:%(lineno)4d:%(message)s"
)

log = logging.getLogger()

class TestSSparser(unittest.TestCase):
        
    def test_lexer(self):
        lexer.input(" 12\t3x<a([")
        tokens = []
        while True:
            tok = lexer.token()
            if not tok: 
                break
            tokens.append(tok)
#        print tokens
    
    def test_parser(self):
        parsed = SSparser.parse("1(2)34", debug=log)
        print (parsed)

logging.shutdown()