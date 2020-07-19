#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    #
    time = s[len(s) - 2]
    sp = s.split(":")
    if time == "P" and sp[0] != "12":
        sp[0] = int(sp[0]) + 12
        if sp[0] == "24":
            sp[0] = "00"
    
    if time == "A" and sp[0] == "12":
        sp[0] = "00"
    
    return str(sp[0]) + ":" + str(sp[1]) + ":" + str(sp[2][0]) + str(sp[2][1])



if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
