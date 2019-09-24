from general_utils import read_config, reduce_repetitive_siteswaps, xor
import functools

SYNTAX_CONFIG = read_config("syntax_config")
THROW_TYPES = SYNTAX_CONFIG["THROW_TYPES"]


def compose_siteswap(beatmap):
    siteswap = ""
    for beat in beatmap:
        if beat.is_fake_for_sync:
            continue
        current_beat_siteswap = __compose_siteswap_for_beat(beat)
        siteswap += current_beat_siteswap
    return reduce_repetitive_siteswaps(siteswap)


def __compose_siteswap_for_beat(beat):
    throws_representation = __create__initial_throws_representation(beat)
    for throw_type in __order_throw_types_by_ss_level():
        throws_representation = __reduce_throws_representation_by_throw_type(throws_representation, throw_type, beat)
        if len(throws_representation) == 1:
            return throws_representation[0][0]


def __create__initial_throws_representation(beat):
    return [
        (__get_base_throw_representation(throw), [throw])
        for throw in beat.throws
    ]


def __reduce_throws_representation_by_throw_type(throws_representation, throw_type, beat):
    aggregated_throws_representations = __aggregate_throws_representation_by_throw_type(throws_representation,
                                                                                        throw_type)
    new_throws_representation = []
    for group_of_throws_representation in aggregated_throws_representations.values():
        representation, represented_throws = __combine_throws_representation_by_throw_type(
            group_of_throws_representation, throw_type, beat)
        new_throws_representation.append((representation, represented_throws))
    return new_throws_representation


def __aggregate_throws_representation_by_throw_type(throws_representation, throw_type):
    identifier_to_group_by = THROW_TYPES[throw_type]["COMMON_IDENTIFIER_IN_THROW_OBJ"]
    if identifier_to_group_by:
        aggregated_throws_representation = {}
        for representation, represented_throws in throws_representation:
            one_represented_throw = represented_throws[0]
            one_represented_throw_identifier_value = one_represented_throw.src.__dict__[identifier_to_group_by]
            aggregated_throws_representation.setdefault(one_represented_throw_identifier_value, []).append(
                (representation, represented_throws))
        return aggregated_throws_representation
    return {"all": throws_representation}


def __combine_throws_representation_by_throw_type(throws_representation, throw_type, beat):
    throw_config = THROW_TYPES[throw_type]
    separator, l_paren, r_paren = throw_config["SEP"], throw_config["L_PAREN"], throw_config["R_PAREN"]
    new_representation = __create_new_representation(l_paren, r_paren, separator, throws_representation, beat)
    new_represented_throws = __combine_all_represented_throws(throws_representation)
    if throw_type == "sync" and beat.beat_duration == 1 and len(throws_representation) > 1:
        new_representation += "!"
    return new_representation, new_represented_throws


def __combine_all_represented_throws(throws_representation):
    all_represented_throws = [represented_throws for _, represented_throws in throws_representation]
    new_represented_throws = functools.reduce(lambda a, b: a + b, all_represented_throws)
    return new_represented_throws


def __create_new_representation(l_paren, r_paren, separator, throws_representation, beat):
    all_representations = [representation for representation, _ in throws_representation]
    if len(all_representations) > 1:
        new_representation = l_paren + separator.join(all_representations) + r_paren
    else:
        new_representation = all_representations[0]
    return new_representation


def __get_base_throw_representation(throw_obj):
    representation = __get_beats_char_representation_for_base_throw(throw_obj)
    should_add_x = __should_add_x_to_base_throw_representation(throw_obj)
    added_p_value = __get_added_p_value_for_base_throw(throw_obj)
    if should_add_x:
        representation += "x"
    representation += added_p_value
    return representation


def __should_add_x_to_base_throw_representation(throw_obj):
    if throw_obj.beats > 0:
        is_throw_between_hands = throw_obj.src.side != throw_obj.dst.side
        is_throw_in_uneven_number_of_beats = bool(throw_obj.beats % 2)
        if xor(is_throw_between_hands, is_throw_in_uneven_number_of_beats):
            return True
    return False


def __get_added_p_value_for_base_throw(throw_obj):
    if throw_obj.beats > 0:
        if throw_obj.src.juggler != throw_obj.dst.juggler:
            return "p" + str(throw_obj.dst.juggler)
    return ""


def __get_beats_char_representation_for_base_throw(throw_obj):
    if throw_obj.beats <= 9:
        representation = str(throw_obj.beats)
    else:
        representation = chr(throw_obj.beats + 96 - 9)
    return representation


def __order_throw_types_by_ss_level():
    siteswap_levels_list = []
    current_siteswap_level = 0
    while current_siteswap_level < len(THROW_TYPES):
        for throw_type, throw_params in THROW_TYPES.items():
            if throw_params["SITESWAP_LEVEL"] == current_siteswap_level:
                siteswap_levels_list.append(throw_type)
                break
        current_siteswap_level += 1
    return siteswap_levels_list
