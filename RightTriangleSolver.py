# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 02:02:35 2021

@author: pgupt

Question : A Right Triangle Solver app that computes the hypotenuse given the length of the two legs
"""

import sys
import math
print("Welcome to the Right Triangle Solver App")

legOne = input("What is the first leg of the triangle: ")

if any(c.isalpha() for c in str(legOne)):
    print("No alphabets allowed in the traingle side")
    sys.exit()
    
#checking for a negative number
elif float(legOne)<=0:
    print("The leg One cannot have a negative value")
    sys.exit()

legTwo = input("What is the second leg of the triangle: ")

if any(c.isalpha() for c in str(legTwo)):
    print("No alphabets allowed in the traingle side")
    sys.exit()
    
#checking for a negative number
elif float(legTwo)<=0:
    print("The leg Two cannot have a negative value")
    sys.exit()
    
area = 0.5 * float(legOne) * float(legTwo)
roundedArea = round(area, 3)
    
hyp1 = pow(float(legOne),2) + pow(float(legTwo), 2)
hypotenuse = math.sqrt(hyp1)
roundedHyp = round(hypotenuse, 3)

print("For a triangle with legs of", legOne, "and", legTwo, "the hypotenuse is", str(roundedHyp))
print("For a triangle with legs of", legOne, "and", legTwo, "the area is", str(roundedArea))

