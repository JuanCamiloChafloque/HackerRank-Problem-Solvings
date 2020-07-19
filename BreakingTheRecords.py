#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):

    max_s = scores[0]
    min_s = scores[0]
    max_c = 0
    min_c = 0

    for i in range(len(scores) - 1):
        if scores[i + 1] > max_s:
            max_s = scores[i + 1]
            max_c = max_c + 1
        if scores[i + 1] < min_s:
            min_s = scores[i + 1]
            min_c = min_c + 1
    
    res = []
    res.append(max_c)
    res.append(min_c)

    return res




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
