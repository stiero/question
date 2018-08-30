#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 21:41:54 2018

@author: tauro
"""

file_open = open('data.dat', 'r')

file = file_open.readlines()

file_open.close()


def frequency_parser(file):
    
    freqs = []    
    
    for line in file:
        if "FREQUENCY" in line:
            freqs.append(line.strip())            
    return freqs

freqs = frequency_parser(file)
    


