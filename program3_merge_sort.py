"""
Experiment 2: Searching and Divide-and-Conquer
Program 3: Merge Sort
Aim: Sort an array using divide and conquer.
"""

def merge_sort(a):
    if len(a) <= 1:
        return a[:]
    mid = len(a) // 2
    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])
    result, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    return result + left[i:] + right[j:]

print(merge_sort([9, 3, 7, 1, 6]))
