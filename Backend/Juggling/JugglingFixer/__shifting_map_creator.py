from .__constant_keys import *


def create_shifting_map_for_exceedings(exceedings):
    ordered_list_of_positive_exceedings = _create_ordered_list_of_positive_exceedings(exceedings)
    ordered_list_of_negative_exceedings = _create_ordered_list_of_negative_exceedings(exceedings)
    assert len(ordered_list_of_negative_exceedings) == len(ordered_list_of_positive_exceedings)
    shifting_map = [{**ordered_list_of_positive_exceedings[i], **ordered_list_of_negative_exceedings[i]}
                    for i in range(len(ordered_list_of_negative_exceedings))]
    return shifting_map


def _create_ordered_list_of_positive_exceedings(exceedings):
    list_of_positive_exceedings = []
    for exceeding in exceedings:
        if exceeding[EXCEEDING] > 0:
            for source_throw in exceeding[SOURCE_THROWS]:
                list_of_positive_exceedings.append({THROW_OBJ: source_throw})
    ordered_list_of_positive_exceedings = sorted(list_of_positive_exceedings,
                                                 key=lambda i: i[THROW_OBJ].route_description.beat_number_of_catch)
    return ordered_list_of_positive_exceedings


def _create_ordered_list_of_negative_exceedings(exceedings):
    list_of_negative_exceedings = []
    for exceeding in exceedings:
        if exceeding[EXCEEDING] < 0:
            for _ in range(- exceeding[EXCEEDING]):
                list_of_negative_exceedings.append({SHIFT_TO_BEAT: exceeding[BEAT_IDX], SHIFT_TO_HAND: exceeding[HAND]})
    ordered_list_of_negative_exceedings = sorted(list_of_negative_exceedings, key=lambda i: i[SHIFT_TO_BEAT])
    return ordered_list_of_negative_exceedings
