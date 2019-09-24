from ..__meta_functions import declare_new_pattern_validator
from ..__PatternProblem import PatternProblem

PROBLEM_MESSAGE_TEMPLATE = """Hand {hand_side} doesn't have same amount of catches and throws.
{number_of_more} {kind_of_more}, and only {number_of_less} {kind_of_less}."""

PROBLEM_MESSAGE_MULTIPLE_JUGGLERS_TEMPLATE = """Hand {hand_side} of Juggler number {juggler_number} doesn't have same amount of catches and throws.
{number_of_more} {kind_of_more}, and only {number_of_less} {kind_of_less}."""

CATCHES = "catches"
THROWS = "throws"
DIFFERENCE = "difference"


@declare_new_pattern_validator
def catch_throw_compatibility(pattern):
    problems = []
    for beat_index, beat in enumerate(pattern.beatmap):
        current_beat_problems = _validate_beat(beat, beat_index)
        problems.extend(current_beat_problems)
    return problems


def _validate_beat(beat, beat_index):
    problems_at_beat = []
    hands_throws_catches_difference = beat.get_throws_catches_difference()
    for hand, throws_catches_difference in hands_throws_catches_difference.items():
        if throws_catches_difference[DIFFERENCE] != 0:
            problem_message = _create_message(throws_catches_difference[THROWS], throws_catches_difference[CATCHES],
                                              hand, beat.jugglers_amount)
            problem = PatternProblem(message=problem_message, problematic_beat=beat_index)
            problems_at_beat.append(problem)
    return problems_at_beat


def _create_message(throws_amount, catches_amount, hand, jugglers_amount):
    if jugglers_amount >= 2:
        relevant_template = PROBLEM_MESSAGE_MULTIPLE_JUGGLERS_TEMPLATE
    else:
        relevant_template = PROBLEM_MESSAGE_TEMPLATE
    if catches_amount > throws_amount:
        return relevant_template.format(number_of_more=catches_amount,
                                        kind_of_more=CATCHES,
                                        number_of_less=throws_amount,
                                        kind_of_less=THROWS,
                                        hand_side=hand.side,
                                        juggler_number=hand.juggler)

    return relevant_template.format(number_of_more=throws_amount,
                                    kind_of_more=THROWS,
                                    number_of_less=catches_amount,
                                    kind_of_less=CATCHES,
                                    hand_side=hand.side,
                                    juggler_number=hand.juggler)
