#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 14:32:26 2021

@author: alina

Finding a Shared Motif

Problem

A common substring of a collection of strings is a substring of every member of
 the collection. We say that a common substring is a longest common substring 
 if there does not exist a longer common substring. 
 For example, "CG" is a common substring of "ACGTACGT" and "AACCGTATA", 
 but it is not as long as possible; in this case, "CGTA" is a longest common 
 substring of "ACGTACGT" and "AACCGTATA".

Note that the longest common substring is not necessarily unique; 
for a simple example, "AA" and "CC" are both longest common substrings of 
"AACC" and "CCAA".

Given: A collection of k (k≤100) DNA strings of length at most 1 kbp each in FASTA format.

Return: A longest common substring of the collection. 
(If multiple solutions exist, you may return any single solution.)

Sample Dataset
>Rosalind_1
GATTACA
>Rosalind_2
TAGACCA
>Rosalind_3
ATACA

Sample Output
AC
CA (I found this one)

https://www.bogotobogo.com/python/python_longest_common_substring_lcs_algorithm_generalized_suffix_tree.php
https://en.wikipedia.org/wiki/Longest_common_substring_problem
"""

def lcs(S,T):
    m = len(S)
    n = len(T)
    counter = [[0]*(n+1) for x in range(m+1)]
    longest = 0
    lcs_set = set()
    for i in range(m):
        for j in range(n):
            if S[i] == T[j]:
                c = counter[i][j] + 1
                counter[i+1][j+1] = c
                if c > longest:
                    lcs_set = set()
                    longest = c
                    lcs_set.add(S[i-c+1:i+1])
                elif c == longest:
                    lcs_set.add(S[i-c+1:i+1])

    return lcs_set

# test 1
ret = lcs('academy', 'abracadabra')
for s in ret:
    print(s)
# test 2
ret = lcs('ababc', 'abcdaba')
for s in ret:
    print(s)


sample_path = '/home/alina/Learning_to_Code/My_Projects/ROSALIND/find_longest_common_substring_SAMPLE.txt'

with open(sample_path) as file:
    samples = file.readlines()

num_samples = len(samples) #6

pair_1 = lcs(samples[1], samples[3])
pair_2 = lcs(samples[3], samples[5])


j = 3
shared_motifs = []

for i in range(1, len(samples) - 2, 2):
    shared_motifs.append(lcs(samples[i], samples[j]))
    j += 2
    
    
    

























    
