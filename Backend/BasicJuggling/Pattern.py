# -*- coding: utf-8 -*-
"""
Created on Fri May 10 16:05:54 2019

@author: shahar
"""

class Pattern(object):
    
    def __init__(self,jugglers_amount=1 ,jugglers_initial_hands=["R"]):
        self.beats = []
        self.jugglers_amount = jugglers_amount
        self.curent_hands_state = jugglers_initial_hands
    
    def __swich_hands (self):
        for juggler_hand in self.currnt_hands_state:
            juggler_hand="R" if juggler_hand=="L" else juggler_hand="L"
    
    