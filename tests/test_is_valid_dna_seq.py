#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 14:18:01 2021

@author: alina

Resources:
https://realpython.com/python-testing/#writing-your-first-test
"""

import unittest

from dna_nucleotide_count import is_valid_dna_seq


class TestValidSequence(unittest.TestCase):
    
    def test_valid_string(self):
        """
        Test if the string provided is a valid DNA string.
        """
        test_value = "ATCGATCGATGCACAGTGTACA"
        result = is_valid_dna_seq(test_value)
        self.assertTrue(result, "test_value is not a valid DNA sequence.")

    def test_invalid_string(self):
        """
        Test if the string provided is not a valid DNA string.
        """
        test_value = "This is not a DNA string!"
        result = is_valid_dna_seq(test_value)
        self.assertFalse(result, "test_value is a valid DNA sequence!.")        
        
    def test_bad_type_int(self):
        """
        Test if it raises an error.
        """
        test_value = 1
        with self.assertRaises(TypeError):
            is_valid_dna_seq(test_value)
    
    def test_bad_type_list(self):
        """
        Test if it raises an error.
        """
        test_value = ['A', 'T', 'C', 'G']
        with self.assertRaises(TypeError) as context:
            is_valid_dna_seq(test_value)
            self.assertTrue("It raised a TypeError" in str(context.exception))
            
# I'M HERE!!!
# https://stackoverflow.com/questions/129507/how-do-you-test-that-a-python-function-throws-an-exception

if __name__ == '__main__':
    unittest.main()   
