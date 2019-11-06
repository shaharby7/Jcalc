"""
The package is designated to find the closest valid pattern to the input pattern. Only public function at this package
is "suggest_valid_pattern"
"""

from .__exceedings_finder import find_exceedings as _find_exceedings
from .__shifting_map_creator import create_shifting_map_for_exceedings as _create_shifting_map_for_exceedings
from .__assertions import assert_pattern_is_fixable as _assert_pattern_is_fixable
from copy import deepcopy


def suggest_valid_pattern(pattern, range_of_beats_to_fix=None):
    """
    Finds the closest valid pattern to the input pattern. The functions finds the beats that has more or less catches
    then throws, and then balances it. For more information about the balancing algorithm please see documentation of
    "_create_shifting_map_for_exceedings". If pattern cannot be balanced JugglingException is being raised.
    :param pattern: Pattern type object
    :param range_of_beats_to_fix: range of beats in which problems at the suggestion pattern would not be allowed. if
        None (as default is) not problems are allowed all over the pattern. If any value is supplied to the function
        the pattern would be treated as linear and not periodic (for more details see documentation of RouteDescription
        class at BasicJuggling.__Throw module).
    :return: valid pattern.
    """
    exceedings = _find_exceedings(pattern, range_of_beats_to_fix)
    _assert_pattern_is_fixable(pattern, exceedings)
    shifting_map = _create_shifting_map_for_exceedings(exceedings)
    new_pattern = deepcopy(pattern)
    for shift_instruction in shifting_map:
        new_pattern.shift_throw(**shift_instruction)
    return new_pattern
