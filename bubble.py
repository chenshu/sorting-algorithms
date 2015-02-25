#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint

def prepare():
    cnt = 10
    return [randint(0, cnt) for _ in range(cnt)]

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

# swap O(N^2)
# compare O(N^2)
def bubble_sort(arr):
    length = len(arr)
    for i in range(length):
        for j in range(0, length - i - 1):
            if arr[j] > arr[j + 1]:
                swap(arr, j, j + 1)

def main():
    arr = prepare()
    print arr
    bubble_sort(arr)
    print arr

if __name__ == '__main__':
    main()
