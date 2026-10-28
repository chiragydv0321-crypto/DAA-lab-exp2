"""
Experiment 2: Searching and Divide-and-Conquer
Program 2: Search in Rotated Sorted Array
Aim: Search for a target in a rotated sorted array using modified binary search.
"""

def rotated_search(a, target):
    left, right = 0, len(a) - 1
    while left <= right:
        mid = (left + right) // 2
        if a[mid] == target:
            return mid
        if a[left] <= a[mid]:
            if a[left] <= target < a[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if a[mid] < target <= a[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1

print(rotated_search([6, 7, 8, 1, 2, 3, 4], 2))
