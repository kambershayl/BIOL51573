#!/usr/bin/env python3
import argparse

#prompt the user for position in the Fibonacci sequence
position = input("please enter a position:")

#initialize two integers
a,b = 0,1

for i in range(int(position)):
    a,b = b, a + b

fibonacci_number = a


print(f"the fibonacci number for {position} is {fibonacci_number}")