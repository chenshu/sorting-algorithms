#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint

def prepare():
    cnt = 10
    return [randint(0, cnt) for _ in range(cnt)]

def swap(arr, i, j):
    arr[i - 1], arr[j - 1] = arr[j - 1], arr[i - 1]

def less(arr, i, j):
    return arr[i - 1] < arr[j - 1]

def sink(arr, k, n):
    while True:
        j = 2 * k
        if j > n:
            break
        if j < n and less(arr, j, j + 1):
            j += 1
        if less(arr, k, j):
            swap(arr, k, j)
        k = j

def heap_sort(arr):
    length = len(arr)
    for k in range(length / 2, 0, -1):
        sink(arr, k, length)
    n = length
    while n > 1:
        swap(arr, 1, n)
        n -= 1
        sink(arr, 1, n)

def main():
    arr = prepare()
    print arr
    heap_sort(arr)
    print arr

if __name__ == '__main__':
    main()
