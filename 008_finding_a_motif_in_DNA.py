#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 14:00:36 2021

@author: alina

Finding a Motif in DNA

Problem
Given two strings s and t, t is a substring of s if t is contained as a contiguous
 collection of symbols in s (as a result, t must be no longer than s).
 
The position of a symbol in a string is the total number of symbols found to its left,
including itself (e.g., the positions of all occurrences of 'U' in 
"AUGCUUCAGAAAGGUCUUACG" are 2, 5, 6, 15, 17, and 18).

The symbol at position i of s is denoted by s[i].
A substring of s can be represented as s[j:k], where j and k represent the starting and
 ending positions of the substring in s; for example, if s = "AUGCUUCAGAAAGGUCUUACG", then s[2:5] = "UGCU".
 
The location of a substring s[j:k] is its beginning position j;
note that t will have multiple locations in s if it occurs more than once as a substring of s (see the Sample below).

Given: Two DNA strings s and t (each of length at most 1 kbp).
Return: All locations of t as a substring of s.

Sample Dataset
GATATATGCATATACTT
ATAT

Sample Output
2 4 10
"""

s = 'CGTTAGAAACAATAGACAATAGACAATAGGACAATAGACAATAGGTACAATAGCACAGCACAATAGGTAGCCACCGACAATAGCACAATAGACAATAGGAGGTGAACAATAGTACAATAGACAATAGGATACAATAGACAATAGACAATAGATACAATAGCCGACAATAGTACAATAGGACAATAGAACAATAGGATGCACTACAATAGGAACAATAGCAAAACAATAGAACACAATAGTTTACAATAGACAATAGACAATAGAACAATAGACAATAGGACAATAGCCACAATAGACAATAGGCGACAATAGGTCACAATAGGACAATAGCTAGGAACAATAGATAGTTCAACAATAGTATGGCCACAATAGACACAATAGACAATAGACACAATAGACTGGCCACAATAGACACAATAGTCACAATAGGCCACAATAGTTACAATAGACAATAGACAATAGGTACAATAGGACAATAGCTACAATAGTTACAATAGAAACAATAGGACAATAGACAATAGGGACAATAGGATACAATAGTCACAATAGACAATAGGACAATAGAGGGCATGAGACAATAGGTATACAATAGACAATAGAAAGCTGCAGAACAATAGACACTAAGACAATAGAACACAATAGTGACCAATGCTGTAACAATAGCGTACAACAATAGAACAATAGCCACGCGGACAATAGACAATAGACGTAACAATAGTACAATAGACAATAGTCATTACGAAACAATAGCCTACAATAGAAACAATAGCACAATAGCCCTACAATAGACAATAGTACAATAGGACAATAGCGCACAATAGGGATGACCACAATAGTCAATTTACAATAGTAGTACAATAGACAATAG'
t = 'ACAATAGAC'

# from:
# https://stackoverflow.com/questions/4664850/how-to-find-all-occurrences-of-a-substring

def findall(t, s):
    '''Yields all the positions of the pattern t in the string s.'''
    i = s.find(t)
    while i != -1:
        yield i
        i = s.find(t, i+1)

my_result = [(i + 1) for i in findall(t, s)]

for item in my_result:
    print(item, end=' ')
