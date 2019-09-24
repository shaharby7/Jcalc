from .__exceedings_finder import find_exceedings as _find_exceedings
from .__shifting_map_creator import create_shifting_map_for_exceedings as _create_shifting_map_for_exceedings
from .__assertions import assert_pattern_is_fixable as _assert_pattern_is_fixable
from copy import deepcopy


def suggest_valid_pattern(pattern, range_of_beats_to_fix=None):
    exceedings = _find_exceedings(pattern, range_of_beats_to_fix)
    _assert_pattern_is_fixable(pattern, exceedings)
    shifting_map = _create_shifting_map_for_exceedings(exceedings)
    new_pattern = deepcopy(pattern)
    for shift_instruction in shifting_map:
        new_pattern.shift_throw(**shift_instruction)
    return new_pattern
