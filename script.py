#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 21:41:54 2018

@author: tauro
"""

# Opening file
file_open = open('data.dat', 'r')
file = file_open.readlines()
file_open.close()


# Some cleaning tasks
def file_clean(file):
    
    file_cleaned = []
    for line in file:
        line = line.strip()     # Remove whitespaces at begining an end of line
        line = " ".join(line.split()) # Remove more than one whitespace between entries
        line = line.replace("POINT ID.", "POINT_ID") # Makes it easier for querying later
        line = line.replace(" ", ",")   # Replaced whitespace with comma
        file_cleaned.append(line)
    return file_cleaned
        
file_cleaned = file_clean(file)


# Parsing frequency values from file
def frequency_parser(file):
    
    store = []
    for i, line in enumerate(file):
        if "FREQUENCY" in line and line.startswith("FREQUENCY"):
            line = line.replace(",", "")
            line = line.strip()
            line = line[10:]
            store.append(line)
    return store

freqs = frequency_parser(file_cleaned)


# Parsing point_id and its corresponding observations
def point_id_parser(file):
    
    store = []
    
    for i, line in enumerate(file):
        if line.startswith("POINT_ID"):
            lines = []
            lines.append(file[i+1:i+19])    # Since every FREQUENCY value has a 18 lines of POINT ID. and its corresponding readings below it
            store.append(lines)
            
    store = [item for sublist in store for item in sublist]
    
    # Removing the extra 0 before the POINT ID. value - only occurs on alternate lines
    for j, coll in enumerate(store):
        for i, line in enumerate(coll):
            if i % 2 == 0:
                coll[i] = str(coll[i])[2:]
                coll[i] = str(coll[i] + "," + coll[i+1] + "," + freqs[j])
                coll[i+1] = None
            
        # This is to remove the redundant phase rows, now that we have merged magnitude and phase rows into one.
        # Tried doing the below steps more 'elegantly' in the loop above, but it messed with the indices.
        # Hence, I am looping through the same list again.          
        
        for i, line in enumerate(coll):
            if line == None:
                del coll[i]
                                 
    return store


point_ids = point_id_parser(file_cleaned)

#Flattening list of lists into a single list - helps when writing to csv
point_ids = [item for sublist in point_ids for item in sublist]

columns = """point_id, type, t1_magnitude, t2_magnitude, t3_magnitude,
r1_magnitude, r2_magnitude, r3_magnitude, t1_phase, t2_phase,
t3_phase, r1_phase, r2_phase, r3_phase, frequency"""

point_ids.insert(0, columns)


# Writing list to csv
import csv # Built in Python module, not third party

def list_to_csv(listname, filename):

    with open(filename, "w") as f:
        writer = csv.writer(f, delimiter=",")
        for row in listname:
            writer.writerow(row.split(",")) # This was the source of the previous csv error
          

list_to_csv(point_ids, "output.csv")