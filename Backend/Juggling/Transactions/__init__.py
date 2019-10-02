from Juggling import Pattern as _Pattern, suggest_valid_pattern as _suggest_valid_pattern, \
    JugglingException as _JugglingException
from math import ceil
from copy import deepcopy


def crate_transaction_pattern(pattern1, pattern2):
    _assert_patterns_are_valid(pattern1, pattern2)
    full_circle_of_pattern1, full_circle_of_pattern2 = _create_full_period_patterns(pattern1, pattern2)
    from_1_to_2 = _find_one_way_transaction(full_circle_of_pattern1, full_circle_of_pattern2)
    from_2_to_1 = _find_one_way_transaction(full_circle_of_pattern2, full_circle_of_pattern1)
    transaction_pattern = _Pattern(siteswap=None, beatmap=from_1_to_2.beatmap + from_2_to_1.beatmap)
    return transaction_pattern


def _find_one_way_transaction(full_circle_of_pattern1, full_circle_of_pattern2):
    two_patterns_united = _Pattern(siteswap=None,
                                   beatmap=full_circle_of_pattern1.beatmap + full_circle_of_pattern2.beatmap)
    range_to_fix = (len(full_circle_of_pattern1.beatmap), len(two_patterns_united.beatmap) - 1)
    valid_transaction = _suggest_valid_pattern(two_patterns_united, range_to_fix)
    return valid_transaction


def _create_full_period_patterns(pattern1, pattern2):
    highest_throw = max([pattern.highest_throw for pattern in [pattern1, pattern2]])
    results = []
    for pattern in [pattern1, pattern2]:
        beatmap_length = len(pattern.beatmap)
        double_by = ceil(highest_throw / beatmap_length)
        full_period_beatmap = []
        [full_period_beatmap.extend(deepcopy(pattern.beatmap)) for _ in range(double_by)]
        full_period_pattern = _Pattern(siteswap=None, beatmap=full_period_beatmap)
        results.append(full_period_pattern)
    return results


def _assert_patterns_are_valid(pattern1, pattern2):
    for pattern in [pattern1, pattern2]:
        if pattern.problems:
            raise _JugglingException("Cannot create transaction for invalid pattern - {}".format(pattern.siteswap))
