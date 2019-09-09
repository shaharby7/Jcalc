# -*- coding: utf-8 -*-
"""
Created on Thu May 16 15:59:32 2019

@author: shahar
"""
import json
import os
import functools


def get_real_directory():
    return os.path.dirname(os.path.realpath(__file__))


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
