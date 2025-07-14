########################################
# MSCS 532 Assignment 6 (Part 1)
# Medians and Order Statistics
########################################

import random

def deterministic_select(arr, k):
    """
    Select the k-th smallest element using the Median of Medians algorithm.
    :param arr: List of comparable elements.
    :param k: 1-based index (e.g., k=1 returns the smallest element).
    :return: The k-th smallest element.
    """
    if not 1 <= k <= len(arr):
        raise IndexError("k is out of bounds")

    def partition(arr, pivot):
        lows = [el for el in arr if el < pivot]
        highs = [el for el in arr if el > pivot]
        pivots = [el for el in arr if el == pivot]
        return lows, pivots, highs

    def select(arr, k):
        if len(arr) <= 5:
            return sorted(arr)[k - 1]

        # Divide arr into sublists of 5 and find medians
        chunks = [arr[i:i + 5] for i in range(0, len(arr), 5)]
        medians = [sorted(chunk)[len(chunk) // 2] for chunk in chunks]
        median_of_medians = select(medians, len(medians) // 2 + 1)

        lows, pivots, highs = partition(arr, median_of_medians)

        if k <= len(lows):
            return select(lows, k)
        elif k <= len(lows) + len(pivots):
            return median_of_medians
        else:
            return select(highs, k - len(lows) - len(pivots))

    return select(arr, k)

def randomized_select(arr, k):
    """
    Select the k-th smallest element using the Randomized Quickselect algorithm.
    :param arr: List of comparable elements.
    :param k: 1-based index (e.g., k=1 returns the smallest element).
    :return: The k-th smallest element.
    """
    if not 1 <= k <= len(arr):
        raise IndexError("k is out of bounds")

    def select(arr, k):
        if len(arr) == 1:
            return arr[0]

        pivot = random.choice(arr)
        lows = [el for el in arr if el < pivot]
        highs = [el for el in arr if el > pivot]
        pivots = [el for el in arr if el == pivot]

        if k <= len(lows):
            return select(lows, k)
        elif k <= len(lows) + len(pivots):
            return pivot
        else:
            return select(highs, k - len(lows) - len(pivots))

    return select(arr, k)

arr = [7, 10, 4, 3, 20, 15, 10, 4]
k = 4

print("Deterministic:", deterministic_select(arr, k))  # e.g., 7
print("Randomized:", randomized_select(arr, k))        # e.g., 7 (may vary across runs)

