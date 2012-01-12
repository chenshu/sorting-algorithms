#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint

def prepare(cnt):
    arr = list()
    for i in range(cnt):
        arr.append(randint(0, cnt))
    return arr

def main(cnt):
    arr = prepare(cnt)
    print arr
    insertion_sort(arr, cnt)
    print arr

def insertion_sort(arr, cnt):
    # 第一个元素认为已经排序
    # 从下一个元素开始，和已经排序的元素从后向前开始比较
    for i in range(1, cnt):
        k = i
        temp = arr[k]
        # 如果这个元素比已经排序的元素小
        while (k > 0 and temp < arr[k - 1]):
            arr[k] =  arr[k - 1]
            k -= 1
        arr[k] = temp

if __name__ == '__main__':
    main(10)
