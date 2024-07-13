# Task 
# Given an integer, n, perform the following conditional actions:

# If n is odd, print Weird
# If n is even and in the inclusive range of 2 to 5, print Not Weird
# If n is even and in the inclusive range of 6 to 20, print Weird
# If n is even and greater than 20, print Not Weird
# Complete the stub code provided in your editor to print whether or not n is weird.

# Input Format
# A single line containing a positive integer, n.

# Constraints
# 1 <= n <= 100

# Output Format
# Print Weird if the number is weird; otherwise, print Not Weird.

# Explanation
# Sample Case 0: n =3
# n is odd and odd numbers are weird, so we Werid
# Sample Case 1: n = 24
# n > 20 and n is even, so it is not werid. Thus, we print Not Werid

## Code 

#!/bin/python3

import math
import os
import random
import re
import sys

N = int(raw_input().strip())

if N % 2 != 0:
    print "Weird"
elif N % 2 == 0 and N >= 2 and N <= 5:
    print "Not Weird"
elif N % 2 == 0 and N >= 6 and N <= 20:
    print "Weird"
elif N % 2 == 0 and N > 20:
    print "Not Weird"
