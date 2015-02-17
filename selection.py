#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint

def prepare():
    cnt = 10
    return [randint(0, cnt) for _ in range(cnt)]

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

# swap O(N)
# compare avg O(N^2) best O(N^2) worst O(N^2)    N*(N-1)/2 ~ N^2/2
def selection_sort(arr):
    length = len(arr)
    for i in range(length - 1):
        min = i
        for j in range(i + 1, length):
            if arr[j] < arr[min]:
                min = j
        if i != min:
            swap(arr, i, min)

def main():
    arr = prepare()
    print arr
    selection_sort(arr)
    print arr

if __name__ == '__main__':
    main()
