#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint

def prepare():
    cnt = 10
    return [randint(0, cnt) for _ in range(cnt)]

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def quick_sort(arr):
    length = len(arr)
    sort(arr, 0, length - 1)

def sort(arr, lo, hi):
    if lo >= hi:
        return
    m = partition(arr, lo, hi)
    sort(arr, lo, m - 1)
    sort(arr, m + 1, hi)

def partition(arr, lo, hi):
    v = arr[lo]
    i, j = lo, hi + 1
    while i < j:
        while i < hi:
            i += 1
            if arr[i] > v:
                break
        while j > lo:
            j -= 1
            if arr[j] < v:
                break
        if i < j:
            swap(arr, i, j)
    swap(arr, j, lo)
    return j

def main():
    arr = prepare()
    print arr
    quick_sort(arr)
    print arr

if __name__ == '__main__':
    main()
