#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'countInversions' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#
def mergeAndCount(arr, low, mid, high):
    i, j = low, mid + 1
    res = []
    invcount = 0
    while i < mid + 1 and j < high + 1:
        if arr[i] <= arr[j]:
            res.append(arr[i])
            i += 1
        else:
            res.append(arr[j])
            j += 1
            invcount += mid - i + 1

    while i < mid + 1:
        res.append(arr[i])
        i += 1

    while j < high + 1:
        res.append(arr[j])
        j += 1

    for k in range(low, high + 1):
        arr[k] = res[k - low]
    return invcount


def countInv(arr, low, high):
    if high - low + 1 == 1:
        return 0
    else:
        mid = low + (high - low) // 2
        x = countInv(arr, low, mid)
        y = countInv(arr, mid + 1, high)
        z = mergeAndCount(arr, low, mid, high)
        return x + y + z


def countInversions(arr):
    # Write your code here
    return countInv(arr, 0, len(arr) - 1)


if __name__ == '__main__':
    with open("int_array.txt") as f:
        x = f.readlines()
    # arr = [7, 5, 3, 1]
    arr = [int(y.rstrip()) for y in x]
    out = countInversions(arr)
    print(out)