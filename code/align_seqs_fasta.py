#!/usr/bin/env python3
""" 
Name: align_seqs_fasta.py

Description: Aligns any two sequences in separate files as explicit inputs given as command-line arguments 
in .fasta format and writes the best alignment & its score to a .txt file in ../results/ folder.

Usage:
    (In ../code/ directory)
    $ python3 align_seqs_fasta.py <relative_path_to_fasta1> <relative_path_to_fasta2>
    OR
    $ python3 align_seqs_fasta.py
    (If no files are given, first two .fasta files in ../data/ are used.)
"""

__author__ = 'Ziyang Wang (zw2425@ic.ac.uk)'
__version__ = '0.0.2'         

import sys
import os

def get_input_sequences():
    """Return two .fasta paths (relative to ../data/)."""
    # Default files
    default1 = os.path.join("..", "data", "407228326.fasta")
    default2 = os.path.join("..", "data", "407228412.fasta")

    # User supplied files (must be in relative path ../data/)
    if len(sys.argv) == 3:                     
        f1 = sys.argv[1]
        f2 = sys.argv[2]
    elif len(sys.argv) == 1:                   
        f1, f2 = default1, default2
    else:
        print("If no files are given, first two .fasta files in ../data/ are used.")
        sys.exit(1)

    # Make sure the files exist
    for path in (f1, f2):
        if not os.path.exists(path):
            print(f"Error: file not found -> {path}")
            sys.exit(1)
    return f1, f2

def import_file_sequences(f1, f2):
    """Read two FASTA files, return longer seq as s1, shorter as s2."""
    def read_one(fname):
        seq = ""
        with open(fname, 'r') as f:
            for line in f:
                line = line.strip()
                if line.startswith(">"):
                    continue
                seq += line
        return seq

    seq1 = read_one(f1) # read sequence from first .fasta file
    seq2 = read_one(f2) # read sequence from second .fasta file

    l1 = len(seq1)
    l2 = len(seq2)
    if l1 >= l2:
        s1, s2 = seq1, seq2
    else:
        s1, s2 = seq2, seq1
        l1, l2 = l2, l1
    return s1, s2, l1, l2

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
    # Remove all print() here compared with align_seqs_fasta.py in prevention of printing large outputs to console
    return score

def main(argv):
    file1, file2 = get_input_sequences() # get .fasta file paths

    s1, s2, l1, l2 = import_file_sequences(file1, file2) # Read sequences from both files

    my_best_align = None
    my_best_score = -1

    for i in range(l1):
        z = calculate_score(s1, s2, l1, l2, i)
        if z > my_best_score:
            my_best_align = "." * i + s2
            my_best_score = z

    out_path = os.path.join("..", "results", "align_fasta_output.txt")

    with open(out_path, 'w') as out: # write best alignment and score to align_fasta_output.txt
        out.write(f"Best alignment:\n{my_best_align}\n")
        out.write(f"{s1}\n")
        out.write(f"Best number of matches: {my_best_score}")

    print("Best score:", my_best_score)
    return 0

if __name__ == "__main__":
    status = main(sys.argv)
    sys.exit(status)