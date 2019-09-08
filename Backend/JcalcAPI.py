# -*- coding: utf-8 -*-
"""
Created on Mon May  6 22:43:05 2019

@author: shahar
"""

from app import app
import os

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=os.environ["BACKEND_PORT"])
