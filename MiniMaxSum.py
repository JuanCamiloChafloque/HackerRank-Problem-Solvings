#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):

    arr.sort()
    minim = 0
    maxim = 0

    for i in range(len(arr) - 1):
        minim = minim + arr[i]
        maxim = maxim + arr[i + 1]
    
    print (str(minim) + " " + str(maxim))
    


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)