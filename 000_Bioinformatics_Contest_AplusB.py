#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 13:37:57 2021

@author: alina

****** Bioinformatics Contest 2021 ******

Example: A + B

You have to find the sum of two elements.

    You have to upload the answer to ﻿the provided test, not the source code!

Input Format
The first line of the input contains the number of tests.
Each test is represented as one line with two integers  - the integers to sum

Output Format
For each test output on a separate line the sum of the two integers.

Scoring
This is a non-scoring problem and you will get 0 points for solving it.﻿

Sample Input

2
3 4
0 6

Sample Output

7
6
"""

with open('test-A/input.txt') as file:
    results = []
    for line in file:
        l = line.split(" ")
        if len(l) > 1:
            results.append(str(int(l[0]) + int(l[1])))
    
    with open('test-A/output.txt', 'w') as file:
        file.write('\n'.join(results))