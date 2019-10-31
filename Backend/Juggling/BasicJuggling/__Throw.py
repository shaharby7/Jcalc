# -*- coding: utf-8 -*-
"""
Created on Fri May 10 16:20:17 2019

@author: shahar
"""

from general_utils import swap_hands, xor, general_class_equality


class Throw(object):
    """
    Logical representation of any throw at a pattern.

    Main attributes:
    * src - UniqueHand object describes the hand that threw the ball
    * dst - UniqueHand object describes the hand that catches the ball
    * beats - the amount of beats that the ball is going to be in the air
    * rout_description - RouteDescription objects that contains information about the relations between the throw and
        the other beats at the pattern. see documentation of RouteDescription for more details.
    """

    def __init__(self, token, thrower_hand, thrower, jugglers_amount):
        self.src = UniqueHand(juggler=(thrower if thrower else 0),
                              hand=(thrower_hand[0]))
        self.dst = None
        self._define_dst(token, thrower_hand, thrower, jugglers_amount)
        self.beats = token.beats_number
        self.route_description = None

    def __eq__(self, other):
        return general_class_equality(self, other)

    def set_route_description(self, beat_number_of_throw, beat_number_of_catch, catch_after_period):
        self.route_description = RouteDescription(beat_number_of_throw, beat_number_of_catch, catch_after_period)

    def set_new_dst(self, unique_hand_obj):
        self.dst = unique_hand_obj

    def set_new_beats_number(self, shift_to_beat):
        beats_to_add = shift_to_beat - self.route_description.beat_number_of_catch
        self.beats += beats_to_add
        self.route_description.set_new_beat_number_of_catch(shift_to_beat)

    def _define_dst(self, token, thrower_hand, thrower, jugglers_amount):
        if token.beats_number > 0:
            dst_hand = Throw._calculate_dst_hand(token, thrower_hand)
            dst_juggling = Throw._calculate_dst_juggler(token, thrower, jugglers_amount)
            self.dst = UniqueHand(hand=dst_hand, juggler=dst_juggling)

    @staticmethod
    def _calculate_dst_hand(token, thrower_hand):
        is_even_number_of_beats = (token.beats_number + 1) % 2
        if xor(is_even_number_of_beats, token.crossed):
            dst_hand = thrower_hand
        else:
            dst_hand = swap_hands(thrower_hand)
        return dst_hand

    @staticmethod
    def _calculate_dst_juggler(token, thrower, jugglers_amount):
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
    """
    Logical representation of one of the hands of one of the jugglers.
    * side - 'L' or 'R'
    * juggler - int that describes the serial number of the juggler at the pattern
    * unique - str of "P{}H{}".format(str(juggler), hand)
    """

    def __init__(self, juggler, hand):
        self.side = hand
        self.juggler = int(juggler)
        self.unique = UniqueHand.create_unique(juggler, hand)

    def __eq__(self, other):
        return general_class_equality(self, other)

    def __hash__(self):
        return hash(self.unique)

    def __repr__(self):
        return self.unique

    @staticmethod
    def create_unique(juggler, hand):
        return "P{}H{}".format(str(juggler), hand)


class RouteDescription(object):
    """
    Objects that contains information about the relations between the throw and the other beats at the pattern
    * beat_number_of_throw - relative to pattern
    * beat_number_of_catch - relative to pattern
    * catch_after_period - set to True only if the catch was of the throw was after a beginning of the patterns from the
        start. basically that attribute allows you to decide by your self weather you would like to treat the pattern as
        periodic or only as a one line of throws. Very useful when trying to calculate a transaction or debugging an
        invalid pattern.
    """

    def __init__(self, beat_number_of_throw, beat_number_of_catch, catch_after_period):
        self.beat_number_of_throw = beat_number_of_throw
        self.beat_number_of_catch = beat_number_of_catch
        self.catch_after_period = catch_after_period

    def __eq__(self, other):
        return general_class_equality(self, other)

    def set_new_beat_number_of_catch(self, new_beat_number_of_catch):
        self.beat_number_of_catch = new_beat_number_of_catch
