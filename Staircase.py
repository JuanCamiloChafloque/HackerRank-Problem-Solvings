#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    it = 0
    while it < n:
        it = it + 1
        for i in range(n - it):
            print(" ", end="")
        for i in range(it):
            print("#", end="")
        print()

if __name__ == '__main__':
    n = int(input())

    staircase(n)