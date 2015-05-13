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
    #sort(arr, 0, length - 1)
    sort_3_way(arr, 0, length - 1)

def sort(arr, lo, hi):
    if lo >= hi:
        return
    p = partition(arr, lo, hi)
    sort(arr, lo, p - 1)
    sort(arr, p + 1, hi)

def partition(arr, lo, hi):
    v = lo
    i = lo + 1
    j = hi
    while True:
        while arr[i] <= arr[v]:
            if i >= hi:
                break
            i += 1
        while arr[j] >= arr[v]:
            if j <= lo:
                break
            j -= 1
        if i >= j:
            break
        swap(arr, i, j)
    swap(arr, lo, j)
    return j

def sort_3_way(arr, lo, hi):
    if lo >= hi:
        return
    lt = lo
    gt = hi
    i = lt + 1
    v = arr[lo]
    while i <= gt:
        c = arr[i] - v
        if c < 0:
            swap(arr, i, lt)
            i += 1
            lt += 1
        elif c > 0:
            swap(arr, i, gt)
            gt -= 1
        else:
            i += 1
    sort_3_way(arr, lo, lt - 1)
    sort_3_way(arr, gt + 1, hi)

def main():
    arr = prepare()
    print arr
    quick_sort(arr)
    print arr

if __name__ == '__main__':
    main()
