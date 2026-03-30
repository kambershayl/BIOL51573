#!/usr/bin/env python3
import argparse
###------------- accept and parse command line arguments
# create an argument parser object
parser = argparse.ArgumentParser(description = "This script calculates the number at a given position \
                                 in the Fibonacci sequence")

# add a positional argument, in this case, the position in the Fibonacci sequence
parser.add_argument("position", help = "Position in the Fibonacci sequence", type = int)


# an optional argument for verbose output or not
# if 'store_true', this means assign "True" if the optional argument is specified 
# on the command line, so the default for 'store_true' is actually false
parser.add_argument("-v","--verbose", help = "Print verbose output", action = 'store_true')

# prompt the user for position in the Fibonacci sequence
# position = input("please enter a position:")

#parse the arguments
args = parser.parse_args()













# initialize two integers
a,b = 0,1

for i in range(int(args.position)):
    a,b = b, a + b

fibonacci_number = a

if args.verbose:
    print(f"the fibonacci number for {args.position} is {fibonacci_number}")
else: 
    print(fibonacci_number)