# -*- coding: utf-8 -*-
"""
Created on Tue May  7 22:17:10 2019

@author: shahar
"""

import unittest
from SSparser.__SSlexer import lexer

class TestSSparser(unittest.TestCase):
    
    def test_lexer(self):
        lexer.input("123")
        while True:
            tok = lexer.token()
            if not tok:
                break
            print tok