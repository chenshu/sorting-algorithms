#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint
import copy

def prepare():
    cnt = 10
    return [randint(0, cnt) for _ in range(cnt)]

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def shell_sort(arr):
    length = len(arr)
    step = 1
    while step < length / 3:
        step = 3 * step + 1
    while step >= 1:
        for i in range(step):
            for j in range(i + step, length, step):
                for k in range(j, i, -(step)):
                    if arr[k] < arr[k - step]:
                        swap(arr, k - step, k)
                    else:
                        break
        step /= 3

def shell_sort2(arr):
    length = len(arr)
    step = 1
    while step < length / 3:
        step = 3 * step + 1
    while step >= 1:
        for i in range(step, length):
            for j in range(i, 0, -(step)):
                if arr[j] < arr[j - step]:
                    swap(arr, j - step, j)
                else:
                    break
        step /= 3

def main():
    arr = prepare()
    arr2 = copy.deepcopy(arr)
    print arr
    shell_sort(arr)
    print arr
    print arr2
    shell_sort2(arr2)
    print arr2

if __name__ == '__main__':
    main()
