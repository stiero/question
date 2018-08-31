#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 12:19:06 2018

@author: henson
"""

file_open = open('data.dat', 'r')

file = file_open.readlines()

file_open.close()

########################################################
def file_clean(file):
    
    file_cleaned = []
    for line in file:
        line = line.strip()
        line = " ".join(line.split())
        line = line.replace("POINT ID.", "POINT_ID")
        #line = line.replace("FREQUENCY =", "FREQUENCY=")
        line = line.replace(" ", ",")
        #line = list(filter(None, line))
        file_cleaned.append(line)
    return file_cleaned
        
file_cleaned = file_clean(file)



def frequency_parser(file):
    
    store = {}
    
    for i, line in enumerate(file):
        if "FREQUENCY" in line and line.startswith("FREQUENCY"):
            line = line.replace(",", "")
            store['FREQUENCY_' + str(i)] = line.strip()            
    return store

freqs = frequency_parser(file_cleaned)
    


# =============================================================================
# def point_id_parser(file):
#     
#     for i, line in enumerate(file):
#         for j, elem in enumerate(freqs):
#             if freqs[elem] in line:
#                 line = line.strip()
#                 line = list(filter(None, line))
#                 print(line)
# =============================================================================


def point_id_parser(file):
    
    store = []
    
    for i, line in enumerate(file):
        if line.startswith("POINT_ID"):
            lines = []
            #lines.append(line)
            #file[i+1] = str(file[i+1])[2:]
            lines.append(file[i+1:i+19])
            
            store.append(lines)
            
            #store[str(file[i+1])] = lines
    
    #return store

#aa = point_id_parser(file_cleaned)

    for coll in store:
        for sub_coll in coll:
            for i, line in enumerate(sub_coll):
                if i % 2 == 0:
                    sub_coll[i] = str(sub_coll[i])[2:]
                    #print(type(sub_coll[i]))
                    
    return store

point_id_parser(file_cleaned)
        


new = point_id_parser(file_cleaned)
            
            
import csv

with open("output.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows(new)            














point_id_parser(file)
