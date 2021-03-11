# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 17:19:28 2021

@author: pgupt
"""
import sys

print("Welcome to the Letter Counter app")

name = input("What is your name: ")

print("Hello, "+ name)
print("I will count the number of times that a specific letter occurs in a message")

message = input("Please enter a message: ")
if len(message) == 0:
    print("No message entered")
    sys.exit()
letter = input("Which letter would you like to count the occurences of: ")
if len(letter) == 0:
    print("No letter entered")
    sys.exit()

elif len(letter) >1:
    print("Please enter only a single letter")
    sys.exit()

counter = 0

if letter.lower() in message.lower():
    for i in message.lower():
        if i == letter.lower():
            counter+=1
    print("Your message has "+ str(counter) + " " + letter.lower() + " in it")

else:
    print("The given letter is not in the message you entered")

