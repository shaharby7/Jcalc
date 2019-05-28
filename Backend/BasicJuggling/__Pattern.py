# -*- coding: utf-8 -*-
"""
Created on Fri May 10 16:05:54 2019

@author: shahar
"""

from SSparser import SSparser
from .__Beat import Beat
from general_utils import swap_hands


class Pattern(object):

    def __init__(self, siteswap):
        self.current_hands_state = ["R"]
        self.siteswap = siteswap
        self.beatmap = []
        self._create_pattern_from_siteswap()

    def _create_pattern_from_siteswap(self):
        tokens_tree = SSparser.parse(self.siteswap)
        for throw in tokens_tree:
            self._add_throw(throw)

    def _add_throw(self, throw):
        beat = Beat(throw, self.current_hands_state)
        self.beatmap.append(beat)
        self.set_current_hand_state(beat)

    def set_current_hand_state(self, beat):
        if beat.implanted_hand_state:
            self.current_hands_state = beat.implanted_hand_state
        elif beat.beat_duration % 2 > 0:
            self.current_hands_state = swap_hands(self.current_hands_state)
