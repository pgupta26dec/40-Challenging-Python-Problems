# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 00:28:42 2021

@author: pgupt


Question:
Convert miles per hour to meter per second, upto 2 decimal places
"""
import sys
print("Welcome to the MPH to MPS Conversion App")

milesph = input("What is your speed in miles per hour: ")


if any(c.isalpha() for c in str(milesph)):
    print("No alphabets allowed")
    sys.exit()

#checking for a negative number
elif float(milesph)<0:
    print("The speed cannot have a negative value")
    sys.exit()


meterps = 0.44704 * float(milesph)
#Rounding up to 2 decimal places
rounded = round(meterps, 2)

print("Your speed in Meter per second is: ", str(rounded))
