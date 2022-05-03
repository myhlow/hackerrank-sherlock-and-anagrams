#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def sherlockAndAnagrams(s):
    # Write your code here
    count = 0
    for i in range(len(s)-1):
        for j in range(i+1,len(s)):
            l = j-i
            s1 = sorted([x for x in s[i:j]])
            for k in range(i+1, len(s)):
                s2 = sorted([x for x in s[k:k+l]])
                if s1 == s2:
                    count = count+1
                    #print(i,j,k,s1,s2)
    return count
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
