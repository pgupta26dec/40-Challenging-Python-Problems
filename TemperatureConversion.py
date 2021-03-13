# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 21:11:43 2021

@author: pgupt

Question:
Convert the degress fahrenheit to degrees kelvin and degrees celsius
"""
import sys
print("Welcome to the Temperature Conversion App")

degreeF = input("\nWhat is the given temperature in degrees Fahrenheit: ")


if any(c.isalpha() for c in str(degreeF)):
    print("No alphabets allowed in the temperature")
    sys.exit()

#Coversion to degree Celsius
degreeC = (float(degreeF) - 32)* 5/9

#Conversion to degree Kelvin
degreeK = degreeC + 273.15

#rounding up the temperatures

roundedF = round(float(degreeF),4)
roundedC = round(float(degreeC), 4)
roundedK = round(float(degreeK), 4)

print("Degrees Fahrenheit:\t", str(roundedF))
print("Degrees Celsius:\t", str(roundedC))
print("Degrees Kelvin:\t\t", str(roundedK))

