# -*- coding: utf-8 -*-
"""
Created on Fri May 10 16:17:41 2019

@author: shahar
"""

from .__tokens_handler import tokens_handler
from collections import Counter

CATCHES = "catches"
THROWS = "throws"
DIFFERENCE = "difference"


class Beat(object):
    """
    Logical representation of specific beat at a juggling pattern. Describing all the throws and catches that should
    take place at the beat.

    Main attributes of the class:
    * throws - list of Throw objects, each describes one of the throws that should take place at the beat.
    * catches - list of Throw objects, each describes one of the throws that should take place at the beat. The update
        of the catches attribute is the responsibility of the Pattern object, for only there the information of the
        throws at the other beats is stored. the Throw object has the swap ref for the Throw object of the throw at the
        other beat (in which it placed at the throws attribute).
    * beat_duration - as confusing as it may be, the meaning is not the duration of the throws (witch are stored at the
        Throw object itself) but for the duration of the beat itself. The only use for it is to mention that beats at
        sync patterns are double.
    * implanted_hand_state - will be defined in case of strange cases in which the hand sate at the end of beat is not
        the same as it should be according to the usual rules of the siteswaps (for example, the notation "<L|R|R>" at a
         passing patten)
    * is_fake_for_sync - at sync patterns any second beat is "fake", and has no any throws or catches, to make it easy
        to keep track of those beat the value of that attribute would be set to True.
    """

    def __init__(self, throw_token=None, hand_state_before_beat=None, is_fake_for_sync=False,
                 jugglers_amount_if_fake=0):
        throws, beat_duration, jugglers_amount, implanted_hand_state = \
            tokens_handler(throw_token, hand_state_before_beat) \
                if not is_fake_for_sync else ([], 1, jugglers_amount_if_fake, None)
        self.beat_duration = beat_duration
        self.throws = throws
        self.jugglers_amount = jugglers_amount
        self.implanted_hand_state = implanted_hand_state
        self.is_fake_for_sync = is_fake_for_sync
        self.catches = []

    def shift_throw(self, throw_obj, shift_to_beat, shift_to_hand):
        """
        Responsible for changing a given throw. gets the current throw, and shift if to the beat and the hand that being
            requested.
        :param throw_obj: Throw instance, that is equivalent to the throw that you would like to change.
        :param shift_to_beat: the new beat you would like to implant
        :param shift_to_hand: the new hand you would like to implant.
        :return: None
        """
        for throw in self.throws:
            if throw == throw_obj:
                throw.set_new_dst(shift_to_hand)
                throw.set_new_beats_number(shift_to_beat)

    def clear_catches(self):
        self.catches = []

    def add_catch(self, throw_obj, beat_number_of_throw, beat_number_of_catch, catch_after_period):
        throw_obj.set_route_description(beat_number_of_throw, beat_number_of_catch, catch_after_period)
        self.catches.append(throw_obj)

    def get_throws_catches_difference(self, with_catches_after_period=True):
        """
        :param with_catches_after_period: set to False if calculation needs to consider the pattern as a disposable
            pattern, and not periodic. Helpful at the calculation of transactions and debugging invalid patterns,
            because in those cases the pattern should not consider as periodic.
        :return: dict with the keys: "throws", "catches", "difference", with int values.
        """
        throws_for_hand = self._get_number_of_throws_or_catches_for_hand(THROWS)
        catches_for_hand = self._get_number_of_throws_or_catches_for_hand(CATCHES, with_catches_after_period)
        all_involved_hands = set(throws_for_hand + catches_for_hand)
        throws_catches_difference = {}
        for hand in all_involved_hands:
            throws_catches_difference.update({hand: {CATCHES: catches_for_hand.get(hand, 0),
                                                     THROWS: throws_for_hand.get(hand, 0),
                                                     DIFFERENCE: catches_for_hand.get(
                                                         hand, 0) - throws_for_hand.get(hand, 0)}})
        return throws_catches_difference

    def _get_number_of_throws_or_catches_for_hand(self, throw_or_catch, with_catches_after_period=True):
        relevant_list = []
        if throw_or_catch == THROWS:
            relevant_list = [throw.src for throw in self.throws if throw.beats > 0]
        elif throw_or_catch == CATCHES:
            relevant_list = [catch.dst for catch in self.catches if not (
                    catch.route_description.catch_after_period and not with_catches_after_period)]
        return Counter(relevant_list)
