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


# potential errors:
    # invalid arguments:
        # not a string
        # an invalid string (just text)
        # an invalid string (DNA with NNNNNN regions)
        # an invalid string (RNA)


class TestSequence(unittest.TestCase):
    def test_invalid_string(self):
        """
        Test if the string provided is a valid DNA string.
        """
        data = "This is not a DNA string!"
        result = dna_nucleotide_count(data)
        self.assertIn(member, container) # should I use this assert?




    def test_bad_type(self):
        """
        Test if it raises an error.
        """
        data = "Testing, testing, 1, 2, 3."
        with self.assertRaises(TypeError):
            result = sum(data)



if __name__ == '__main__':
    unittest.main()   