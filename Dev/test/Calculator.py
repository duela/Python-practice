# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 03:29:52 2022

@author: yinku
"""

        
import unittest

from app.calculator import Calculator
class BasicCalculatorTest(unittest.TestCase):
    def test_add(self):
        calc = Calculator()
        result = calc.add(2, 2)
        self.assertEqual(4, result)

    def test_subtract(self):
        calc = Calculator()
        result = calc.subtract(4, 2)
        self.assertEqual(2, result)

    def test_multiply(self):
        calc = Calculator()
        result = calc.multiply(4, 2)
        self.assertEqual(8, result)

    def test_divide(self):
        calc = Calculator()
        result = calc.divide(4, 2)
        self.assertEqual(2, result)
