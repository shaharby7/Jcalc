# -*- coding: utf-8 -*-
"""
Created on Fri May 10 16:20:17 2019

@author: shahar
"""

from general_utils import swap_hands, xor


class Throw(object):

    def __init__(self, token, thrower_hand, thrower, jugglers_amount):
        assert token.throw_type == "base_throw"
        self.src_juggler = thrower if thrower else 0
        self.src_hand = thrower_hand[0]
        self.src_unique = Throw.create_unique(self.src_juggler, self.src_hand)
        self.dst_juggler = None
        self.dst_hand = None
        self.define_dst(token, thrower_hand, thrower, jugglers_amount)
        self.dst_unique = Throw.create_unique(self.dst_juggler, self.dst_hand)
        self.beats = token.beats_number

    def define_dst(self, token, thrower_hand, thrower, jugglers_amount):
        self.define_dst_hand(token, thrower_hand)
        self.define_dst_juggler(token, thrower, jugglers_amount)

    def define_dst_hand(self, token, thrower_hand):
        is_even_number_of_beats = (token.beats_number + 1) % 2
        if xor(is_even_number_of_beats, token.crossed):
            self.dst_hand = thrower_hand
        else:
            self.dst_hand = swap_hands(thrower_hand)

    def define_dst_juggler(self, token, thrower, jugglers_amount):
        if thrower is None:
            self.dst_juggler = 0
        elif not token.is_pass:
            self.dst_juggler = thrower
        elif token.pass_to:
            self.dst_juggler = token.pass_to
        else:
            self.dst_juggler = (thrower + 1) % jugglers_amount

    @staticmethod
    def create_unique(juggler, hand):
        return "P{}H{}".format(str(juggler), hand)
