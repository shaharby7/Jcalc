from Juggling import Pattern as _Pattern, suggest_valid_pattern as _suggest_valid_pattern, \
    JugglingException as _JugglingException
from math import ceil


def crate_transaction_pattern(pattern1, pattern2):
    _assert_patterns_are_valid(pattern1, pattern2)
    full_circle_of_pattern1 = _double_pattern_to_full_circle(pattern1)
    full_circle_of_pattern2 = _double_pattern_to_full_circle(pattern2)
    from_1_to_2 = _find_one_way_transaction(full_circle_of_pattern1, pattern2)
    from_2_to_1 = _find_one_way_transaction(full_circle_of_pattern2, pattern1)
    transaction_pattern = _Pattern(siteswap=None, beatmap=from_1_to_2.beatmap + from_2_to_1.beatmap)
    return transaction_pattern


def _find_one_way_transaction(full_circle_of_pattern1, pattern2):
    two_patterns_united = _Pattern(siteswap=None, beatmap=full_circle_of_pattern1.beatmap + pattern2.beatmap)
    valid_transaction = _suggest_valid_pattern(two_patterns_united,
                                               (len(full_circle_of_pattern1.beatmap), len(two_patterns_united.beatmap)))
    return valid_transaction


def _double_pattern_to_full_circle(pattern):
    beatmap_length = len(pattern.beatmap)
    highest_throw = pattern.highest_throw
    double_by = ceil(highest_throw / beatmap_length)
    return _Pattern(siteswap=None, beatmap=pattern.beatmap * double_by)


def _assert_patterns_are_valid(pattern1, pattern2):
    for pattern in [pattern1, pattern2]:
        if pattern.problems:
            raise _JugglingException("Cannot create transaction for invalid pattern - {}".format(pattern.siteswap))
