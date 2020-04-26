# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/ctci-merge-sort/problem
# Difficulty: Hard
# Max Score: 45
# Language: Python

# ========================
#         Solution
# ========================

INVERSION_COUNT = 0

def merge_sort(array, length_array):
    '''Use Inversion Count'''
    return _merge_sort(array)

def _merge_sort(array):
    '''Use MergeSort to count inversions'''
    if len(array) > 1:
        mid = len(array)//2
        left_half = array[:mid]
        right_half = array[mid:]

        # Will calculate inversion counts in the left subarray
        # Will call the mergesort with right_half and left_half
        _merge_sort(left_half)
        _merge_sort(right_half)

        # Will call the merge to sort our tables right_half and left_half
        merge(array, left_half, right_half)
        # Will calculate inversion counts in right subarray
        # Will merge two subarrays in a sorted subarray

def merge(array, left_half, right_half):
    '''Will merge two subarrays in a single sorted subarray'''
    global INVERSION_COUNT # Will store our inventions count

    left = 0 # Starting index of left subarray
    right = 0 # Starting index of right subarray
    index = 0 # Starting index of to be sorted subarray

    # Conditions are checked to make sure that i and j do not exceed their subarray limits
    left_length = len(left_half)
    right_length = len(right_half)

    while left < left_length and right < right_length:
        # There will be no inversion if left_half[left] <= right_half[right]
        array_1 = left_half[left]
        array_2 = right_half[right]
        if array_1 <= array_2:
            array[index] = array_1
            index += 1
            left += 1
        else:
            # Inversion will occur
            array[index] = array_2
            INVERSION_COUNT += left_length - left
            index += 1
            right += 1

    # Copy the remaining elements of left subarray into a temporary array
    while left < left_length:
        array[index] = left_half[left]
        left += 1
        index += 1

    # Copy the remaining elements of right subarray into a temporary array
    while right < right_length:
        array[index] = right_half[right]
        right += 1
        index += 1

for _ in range(int(input())):
    length_array = int(input())
    array = list(map(int, input().split()))

    merge_sort(array, length_array)

    print(INVERSION_COUNT)
    INVERSION_COUNT = 0
