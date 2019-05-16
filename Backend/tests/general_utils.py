# -*- coding: utf-8 -*-
"""
Created on Thu May 16 15:59:32 2019

@author: shahar
"""
import json
import os

def read_config(config_name):
    path = os.path.join("configs",config_name+".json")
    with open (path,"r") as file:
        content = file.read()
        configuration = json.dumps(content)
    return configuration