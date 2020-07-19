#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):

    n = len(arr)
    pos = 0
    neg = 0
    zero = 0

    for i in arr:
        if i > 0:
            pos = pos + 1
        elif i < 0:
            neg = neg + 1
        else:
            zero = zero + 1

    print (str(pos / n ) + "\n" + str(neg / n) + "\n" + str(zero / n))


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
