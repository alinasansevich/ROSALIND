#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 30 14:49:21 2021

@author: alina

Translating RNA into Protein

Problem
The 20 commonly occurring amino acids are abbreviated by using 20 letters from the English alphabet 
(all letters except for B, J, O, U, X, and Z). Protein strings are constructed from these 20 symbols.
Henceforth, the term genetic string will incorporate protein strings along with DNA strings and RNA strings.

The RNA codon table dictates the details regarding the encoding of specific codons into the amino acid alphabet.

Given: An RNA string 'seq' corresponding to a strand of mRNA (of length at most 10 kbp).

Return: The protein string encoded by seq.

Sample Dataset
AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA

Sample Output
MAMAPRTEINSTRING

"""
genetic_code = {'A': ['GCU', 'GCC', 'GCA', 'GCG'], 
                'C': ['UGU', 'UGC'],
                'D': ['GAU', 'GAC'],
                'E': ['GAA', 'GAG'], 
                'F': ['UUU', 'UUC'],
                'G': ['GGU', 'GGC', 'GGA', 'GGG'],
                'H': ['CAU', 'CAC'],
                'I': ['AUU', 'AUC', 'AUA'],
                'K': ['AAA', 'AAG'],
                'L': ['CUU', 'CUC', 'UUA', 'UUG', 'CUA', 'CUG'],
                'M': ['AUG'],
                'N': ['AAU', 'AAC'],
                'P': ['CCU', 'CCC', 'CCA', 'CCG'],
                'Q': ['CAA', 'CAG'],
                'R': ['CGU', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
                'S': ['AGU', 'AGC', 'UCU', 'UCC', 'UCA', 'UCG'], 
                'T': ['ACU', 'ACC', 'ACA', 'ACG'],
                'V': ['GUU', 'GUC', 'GUA', 'GUG'],
                'W': ['UGG'],
                'Y': ['UAU', 'UAC'],
                'Stop': ['UGA', 'UAG', 'UAA']
                }

filepath = '/home/alina/Learning_to_Code/My_Projects/ROSALIND/rosalind_prot.txt'

def translate(filepath):
    """
    Return the protein string encoded by seq 
    (an RNA string corresponding to a strand of mRNA) read from filepath.
    """
    prot = ''
    
    with open(filepath) as f:
        seq = f.read()
        for i in range(0, len(seq), 3):
            codon = seq[i:i+3]     
            for aa, codon_l in genetic_code.items():
                if codon in codon_l and aa != 'Stop':
                    prot += aa
        
        return prot

translate(filepath)




# ### test

# seq = 'AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA'
# prot = ''
# sample_prot = 'MAMAPRTEINSTRING'

# for i in range(0, len(seq), 3):
#     codon = seq[i:i+3]
#     for aa, codon_l in genetic_code.items():
#         if codon in codon_l and aa != 'Stop':
#             prot += aa

# prot == sample_prot