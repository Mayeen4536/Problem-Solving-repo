# a = "A"
# c = "C"

# print((ord(c) - ord(a))%26)


# from matplotlib import collections



import collections
import math
import os
import random
import re
import sys

# def almost(word1:str,word2:str):
#     w1 = collections.Counter(word1)
#     w2 = collections.Counter(word2)

#     print(w1)

#     print(set(list(w1.keys()) + list(w2.keys())))

#     for c in set(list(w1.keys()) + list(w2.keys())):
#         print(w1[c])
#         print(w2[c])
#         if abs(w1[c] - w2[c]) > 3:
#             return False

#     return True


# print(almost("aabaab","bbabbc"))


# arr = [3,4,5,6,9]
# arr.sort()
# x = math.floor(len(arr)/2)
# print(arr[x])


#!/bin/python3




#
# Complete the 'findMedian' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

# def findMedian(arr):
#     # Write your code here
#     arr.sort()
#     x = math.floor(len(arr)/2)
#     print(arr[x])





# arr = [1,2,3,4,5]

# result = findMedian(arr)


def lonelyinteger(a):
    # Write your code here
    w = collections.Counter(a)
    print(w)
    print(set(w.keys()))
    for s in set(w.keys()):
        print(s)
        if w[s] == 1:
            return s

a = [1,2,2,1,4,3,4]
print(lonelyinteger(a))



