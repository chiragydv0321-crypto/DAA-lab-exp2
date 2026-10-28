"""
Experiment 2: Searching and Divide-and-Conquer
Program 4: Count Inversions using Merge Sort
Aim: Count pairs i < j for which a[i] > a[j].
"""

def count_inversions(a):
    def sort_count(x):
        if len(x) <= 1:
            return x, 0
        mid = len(x) // 2
        left, c1 = sort_count(x[:mid])
        right, c2 = sort_count(x[mid:])
        merged, i, j, cross = [], 0, 0, 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i]); i += 1
            else:
                merged.append(right[j]); j += 1
                cross += len(left) - i
        return merged + left[i:] + right[j:], c1 + c2 + cross
    return sort_count(a)[1]

print(count_inversions([8, 4, 2, 1]))
