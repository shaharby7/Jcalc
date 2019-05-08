# -*- coding: utf-8 -*-
"""
Created on Tue May  7 22:17:10 2019

@author: shahar
"""

import unittest
from SSparser.__SSlexer import lexer
from SSparser import SSparser

class TestSSparser(unittest.TestCase):
    
    def test_lexer(self):
        lexer.input("12x<a")
        tokens = []
        while True:
            tok = lexer.token()
            if not tok:
                break
            tokens.append(tok)
        self.assertEqual(tokens[0].value, (1,False))
        self.assertEqual(tokens[1].value, (2,True))
        self.assertEqual(tokens[2].value, "<")
        self.assertEqual(tokens[3].value, (10,False))
    
    def test_parser(self):
        print SSparser.parse("123")
        