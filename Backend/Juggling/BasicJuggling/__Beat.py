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
        for throw in self.throws:
            if throw == throw_obj:
                throw.set_new_dst(shift_to_hand)
                throw.set_new_beats_number(shift_to_beat)

    def clear_catches(self):
        self.catches = []

    def add_catch(self, throw_obj, beat_number_of_throw, beat_number_of_catch, catch_after_period):
        throw_obj.set_route_description(beat_number_of_throw, beat_number_of_catch, catch_after_period)
        self.catches.append(throw_obj)

    def get_throws_catches_difference(self):
        throws_for_hand = self._get_number_of_throws_or_catches_for_hand(throw_or_catch=THROWS)
        catches_for_hand = self._get_number_of_throws_or_catches_for_hand(throw_or_catch=CATCHES)
        all_involved_hands = set(throws_for_hand + catches_for_hand)
        throws_catches_difference = {}
        for hand in all_involved_hands:
            throws_catches_difference.update({hand: {CATCHES: catches_for_hand.get(hand, 0),
                                                     THROWS: throws_for_hand.get(hand, 0),
                                                     DIFFERENCE: catches_for_hand.get(
                                                         hand, 0) - throws_for_hand.get(hand, 0)}})
        return throws_catches_difference

    def _get_number_of_throws_or_catches_for_hand(self, throw_or_catch):
        relevant_list = []
        if throw_or_catch == THROWS:
            relevant_list = [throw.src for throw in self.throws if throw.beats > 0]
        elif throw_or_catch == CATCHES:
            relevant_list = [catch.dst for catch in self.catches]
        return Counter(relevant_list)
