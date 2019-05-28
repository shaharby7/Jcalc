# -*- coding: utf-8 -*-
"""
Created on Thu May 16 16:28:22 2019

@author: shahar
"""


class throwToken(object):

    def __init__(self, throw_type="base_throw", beats_number=None, crossed=False, sub_throws=None, is_pass=False,
                 pass_to=None, is_hand_spec=False, hand_to=None):
        self.__dict__.update(locals())
        del self.__dict__["self"]

    def __repr__(self):
        pass
        rel_values = ["{}={}".format(k.__repr__(), v.__repr__()) for k, v in self.__dict__.items() if v]
        return "throwToken({})".format(",".join(rel_values))
