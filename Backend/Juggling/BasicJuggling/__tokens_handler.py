from .__Throw import Throw
from general_utils import swap_hands
from copy import deepcopy


def _basic_throw_handler(token, hand_state, thrower, jugglers_amount):
    throws = [Throw(token, hand_state[0], thrower, jugglers_amount)]
    return throws, 1, 1, None


def _passing_throw_handler(token, hand_state, thrower, jugglers_amount):
    del thrower
    del jugglers_amount
    throws = []
    each_beat_duration = []
    jugglers_amount = len(token.sub_throws)
    hand_state = __extend_hand_state_if_needed_at_passing(hand_state, jugglers_amount)
    for thrower, sub_token in enumerate(token.sub_throws):
        current_throw, current_beat_duration, ignored_juggling_amount, implanted_hand_state = \
            tokens_handler(throw_token=sub_token,
                           hand_state=hand_state[thrower],
                           thrower=thrower,
                           jugglers_amount=jugglers_amount)
        throws.extend(current_throw)
        each_beat_duration.append(current_beat_duration)
    implanted_hand_state = __create_implanted_hand_state_for_passing_throws(each_beat_duration, hand_state,
                                                                            implanted_hand_state)
    return throws, each_beat_duration[0], jugglers_amount, implanted_hand_state


def __extend_hand_state_if_needed_at_passing(hand_state, jugglers_amount):
    new_hand_state = hand_state.copy()
    if jugglers_amount > len(hand_state):
        for i in range(len(hand_state), jugglers_amount):
            new_hand_state.append("R")
    return new_hand_state


def __create_implanted_hand_state_for_passing_throws(each_beat_duration, hand_state, implanted_hand_state):
    implanted_hand_state = []
    for idx, hand in enumerate(hand_state):
        if each_beat_duration[idx] % 2 > 0:
            implanted_hand_state.append(swap_hands(hand))
        else:
            implanted_hand_state.append(hand)
    return implanted_hand_state


def _sync_throw_handler(token, hand_state, thrower, jugglers_amount):
    throws = []
    current_hand_state = deepcopy(hand_state)
    for sub_token in token.sub_throws:
        current_throw, current_beat_duration, ignored_jugglers_amount, implanted_hand_state = \
            tokens_handler(throw_token=sub_token,
                           hand_state=current_hand_state,
                           thrower=thrower,
                           jugglers_amount=jugglers_amount)
        throws.extend(current_throw)
        current_hand_state = swap_hands(current_hand_state)
    specified_beat_duration = token.specified_beat_duration or 2
    implanted_hand_state = deepcopy(hand_state)
    return throws, specified_beat_duration, 1, implanted_hand_state


def _multyplex_throw_handler(token, hand_state, thrower, jugglers_amount):
    throws = []
    implanted_hand_state = None
    for sub_token in token.sub_throws:
        current_throw, current_beat_duration, ignored_jugglers_amount, implanted_hand_state = \
            tokens_handler(throw_token=sub_token,
                           hand_state=hand_state,
                           thrower=thrower,
                           jugglers_amount=jugglers_amount)
        throws.extend(current_throw)
    return throws, 1, 1, implanted_hand_state


def _hand_assignment_handler(token, hand_state, thrower, jugglers_amount):
    del hand_state, thrower, jugglers_amount
    return [], 0, len(token.sub_throws), token.sub_throws


_handlers = {
    "base_throw": _basic_throw_handler,
    "sync": _sync_throw_handler,
    "passing": _passing_throw_handler,
    "multyplex": _multyplex_throw_handler,
    "hands_assignment": _hand_assignment_handler
}


def tokens_handler(throw_token, hand_state, thrower=None, jugglers_amount=None):
    """
    The functions recursively disassemble hte token tree created by the SSparser. All Throw objects resulted by the
        throw_token are returned only after the lowest hierarchy of the token is being disassembled.
    :param throw_token: output of SSparser, or any lower hierarchy of output of SSparser
    :param hand_state: hand_state of the pattern before throw_token was disassembled
    :param thrower: if pattern is multi-jugglers the param defines to witch of them the token is relevant.
    :param jugglers_amount: pretty self-explanatory
    :return:
        throws - list of Throw objects that represent the throws that are described at the token.
        beat_duration - usually 1, 2 only at sync patterns
        jugglers_amount - different than the param jugglers amount if the token defines more jugglers than the param.
        implanted_hand_state - will be defined in case of strange cases in which the hand sate at the end of beat is not
            the same as it should be according to the usual rules of the siteswaps (for example, the notation "<L|R|R>" at a
            passing patten)
    """
    handler = _handlers[throw_token.throw_type]
    throws, beat_duration, jugglers_amount, implanted_hand_state \
        = handler(throw_token, hand_state, thrower, jugglers_amount)
    return throws, beat_duration, jugglers_amount, implanted_hand_state
