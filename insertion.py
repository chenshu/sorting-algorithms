#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint

def prepare():
    cnt = 10
    return [randint(0, cnt) for _ in range(cnt)]

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

# compare avg O(N^2) best O(N) worst O(N^2)
# swap avg O(N^2) best O(0) worst O(N^2)
def insertion_sort(arr):
    length = len(arr)
    for i in range(1, length):
        for j in range(i, 0, -1):
            if arr[j] < arr[j - 1]:
                swap(arr, j - 1, j)
            else:
                break

def main():
    arr = prepare()
    print arr
    insertion_sort(arr)
    print arr

if __name__ == '__main__':
    main()
