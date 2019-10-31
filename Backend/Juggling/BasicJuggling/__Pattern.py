# -*- coding: utf-8 -*-
"""
Created on Fri May 10 16:05:54 2019

@author: shahar
"""

from Juggling.SSparser import SSparser
from Juggling.SScomposer import compose_siteswap
from .__Beat import Beat
from general_utils import swap_hands, max_if_null_return_0
from ..JugglingDebugger import debug_pattern

from copy import deepcopy

HANDS_FOR_JUGGLER = 2


class Pattern(object):
    """
    logical representation of juggling pattern.
    An instance of this class can be initiated by pattern, or by a "beatmap" (a list of Beat type instances).
    It is HIGHLY RECOMMENDED to use only public methods, otherwise sync between the different beats at the beatmap
    is not promised.

    Main attributes of the class:
    * siteswap - str siteswap that represent the pattern. If the class is initiated by beatmap or if beatmap has changed
        as a result of using one of the public methods of an instance SScomposer is being invoked to keep the siteswap
        and the beatmap compatible.
    * beatmap - a list of Beat instances, describing the sequence of what throws and what catches should take place
        at each beat.
    * problems - list of PatternProblems, describing all logical problems at the pattern.
    """

    def __init__(self, siteswap=None, beatmap=None):
        self._current_hands_state = ["R"]
        self.siteswap = None
        self.beatmap = []
        self.problems = []
        self.highest_throw = None
        self._analyze_pattern(siteswap, beatmap)

    def shift_throw(self, throw_obj, shift_to_beat, shift_to_hand):
        """
        Responsible for changing a given throw. gets the current throw, and shift if to the beat and the hand that being
            requested.
        :param throw_obj: Throw instance, that is equivalent to the throw that you would like to change.
        :param shift_to_beat: the new beat you would like to implant
        :param shift_to_hand: the new hand you would like to implant.
        :return: None
        """
        beat_number_of_throw = throw_obj.route_description.beat_number_of_throw
        beat_of_throw = self.beatmap[beat_number_of_throw]
        beat_of_throw.shift_throw(throw_obj, shift_to_beat, shift_to_hand)
        self._analyze_pattern_by_beatmap(self.beatmap)

    def _analyze_pattern(self, siteswap, beatmap):
        if siteswap:
            self._analyze_pattern_by_siteswap(siteswap)
        elif beatmap:
            self._analyze_pattern_by_beatmap(beatmap)
        else:
            raise Exception("Pattern cannot be initialized without siteswap nor beatmap")

    def _analyze_pattern_by_siteswap(self, siteswap):
        self.siteswap = siteswap
        tokens_tree = SSparser.parse(self.siteswap)
        self._create_beatmap_from_tokens_tree(tokens_tree)
        self.highest_throw = self._get_highest_throw()
        self._set_catches_to_beats()
        self.problems = debug_pattern(self)

    def _analyze_pattern_by_beatmap(self, beatmap):
        self.beatmap = beatmap
        self.highest_throw = self._get_highest_throw()
        self._set_catches_to_beats()
        self.siteswap = compose_siteswap(self.beatmap)
        self.problems = debug_pattern(self)

    def _create_beatmap_from_tokens_tree(self, tokens_tree):
        while len(self.beatmap) == 0 or len(self.beatmap) % HANDS_FOR_JUGGLER:
            for throw in tokens_tree:
                self._add_beat_to_beatmap(throw)

    def _add_beat_to_beatmap(self, throw):
        beat = Beat(throw, self._current_hands_state)
        self.beatmap.append(beat)
        self._add_empty_beats_if_needed(beat)
        self._set_hand_state(beat)

    def _add_empty_beats_if_needed(self, beat):
        if beat.beat_duration > 1:
            empty_beat = Beat(is_fake_for_sync=True, jugglers_amount_if_fake=beat.jugglers_amount)
            list_of_empty_beats = [deepcopy(empty_beat)] * (beat.beat_duration - 1)
            self.beatmap.extend(list_of_empty_beats)

    def _set_hand_state(self, beat):
        if beat.implanted_hand_state:
            self._current_hands_state = beat.implanted_hand_state
        elif beat.beat_duration % 2 > 0:
            self._current_hands_state = swap_hands(self._current_hands_state)

    def _get_highest_throw(self):
        highest_throw_for_each_beat = []
        for beat_idx, beat in enumerate(self.beatmap):
            all_throws_length_in_beat = [throw.beats for throw in beat.throws]
            highest_throw_for_beat = max_if_null_return_0(all_throws_length_in_beat)
            highest_throw_for_each_beat.append(highest_throw_for_beat)
        return max(highest_throw_for_each_beat)

    def _set_catches_to_beats(self):
        [beat.clear_catches() for beat in self.beatmap]
        for beat_idx, beat in enumerate(self.beatmap):
            for throw in beat.throws:
                if throw.beats > 0:
                    beat_number_of_catch = (beat_idx + throw.beats) % len(self.beatmap)
                    catch_after_period = bool(beat_idx + throw.beats > len(self.beatmap))
                    self.beatmap[beat_number_of_catch].add_catch(throw, beat_idx, beat_number_of_catch,
                                                                 catch_after_period)
