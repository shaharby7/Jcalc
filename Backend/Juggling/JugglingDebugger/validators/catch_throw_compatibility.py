from ..meta_functions import declare_new_pattern_validator
from ..PatternProblem import PatternProblem
from collections import Counter

PROBLEM_MESSAGE_TEMPLATE = """Hand {hand_id} doesn't have same amount of catches and throws.
{number_of_more} {kind_of_more}, and only {number_of_less} {kind_of_less}."""
CATCHES = "catches"
THROWS = "throws"


@declare_new_pattern_validator
def catch_throw_compatibility(pattern):
    problems = []
    for beat_index, beat in enumerate(pattern.beatmap):
        current_beat_problems = _validate_beat(beat, beat_index)
        if current_beat_problems:
            problems.extend(current_beat_problems)
    return problems


def _validate_beat(beat, beat_index):
    problems_at_beat = []
    throws_for_hand = _get_number_of_throws_or_catches_for_hand(beat, throw_or_catch=THROWS)
    catches_for_hand = _get_number_of_throws_or_catches_for_hand(beat, throw_or_catch=CATCHES)
    all_involved_hands = set(throws_for_hand + catches_for_hand)
    for hand in all_involved_hands:
        problem_at_hand = _validate_beat_for_hand(beat_index, hand,
                                                  throws_for_hand.get(hand, 0),
                                                  catches_for_hand.get(hand, 0))
        if problem_at_hand:
            problems_at_beat.append(problem_at_hand)
    return problems_at_beat


def _get_number_of_throws_or_catches_for_hand(beat, throw_or_catch):
    relevant_list = []
    if throw_or_catch == THROWS:
        relevant_list = [throw.src_unique for throw in beat.throws]
    elif throw_or_catch == CATCHES:
        relevant_list = [throw.dst_unique for throw in beat.catches]
    return Counter(relevant_list)


def _validate_beat_for_hand(beat_index, hand,
                            throws_amount,
                            catches_amount):
    if throws_amount == catches_amount:
        return None
    problem_message = _create_message(catches_amount, throws_amount, hand_id=hand)
    return PatternProblem(message=problem_message, problematic_beat=beat_index)


def _create_message(catches_amount, throws_amount, hand_id):
    if catches_amount > throws_amount:
        return PROBLEM_MESSAGE_TEMPLATE.format(number_of_more=catches_amount,
                                               kind_of_more=CATCHES,
                                               number_of_less=throws_amount,
                                               kind_of_less=THROWS,
                                               hand_id=hand_id)

    return PROBLEM_MESSAGE_TEMPLATE.format(number_of_more=catches_amount,
                                           kind_of_more=CATCHES,
                                           number_of_less=throws_amount,
                                           kind_of_less=THROWS, hand_id=hand_id)
