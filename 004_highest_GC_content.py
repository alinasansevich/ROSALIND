#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 13:54:43 2021

@author: alina

Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. 
Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.

Sample Dataset:

>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT

Sample Output:

Rosalind_0808
60.919540

"""
def gc_content(sequence):
    """
    (str) -> float
    Returns the GC content of sequence.
    """
    gc = sequence.count('G') + sequence.count('C')
    atgc = sequence.count('A') + sequence.count('T') + sequence.count('G') + sequence.count('C')
    
    return (gc/atgc) * 100


def get_highest_gc(filepath):
    f = open(filepath)
    lines = f.read()
    f.close()
    
    ## extract all sequences and their IDs 
    all_seqs = {}
    sequences = lines.split('>')
    sequences = sequences[1:] # drop the first item (an empty str)
    for i in range(len(sequences)):
        name = sequences[i][:13] # extract sequence ID
        seq = sequences[i][13:].splitlines() # remove line breaks
        seq = ''.join(seq) # full sequence as str
        all_seqs[name] = seq
    
    ## calculate GC content for each sequence
    gc_contents = {}
    for name, seq in all_seqs.items():
        gc = gc_content(seq)
        gc_contents[name] = gc
    
    ## find highest GC content value
    max_gc = max(gc_contents.values())
    
    ## find sequence ID with max GC content
    max_id = list(gc_contents.keys())[list(gc_contents.values()).index(max(gc_contents.values()))]
    
    print("{}\n{}".format(max_id, max_gc))



filepath = '/home/alina/Learning_to_Code/My_Projects/ROSALIND/rosalind_gc.txt'
get_highest_gc(filepath)