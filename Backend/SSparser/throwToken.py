# -*- coding: utf-8 -*-
"""
Created on Thu May 16 16:28:22 2019

@author: shahar
"""

class throwToken(object):
    
    def __init__(self, throw_type="base_throw", beats_number = None, crossed = None, sub_throws = None):
        self.__dict__.update(locals())
        del self.__dict__["self"]
    
    def __repr__(self):
        pass
        rel_values = ["{}={}".format(str(k), str(v)) for k,v in self.__dict__.items() if v]
        return "throwToken({})".format(",".join(rel_values))