#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 15:46:29 2021

@author: alina

Resources:
https://realpython.com/python-testing/#writing-your-first-test
"""

import unittest

# import the function I want to test with __import__()
target = __import__("001_dna_nucleotide_count.py")
dna_nucleotide_count = target.dna_nucleotide_count


# https://www.geeksforgeeks.org/python-unittest-assertin-function/
# https://www.geeksforgeeks.org/python-unittest-assertnotin-function/

class TestSum(unittest.TestCase):
    def test_invalid_string(self):
        """
        Test if the string provided is a valid DNA string.
        """
        data = "This is not a DNA string!"
        result = dna_nucleotide_count(data)
        self.assertIn(member, container) # should I use this assert?




if __name__ == '__main__':
    unittest.main()   