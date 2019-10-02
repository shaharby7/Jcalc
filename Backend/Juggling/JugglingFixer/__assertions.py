from Juggling.__JugglingException import JugglingException
from .__constant_keys import *
from functools import reduce


def assert_pattern_is_fixable(pattern, exceedings_map):
    __assert_jugglers_amount(pattern)
    __assert_negative_and_positive_exceedings_are_balanced(exceedings_map)


def __assert_jugglers_amount(pattern):
    for problem in pattern.problems:
        if problem.kind == "jugglers_amount":
            raise JugglingException("Its is not possible to fix pattern with jugglers_amount problem",
                                    problematic_beat=problem.problematic_beat)


def __assert_negative_and_positive_exceedings_are_balanced(exceedings_map):
    sum_of_positives = sum([len(exceeding[SOURCE_THROWS]) for exceeding in exceedings_map if
                            exceeding[EXCEEDING] > 0])
    sum_of_negatives = sum([exceeding[EXCEEDING] for exceeding in exceedings_map if
                            exceeding[EXCEEDING] < 0])
    if sum_of_positives + sum_of_negatives != 0:
        raise JugglingException("Exceedings in pattern cannot be balanced")
