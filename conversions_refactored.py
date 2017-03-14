#!/usr/bin/env python
# -*- coding: utf-8
"refractored"

#!/usr/bin/env python

# Custom Exception Name
class ConversionNotPossible(Exception):
    pass

def convert(fromUnit, toUnit, value):

    if toUnit == fromUnit:
        return value

    # otherwise
    if fromUnit == "Celsius":
        if toUnit == "Fahrenheit":
            return round((value * 9/5.0) + 32.0, 2)
        elif toUnit == "Kelvin":
            return round(value + 273.15, 2)
        else:
            raise ConversionNotPossible("Type mismatch occurred.")

    elif fromUnit == "Fahrenheit":
        if toUnit == "Celsius":
            return round((value - 32.0) * 5/9.0, 2)
        elif toUnit == "Kelvin":
            return round((value + 459.67) * 5/9.0, 2)
        else:
            raise ConversionNotPossible("Type mismatch occurred.")

    elif fromUnit == "Kelvin":
        if toUnit == "Celsius":
            return round(value - 273.15, 2)
        elif toUnit == "Fahrenheit":
            return round((value * 9/5.0) - 459.67, 2)
        else:
            raise ConversionNotPossible("Type mismatch occurred.")

    elif fromUnit == "Miles":
        if toUnit == "Yards":
            return round(value * 1760, 2)
        elif toUnit == "Meters":
            return round(value * 1609.34, 2)
        else:
            raise ConversionNotPossible("Type mismatch occurred.")

    elif fromUnit == "Yards":
        if toUnit == "Miles":
            return round(value * 0.000568182, 2)
        elif toUnit == "Meters":
            return round(value * 0.9144, 2)
        else:
            raise ConversionNotPossible("Type mismatch occurred.")

    elif fromUnit == "Meters":
        if toUnit == "Miles":
            return round(value * 0.000621371, 2)
        elif toUnit == "Yards":
            return round(value * 1.09361, 2)
        else:
            raise ConversionNotPossible("Type mismatch occurred.")
