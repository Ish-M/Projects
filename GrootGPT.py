# -*- coding: utf-8 -*-
"""
Created on Fri May  5 18:44:42 2023

@author: Ishaan
"""
import random


while True:
    if input("USER: ") == "I am Groot":
        print("We are groot")
    elif (random.randrange(0,25))== 10:
        print("Error")
        break
    else:
        print("I am Groot")