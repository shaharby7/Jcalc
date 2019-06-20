# -*- coding: utf-8 -*-
"""
Created on Fri May 10 16:17:41 2019

@author: shahar
"""

from .__Throw import Throw
from general_utils import swap_hands
from copy import deepcopy


class Beat(object):

    def __init__(self, throw_token=None, hand_state_before_beat=None, is_empty=False):
        if not is_empty:
            throws, beat_duration, jugglers_amount, implanted_hand_state = \
                self._create_beat_from_tokens(throw_token, hand_state_before_beat)
        else:
            throws, beat_duration, jugglers_amount, implanted_hand_state = \
                ([], 1, None, None)
        self.beat_duration = beat_duration
        self.throws = throws
        self.jugglers_amount = jugglers_amount
        self.implanted_hand_state = implanted_hand_state
        self.is_empty = is_empty
        self.catches = None

    def set_catches_at_beat(self, catches):
        self.catches = catches

    @staticmethod
    def _create_beat_from_tokens(throw_token, hand_state, thrower=None, jugglers_amount=None):
        handler = Beat._handlers[throw_token.throw_type]
        throws, beat_duration, jugglers_amount, implanted_hand_state \
            = handler(throw_token, hand_state, thrower, jugglers_amount)
        return throws, beat_duration, jugglers_amount, implanted_hand_state

    @staticmethod
    def _basic_throw_handler(token, hand_state, thrower, jugglers_amount):
        throw = Throw(token, hand_state[0], thrower, jugglers_amount)
        throws = [throw]
        return throws, 1, 1, None

    @staticmethod
    def _passing_throw_handler(token, hand_state, thrower, jugglers_amount):
        del thrower
        del jugglers_amount
        throws = []
        each_beat_duration = []
        jugglers_amount = len(token.sub_throws)
        if jugglers_amount > len(hand_state):
            for i in range(len(hand_state), jugglers_amount):
                hand_state.append("R")
        for thrower, sub_token in enumerate(token.sub_throws):
            current_throw, current_beat_duration, ignored_juggling_anount, implanted_hand_state = \
                Beat._create_beat_from_tokens(throw_token=sub_token,
                                              hand_state=hand_state[thrower],
                                              thrower=thrower,
                                              jugglers_amount=jugglers_amount)
            throws.extend(current_throw)
            each_beat_duration.append(current_beat_duration)
        implanted_hand_state = []
        for idx, hand in enumerate(hand_state):
            if each_beat_duration[idx] % 2 > 0:
                implanted_hand_state.append(swap_hands(hand))
            else:
                implanted_hand_state.append(hand)
        # Todo: add assertion
        return throws, each_beat_duration[0], jugglers_amount, implanted_hand_state

    @staticmethod
    def _sync_throw_handler(token, hand_state, thrower, jugglers_amount):
        throws = []
        current_hand_state = deepcopy(hand_state)
        implanted_hand_state = None
        for sub_token in token.sub_throws:
            current_throw, current_beat_duration, jugglers_amount, implanted_hand_state = \
                Beat._create_beat_from_tokens(throw_token=sub_token,
                                              hand_state=current_hand_state,
                                              thrower=thrower,
                                              jugglers_amount=jugglers_amount)
            throws.extend(current_throw)
            current_hand_state = swap_hands(current_hand_state)
        # TODO: add ! consideration for sync throw of one beat
        return throws, 2, 1, implanted_hand_state

    @staticmethod
    def _multyplex_throw_handler(token, hand_state, thrower, jugglers_amount):
        throws = []
        implanted_hand_state = None
        for sub_token in token.sub_throws:
            current_throw, current_beat_duration, jugglers_amount, implanted_hand_state = \
                Beat._create_beat_from_tokens(throw_token=sub_token,
                                              hand_state=hand_state,
                                              thrower=thrower,
                                              jugglers_amount=jugglers_amount)
            throws.extend(current_throw)
        return throws, 1, 1, implanted_hand_state

    @staticmethod
    def _hand_assignment_handler(token, hand_state, thrower, jugglers_amount):
        del hand_state, thrower, jugglers_amount
        return [], 0, len(token.sub_throws), token.sub_throws

    _handlers = {
        "base_throw": _basic_throw_handler.__func__,
        "sync": _sync_throw_handler.__func__,
        "passing": _passing_throw_handler.__func__,
        "multyplex": _multyplex_throw_handler.__func__,
        "hands_assignment": _hand_assignment_handler.__func__
    }
