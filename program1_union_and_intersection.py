"""
Experiment 2: Searching and Divide-and-Conquer
Program 1: Union and Intersection of Two Sorted Arrays
Aim: Find union and intersection of two sorted arrays.
"""

def union_intersection(a, b):
    i = j = 0
    union, inter = [], []
    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            if not union or union[-1] != a[i]:
                union.append(a[i])
            inter.append(a[i])
            i += 1
            j += 1
        elif a[i] < b[j]:
            if not union or union[-1] != a[i]:
                union.append(a[i])
            i += 1
        else:
            if not union or union[-1] != b[j]:
                union.append(b[j])
            j += 1
    while i < len(a):
        if not union or union[-1] != a[i]:
            union.append(a[i])
        i += 1
    while j < len(b):
        if not union or union[-1] != b[j]:
            union.append(b[j])
        j += 1
    return union, inter

print(union_intersection([1, 2, 4, 5], [2, 4, 6]))
