import math
from random import randint


def shuffledRange(length, swaps):
    result = [*range(length)]
    for i in range(swaps):
        result = swap(result, randint(0, length-1), randint(0, length-1))
    return result


def isSorted(arr):
    if len(arr) <= 1:
        return True
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
    return True


def swap(arr, a, b):
    arrCopy = arr[:]
    arrCopy[a] = arr[b]
    arrCopy[b] = arr[a]
    return arrCopy


def bubbleSort(arr):
    arrCopy = arr[:]
    history = []
    comparisons = len(arrCopy)

    while not isSorted(arrCopy):
        comparisons -= 1
        for i in range(comparisons):
            if arrCopy[i] > arrCopy[i+1]:
                arrCopy = swap(arrCopy, i, i+1)
            history.append(arrCopy)
    return history


def shellSort(arr):
    arrCopy = arr[:]
    history = []
    shellSize = math.floor(len(arrCopy) / 2)

    while not isSorted(arrCopy):
        a = 0
        b = shellSize
        while b < len(arrCopy):
            if arrCopy[a] > arrCopy[b]:
                arrCopy = swap(arrCopy, a, b)
            a += 1
            b += 1
            history.append(arrCopy)
        shellSize -= 1
    return history


def mergeSort(arr, start=0, end=None):
    history = []

    if end is None:
        end = len(arr)

    if end - start <= 1:
        return [arr]

    pivotIndex = math.floor(start + (end - start) / 2)

    history += mergeSort(arr, start, pivotIndex)
    history += mergeSort(history[-1], pivotIndex, end)
    history += merge(history[-1], start, pivotIndex, end)

    return history


def merge(arr, start, pivotIndex, end):
    arrCopy1 = arr[start:pivotIndex]
    arrCopy2 = arr[pivotIndex:end]
    result = []
    history = []

    while len(arrCopy1) and len(arrCopy2):
        if arrCopy1[0] < arrCopy2[0]:
            result.append(arrCopy1[0])
            arrCopy1 = arrCopy1[1:]
        else:
            result.append(arrCopy2[0])
            arrCopy2 = arrCopy2[1:]
        history.append(arr[:start] + result + arrCopy1 + arrCopy2 + arr[end:])

    if len(arrCopy1):
        result += arrCopy1
    else:
        result += arrCopy2
    history.append(arr[:start] + result + arr[end:])
    return history
