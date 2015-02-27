#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint
import copy

def prepare():
    cnt = 10
    return [randint(0, cnt) for _ in range(cnt)]

# compare O(NlgN)
def merge_sort(arr):
    length = len(arr)
    aux = [x for x in range(length)]
    sort(arr, 0, length - 1, aux)

def sort(arr, lo, hi, aux):
    if lo == hi:
        return
    mid = lo + (hi - lo) / 2
    sort(arr, lo, mid, aux)
    sort(arr, mid + 1, hi, aux)
    merge(arr, lo, mid, hi, aux)

def merge(arr, lo, mid, hi, aux):
    i, j = lo, mid + 1
    for k in range(lo, hi + 1):
        if i > mid:
            aux[k] = arr[j]
            j = j + 1
        elif j > hi:
            aux[k] = arr[i]
            i = i + 1
        elif arr[i] < arr[j]:
            aux[k] = arr[i]
            i = i + 1
        else:
            aux[k] = arr[j]
            j = j + 1
    for k in range(lo, hi + 1):
        arr[k] = aux[k]

# compare O(NlgN)
def merge_sort2(arr):
    length = len(arr)
    aux = [x for x in range(length)]
    sz = 1
    while sz < length:
        lo = 0
        while lo < length - sz:
            merge(arr, lo, lo + sz - 1, min(lo + sz + sz - 1, length - 1), aux)
            lo += sz * 2
        sz += sz

def main():
    arr = prepare()
    arr2 = copy.deepcopy(arr)
    print arr
    merge_sort(arr)
    print arr
    print arr2
    merge_sort2(arr2)
    print arr2

if __name__ == '__main__':
    main()
