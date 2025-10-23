#!/usr/bin/env python3 

"""
oaks_debugme.py

Descriptions: 
    Filter oak species from a CSV file and save them to a new CSV file. 
    Additionally, it can identify oak species even with minor typos in the genus name. 
    Docstring includes examples and can be tested with doctest set in the key function is_an_oak(name).  

Usage:
    python3 oaks_debugme.py
"""

import csv
import sys
import os
import difflib

def is_an_oak(name):
    """ 
    Returns True if the genus is 'Quercus' (case-insensitive).
    Allows minor typos (like one-character mistakes).

    Examples:
    >>> is_an_oak('Quercus robur')
    True
    >>> is_an_oak('quercus petraea')
    True
    >>> is_an_oak('Fagus sylvatica')
    False
    >>> is_an_oak('Quercuss something')
    True
    >>> is_an_oak('Querqus alba')
    True
    """
    name = name.strip().lower()
    genus = name.split(" ")[0]
    # Find the similarity ratio between input and "quercus"
    similarity = difflib.SequenceMatcher(None, genus, "quercus").ratio()
    return similarity > 0.8  # accept if more than 80% similar

def main(argv): 
    f = open('../data/TestOaksData.csv','r')
    g = open('../data/JustOaksData.csv','w')
    taxa = csv.reader(f)
    csvwrite = csv.writer(g)
    oaks = set()
    for row in taxa:
        print(row)
        print ("The genus is: ") 
        print(row[0] + '\n')
        if is_an_oak(row[0]):
            print('FOUND AN OAK!\n')
            csvwrite.writerow([row[0], row[1]])    

    return 0
    
if (__name__ == "__main__"):
    status = main(sys.argv)