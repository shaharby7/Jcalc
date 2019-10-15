from copy import deepcopy
from .__constant_keys import *
from general_utils import is_beat_in_range


def find_exceedings(pattern, range_of_beats_to_fix):
    exceedings = __get_exceeded_hands_per_beats(pattern, range_of_beats_to_fix)
    exceedings_with_sources = __add_source_throws_to_positive_exceedings(exceedings, pattern, range_of_beats_to_fix)
    return exceedings_with_sources


def __get_exceeded_hands_per_beats(pattern, range_of_beats_to_fix):
    exceeded_hands_per_beat = []
    for beat_idx, beat in enumerate(pattern.beatmap):
        if not is_beat_in_range(beat_idx, range_of_beats_to_fix):
            continue
        beat_diff = beat.get_throws_catches_difference(with_catches_after_period=not(bool(range_of_beats_to_fix)))
        for hand, throws_catches_difference_per_hand in beat_diff.items():
            difference = throws_catches_difference_per_hand[DIFFERENCE]
            if difference != 0:
                exceeded_hands_per_beat.append({BEAT_IDX: beat_idx, HAND: hand, EXCEEDING: difference})
    return exceeded_hands_per_beat


def __add_source_throws_to_positive_exceedings(exceedings, pattern, range_of_beats_to_fix):
    exceedings_copy = deepcopy(exceedings)
    for exceeding in exceedings_copy:
        if exceeding[EXCEEDING] > 0:
            source_throws_of_exceeding = __find_source_throws_of_positive_exceeding(exceeding, pattern,
                                                                                    range_of_beats_to_fix)
            exceeding.update({SOURCE_THROWS: source_throws_of_exceeding})
    return exceedings_copy


def __find_source_throws_of_positive_exceeding(exceeding, pattern, range_of_beats_to_fix):
    source_throws = []
    for catch in pattern.beatmap[exceeding[BEAT_IDX]].catches:
        if catch.dst == exceeding[HAND]:
            if not (bool(range_of_beats_to_fix) and catch.route_description.catch_after_period):
                source_throws.append(catch)
        if exceeding[EXCEEDING] == len(source_throws):
            return source_throws
