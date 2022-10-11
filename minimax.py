#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    lo = 0
    hi = 0
    
    for s in range(4):
        lo+=arr[s]
        
    for x in range(3,0,1):
        hi+=arr[x]
        
    
    print(lo,hi)
    


miniMaxSum([1,2,3,4,5])
