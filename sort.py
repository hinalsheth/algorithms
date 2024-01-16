# Sorting

import unittest

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2  # midpoint of array
    L = arr[:mid]  # Sort two halves of array
    R = arr[mid:]

    merge_sort(L)  # Sorting the first half
    merge_sort(R)  # Sorting the second half

    i = j = k = 0

    # Copy data to temp arrays L[] and R[]
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Append remaining elements
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1

    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1

    return arr

def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

class TestSort(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(merge_sort([]), [])
        self.assertEqual(quicksort([]), [])

    def test_single_element(self):
        self.assertEqual(merge_sort([1]), [1])
        self.assertEqual(quicksort([1]), [1])

    def test_sorted(self):
        self.assertEqual(merge_sort([1, 2, 3, 4]), [1, 2, 3, 4])
        self.assertEqual(quicksort([1, 2, 3, 4]), [1, 2, 3, 4])

    def test_reverse(self):
        self.assertEqual(merge_sort([4, 3, 2, 1]), [1, 2, 3, 4])
        self.assertEqual(quicksort([4, 3, 2, 1]), [1, 2, 3, 4])

    def test_unsorted(self):
        self.assertEqual(merge_sort([12, 11, 13, 5, 6, 7]), [5, 6, 7, 11, 12, 13])
        self.assertEqual(quicksort([12, 11, 13, 5, 6, 7]), [5, 6, 7, 11, 12, 13])

# To run the tests
if __name__ == '__main__':
    unittest.main()
