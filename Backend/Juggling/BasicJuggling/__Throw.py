# -*- coding: utf-8 -*-
"""
Created on Fri May 10 16:20:17 2019

@author: shahar
"""

from general_utils import swap_hands, xor


class Throw(object):

    def __init__(self, token, thrower_hand, thrower, jugglers_amount):
        assert token.throw_type == "base_throw"
        self.src_unique = UniqueHand(juggler=(thrower if thrower else 0),
                                     hand=(thrower_hand[0]))
        self.dst_unique = None
        self.__define_dst(token, thrower_hand, thrower, jugglers_amount)
        self.beats = token.beats_number

    def __define_dst(self, token, thrower_hand, thrower, jugglers_amount):
        dst_hand = Throw.calculate_dst_hand(token, thrower_hand)
        dst_juggling = Throw.calculate_dst_juggler(token, thrower, jugglers_amount)
        self.dst_unique = UniqueHand(hand=dst_hand, juggler=dst_juggling)

    @staticmethod
    def calculate_dst_hand(token, thrower_hand):
        is_even_number_of_beats = (token.beats_number + 1) % 2
        if xor(is_even_number_of_beats, token.crossed):
            dst_hand = thrower_hand
        else:
            dst_hand = swap_hands(thrower_hand)
        return dst_hand

    @staticmethod
    def calculate_dst_juggler(token, thrower, jugglers_amount):
        if thrower is None:
            dst_juggler = 0
        elif not token.is_pass:
            dst_juggler = thrower
        elif token.pass_to:
            dst_juggler = token.pass_to
        else:
            dst_juggler = (thrower + 1) % jugglers_amount
        return dst_juggler


class UniqueHand(object):
    def __init__(self, juggler, hand):
        self.side = hand
        self.juggler = juggler
        self.unique = UniqueHand.create_unique(juggler, hand)

    def __eq__(self, other):
        if isinstance(other, UniqueHand) and self.unique == other.unique:
            return True
        return False

    def __hash__(self):
        return hash(self.unique)

    def __repr__(self):
        return self.unique

    @staticmethod
    def create_unique(juggler, hand):
        return "P{}H{}".format(str(juggler), hand)
