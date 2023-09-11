#!/usr/bin/env python3

def print_fibonacci(length):
    arr = []
    if length == 0:
        arr
    elif length == 1:
        arr.append(0)
    elif length >= 2:
        i = 0
        arr = [0, 1]
        while len(arr) < length:
            total = arr[i] + arr[i + 1]
            arr.append(total)
            i += 1
    print(arr)
        



  