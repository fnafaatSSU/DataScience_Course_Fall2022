# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 20:37:59 2022

@author: Fatema Nafa
"""

import kanren
from kanren import run,eq,var,conde
from  kanren import Relation,fact

with open ('coastal_states.txt') as myfile:
    line=myfile.read()
print(type(line))
    
    