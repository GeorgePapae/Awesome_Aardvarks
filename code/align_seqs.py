#!/usr/bin/env python3
""" Aligns sequences in .fasta format """
__author__ = 'Ekadh (er925@ic.ac.uk)'
__version__ = '0.0.1'

import sys

def import_file_sequences():
    """ Import the sequence file. store sequences in a list and calculate lengths """
    seqs = []
    current_seq = ""
    with open('../data/testfasta.fasta', 'r') as f:
        for line in f:
            line = line.strip()
            if line.startswith(">"):
                if current_seq:
                    seqs.append(current_seq)
                    current_seq = ""
                continue
            current_seq = current_seq + line
        if current_seq:
            seqs.append(current_seq)

    seq2 = str(seqs[1])
    seq1 = str(seqs[0])
    l1 = len(seq1)
    l2 = len(seq2)
    if l1 >= l2:
        s1 = seq1
        s2 = seq2
    else:
        s1 = seq2
        s2 = seq1
        l1, l2 = l2, l1 # swap the two lengths
    return(s1, s2, l1, l2)

# A function that computes a score by returning the number of matches starting
# from arbitrary startpoint (chosen by user)
def calculate_score(s1, s2, l1, l2, startpoint):
    """ Starts from a startpoint and calculates matches """
    matched = "" # to hold string displaying alignements
    score = 0
    for i in range(l2):
        if (i + startpoint) < l1:
            if s1[i + startpoint] == s2[i]: # if the bases match
                matched = matched + "*"
                score = score + 1
            else:
                matched = matched + "-"
    print("." * startpoint + matched)           
    print("." * startpoint + s2)
    print(s1)
    print(score) 
    print(" ")
    return score

#import ipdb; ipdb.set_trace()

# Test the function with some example starting points:
# calculate_score(s1, s2, l1, l2, 0)
# calculate_score(s1, s2, l1, l2, 1)
# calculate_score(s1, s2, l1, l2, 5)

def main(argv):
    s1, s2, l1, l2 = import_file_sequences()
    
    my_best_align = None
    my_best_score = -1

    for i in range(l1): # Note that you just take the last alignment with the highest score
        """ Aligns sequences by adding dots to change startpoint and counting matches """
        z = calculate_score(s1, s2, l1, l2, i)
        if z > my_best_score:
            my_best_align = "." * i + s2 # think about what this is doing!
            my_best_score = z 

    with open("../results/align_output.txt", 'w') as out:
        """ Writes output to a text file, check results folder """
        out.write(f"Best alignment:\n{my_best_align}\n")
        out.write(f"{s1}\n")
        out.write(f"Best number of matches: {my_best_score}")
    print("Best score:", my_best_score)
    return 0

if __name__ == "__main__":
    status = main(sys.argv)
    sys.exit(status)
