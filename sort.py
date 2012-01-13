#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint

def prepare(cnt):
    return [randint(0, cnt) for i in range(cnt)]

# 插入排序
# stable
# O(1) extra space
# O(n^2) comparisons
# O(n^2) swaps
# Adaptive: O(n) when nearly sorted
def insertion_sort(arr, cnt):
    # 假设第一个元素为已经排序元素
    # 遍历所有未排序元素
    for i in range(1, cnt):
        # 未排序的元素
        temp = arr[i]
        k = i
        # 未排序元素与已排序元素从大到小分别比较
        while (k > 0 and temp < arr[k - 1]):
            # 这个未排序元素比已排序元素小，已排序元素向后移一位
            arr[k] = arr[k - 1]
            k -= 1
        arr[k] = temp

# 选择排序
# not stable
# O(1) extra space
# O(n^2) comparisons
# O(n) swaps
# Not adaptive
def selection_sort(arr, cnt):
    # 遍历所有元素
    for i in range(cnt):
        # 当前元素认为是最小的
        k = i
        # 找到后面的元素中比当前元素小的
        for j in range(i + 1, cnt):
            if arr[j] < arr[k]:
                k = j
        # 最小的元素与当前元素交换位置
        arr[i], arr[k] = arr[k], arr[i]

# 冒泡排序
# stable
# O(1) extra space
# O(n^2) comparisons
# O(n^2) swaps
# Adaptive: O(n) when nearly sorted
def bubble_sort(arr, cnt):
    # 遍历所有元素个数次
    for i in range(cnt):
        # 是否还有交换的
        swaped = False
        # 比较所有剩余元素
        for j in range(cnt - i - 1):
            # 找出最大的元素,交换到最后
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            # 已经交换过
            swaped = True
        # 如果不需要交换, 不需要遍历所有元素个数次
        if swaped == False:
            break

# Shell排序
def shell_sort(arr, cnt):
    gap = 0
    while gap <= cnt:
        gap = gap * 3 + 1
    while gap > 0:
        for i in range(gap, cnt):
            temp = arr[i]
            k = i - gap
            while (k >= 0 and temp < arr[k]):
                arr[k + gap] = arr[k]
                k -= gap
            arr[k + gap] = temp
        gap = (gap - 1) / 3

# Shell排序
def shell_sort2(arr, cnt):
    gap = 0
    while gap <= cnt:
        gap = gap * 3 + 1
    while gap > 0:
        for i in range(gap, cnt):
            temp = arr[i]
            k = i
            while (k > gap - 1 and temp < arr[k - gap]):
                arr[k] = arr[k - gap]
                k -= gap
            arr[k] = temp
        gap = (gap - 1) / 3

def main():
    cnt = 10
    arr = prepare(cnt)
    #arr = [i for i in range(cnt)]
    #arr.sort()
    #arr.reverse()
    print arr
    arr1 = list(arr)
    insertion_sort(arr1, cnt)
    print arr1
    arr2 = list(arr)
    selection_sort(arr2, cnt)
    print arr2
    arr3 = list(arr)
    bubble_sort(arr3, cnt)
    print arr3
    arr4 = list(arr)
    shell_sort(arr4, cnt)
    print arr4
    arr5 = list(arr)
    shell_sort2(arr5, cnt)
    print arr5

if __name__ == '__main__':
    main()
