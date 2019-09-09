from ..__meta_functions import declare_new_pattern_validator
from ..__PatternProblem import PatternProblem

MESSAGE_TEMPLATE = """Pattern is not consistent in jugglers amount.
 First beat designated for {first_beat} jugglers while beat {problematic_beat} is for {problematic_number}"""


@declare_new_pattern_validator
def jugglers_amount(pattern):
    first_beat = pattern.beatmap[0].jugglers_amount
    for beat_index, beat in enumerate(pattern.beatmap):
        if not beat.is_fake_for_sync and beat.jugglers_amount != first_beat:
            return PatternProblem(message=MESSAGE_TEMPLATE.format(first_beat=first_beat,
                                                                  problematic_beat=beat_index,
                                                                  problematic_number=beat.jugglers_amount),
                                  problematic_beat=beat_index)
    return None
