#!/usr/bin/env python
# -*- coding: utf-8 -*-
"Unit tests"

import unittest


def convertCelsiusToKelvin(temp):
    """
    returns the temp converted to Kelvins
    """
    return round(temp + 273.15, 2)


def convertCelsiusToFahrenheit(temp):
    """
    returns the temp converted to Fahrenheit
    """
    return round((temp * 9/5.0) + 32.0, 2)


def convertFahrenheitToCelsius(temp):
    """
    returns the temp converted to Celsius
    """
    return round((temp - 32.0) * 5/9.0, 2)


def convertFahrenheitToKelvin(temp):
    """
    returns the temp converted to Kelvins
    """
    return round((temp + 459.67) * 5/9.0, 2)


def convertKelvinToFahrenheit(temp):
    """
    returns the temp converted to Fahrenheit
    """
    return round((temp * 9/5.0) - 459.67, 2)


def convertKelvinToCelsius(temp):
    """
    returns the temp converted to Celsius
    """
    return round(temp - 273.15, 2)


class Conversion(unittest.TestCase):
    # C, F, K
    knownValues = [[300.00, 572.00, 573.15],
                   [400.00, 752.00, 673.15],
                   [350.00, 662.00, 623.15],
                   [380.00, 716.00, 653.15],
                   [430.00, 806.00, 703.15]
                   ]

    def testCelsiusToKelvin(self):
        for c, f, k in self.knownValues:
            result = convertCelsiusToKelvin(c)
            self.assertEqual(k, result)

    def testCelsiusToFahrenheit(self):
        for c, f, k in self.knownValues:
            result = convertCelsiusToFahrenheit(c)
            self.assertEqual(f, result)

    def testFahrenheitToCelsius(self):
        for c, f, k in self.knownValues:
            result = convertFahrenheitToCelsius(f)
            self.assertEqual(c, result)

    def testFahrenheitToKelvin(self):
        for c, f, k in self.knownValues:
            result = convertFahrenheitToKelvin(f)
            self.assertEqual(k, result)

    def testKelvinToCelsius(self):
        for c, f, k in self.knownValues:
            result = convertKelvinToCelsius(k)
            self.assertEqual(c, result)

    def testKelvinToFahrenheit(self):
        for c, f, k in self.knownValues:
            result = convertKelvinToFahrenheit(k)
            self.assertEqual(f, result)
if __name__ == '__main__':
    # set verbosity to True
    unittest.main(verbosity=2)
