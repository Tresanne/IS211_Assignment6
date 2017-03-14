#!/usr/bin/env python
# -*- coding: utf-8 -*-
"test file"

import unittest
from conversions_refactored import *


class Conversion(unittest.TestCase):
    # C, F, K
    knownTempValues = [[300.00, 572.00, 573.15],
                       [400.00, 752.00, 673.15],
                       [350.00, 662.00, 623.15],
                       [380.00, 716.00, 653.15],
                       [430.00, 806.00, 703.15]
                       ]
    # miles, yards, meters
    knownDistValues = [[100.00, 176000.00, 160934.00],
                       [20.00, 35200.00, 32186.90],
                       [50.00, 88000.00, 80467.20],
                       [85.00, 149600.00, 136794.00],
                       [95.00, 167200.00, 152888.00]]

    def testTempConvert(self):
        for c, f, k in self.knownTempValues:
            result = convert("Celsius", "Fahrenheit", c)
            self.assertEqual(f, result)

        for c, f, k in self.knownTempValues:
            result = convert("Kelvin", "Celsius", k)
            self.assertEqual(c, result)

    def testDistConvert(self):
        for mil, yar, met in self.knownDistValues:
            result = convert("Miles", "Yards", mil)
            self.assertEqual(yar, result)

        for mil, yar, met in self.knownDistValues:
            result = convert("Meters", "Miles", met)
            self.assertEqual(mil, result)

    def testSameUnitConvert(self):
        for c, f, k in self.knownTempValues:
            result = convert("Celsius", "Celsius", c)
            self.assertEqual(c, result)

    def testIncompatibleUnits(self):
        for c, f, k in self.knownTempValues:
            result = convert("Celsius", "Meters", c)
            self.assertEqual(c, result)

if __name__ == '__main__':
    unittest.main(verbosity=2)
