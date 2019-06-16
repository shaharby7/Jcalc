# -*- coding: utf-8 -*-
"""
Created on Fri May 10 16:05:54 2019

@author: shahar
"""

from Juggling.SSparser import SSparser
from .__Beat import Beat
from general_utils import swap_hands


class Pattern(object):

    def __init__(self, siteswap):
        self.current_hands_state = ["R"]
        self.siteswap = siteswap
        self.beatmap = []
        self._create_pattern_from_siteswap()
        self.highest_throw = self._get_highest_throw()

    def _create_pattern_from_siteswap(self):
        tokens_tree = SSparser.parse(self.siteswap)
        for throw in tokens_tree:
            self._add_throw(throw)

    def _add_throw(self, throw):
        beat = Beat(throw, self.current_hands_state)
        self.beatmap.append(beat)
        if beat.beat_duration > 1:
            self.beatmap.extend([None] * (beat.beat_duration - 1))
        self._set_hand_state(beat)

    def _set_hand_state(self, beat):
        if beat.implanted_hand_state:
            self.current_hands_state = beat.implanted_hand_state
        elif beat.beat_duration % 2 > 0:
            self.current_hands_state = swap_hands(self.current_hands_state)

    def _get_highest_throw(self):
        highest_throw_for_each_beat = []
        for beat in self.beatmap:
            if beat:
                highest_throw_for_beat = max(throw.beats for throw in beat.throws)
                highest_throw_for_each_beat.append(highest_throw_for_beat)
        return max(highest_throw_for_each_beat)

    def get_landings_at_beat(self, requested_beat):
        landings_at_req_beat = []
        first_relevant_beat = requested_beat - self.highest_throw
        for former_beat_index in range(first_relevant_beat, requested_beat):
            former_beat = self.get_throws_at_beat(former_beat_index)
            relevant_landings = Pattern.get_relevant_throws_to_beat(former_beat,
                                                                    requested_beat - former_beat_index)
            landings_at_req_beat.extend(relevant_landings)
        return landings_at_req_beat

    def get_throws_at_beat(self, requested_beat):
        return self.beatmap[requested_beat % len(self.beatmap)]

    @staticmethod
    def get_relevant_throws_to_beat(former_beat, distance_between_beats):
        relevant_throws_for_landing = []
        if former_beat:
            for former_throw in former_beat.throws:
                if former_throw.beats == distance_between_beats:
                    relevant_throws_for_landing.append(former_throw)
        return relevant_throws_for_landing
