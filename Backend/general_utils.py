# -*- coding: utf-8 -*-
"""
Created on Thu May 16 15:59:32 2019

@author: shahar
"""
import json
import os
import functools


def read_config(config_name):
    path = os.path.join("configs", config_name + ".json")
    with open(path, "r") as file:
        content = file.read()
        configuration = json.loads(content)
    return configuration


def escape_metacharacters(some_string):
    all_metacharacters = list(r".^$*+?{}[]\|()")
    results = ""
    for i in some_string:
        if i in all_metacharacters:
            results += "\\" + i
        else:
            results += i
    return results


def swap_hands(hands):
    def swap_one_hand(hand):
        return "L" if hand == "R" else "R"

    if type(hands) is str:
        return swap_one_hand(hands)
    elif type(hands) is list:
        return [swap_one_hand(hand) for hand in hands]


def xor(x, y):
    return (x and not y) or (y and not x)


def reduce_repetitive_siteswaps(siteswap):
    len_siteswap = len(siteswap)
    for chunk_size in range(len_siteswap):
        chunk_size += 1
        chunks = [siteswap[i:i + chunk_size] for i in range(0, len_siteswap, chunk_size)]
        is_repetitive_chunks = functools.reduce(lambda a, b: a == b, chunks)
        if is_repetitive_chunks:
            return chunks[0]
    return siteswap


def max_if_null_return_0(some_list):
    try:
        return max(some_list)
    except ValueError:
        return 0


def is_beat_in_range(beat_idx, beats_to_include):
    if beats_to_include is None:
        return True
    elif isinstance(beats_to_include, tuple):
        return True if (beats_to_include[0] <= beat_idx <= beats_to_include[1]) else False
    elif isinstance(beats_to_include, int):
        return True if beats_to_include == beat_idx else False


def general_class_equality(self, other):
    if isinstance(other, type(self)) and self.__dict__ == other.__dict__:
        return True
    return False
