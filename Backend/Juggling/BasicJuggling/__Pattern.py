# -*- coding: utf-8 -*-
"""
Created on Fri May 10 16:05:54 2019

@author: shahar
"""

from Juggling.SSparser import SSparser
from .__Beat import Beat
from general_utils import swap_hands
from ..JugglingDebugger import debug_pattern

from copy import deepcopy

HANDS_FOR_JUGGLER = 2


class Pattern(object):

    def __init__(self, siteswap):
        self._current_hands_state = ["R"]
        self.siteswap = siteswap
        self.beatmap = []
        self._set_beatmap()
        self.highest_throw = self._get_highest_throw()
        self._set_catches_to_all_beats()
        self.problems = debug_pattern(self)

    def _set_beatmap(self):
        tokens_tree = SSparser.parse(self.siteswap)
        while len(self.beatmap) == 0 or len(self.beatmap) % HANDS_FOR_JUGGLER:
            for throw in tokens_tree:
                self._add_throw(throw)

    def _add_throw(self, throw):
        beat = Beat(throw, self._current_hands_state)
        self.beatmap.append(beat)
        self._add_empty_beats_if_needed(beat)
        self._set_hand_state(beat)

    def _add_empty_beats_if_needed(self, beat):
        if beat.beat_duration > 1:
            empty_beat = Beat(is_empty=True)
            list_of_empty_beats = [deepcopy(empty_beat)] * (beat.beat_duration - 1)
            self.beatmap.extend(list_of_empty_beats)

    def _set_hand_state(self, beat):
        if beat.implanted_hand_state:
            self._current_hands_state = beat.implanted_hand_state
        elif beat.beat_duration % 2 > 0:
            self._current_hands_state = swap_hands(self._current_hands_state)

    def _get_highest_throw(self):
        highest_throw_for_each_beat = []
        for beat in self.beatmap:
            if not beat.is_empty:
                highest_throw_for_beat = max(throw.beats for throw in beat.throws)
                highest_throw_for_each_beat.append(highest_throw_for_beat)
        return max(highest_throw_for_each_beat)

    def _set_catches_to_all_beats(self):
        for beat_index, beat in enumerate(self.beatmap):
            catches_at_beat = self._calculate_catches_at_beat(beat_index)
            beat.set_catches_at_beat(catches_at_beat)

    def _calculate_catches_at_beat(self, requested_beat):
        catches_at_req_beat = []
        first_relevant_beat = requested_beat - self.highest_throw
        for former_beat_index in range(first_relevant_beat, requested_beat):
            former_beat = self.beatmap[former_beat_index % len(self.beatmap)]
            relevant_catches = Pattern._get_relevant_throws_to_beat(former_beat,
                                                                    requested_beat - former_beat_index)
            catches_at_req_beat.extend(relevant_catches)
        return catches_at_req_beat

    @staticmethod
    def _get_relevant_throws_to_beat(former_beat, distance_between_beats):
        relevant_throws_for_catch = []
        if former_beat:
            for former_throw in former_beat.throws:
                if former_throw.beats == distance_between_beats:
                    relevant_throws_for_catch.append(former_throw)
        return relevant_throws_for_catch
