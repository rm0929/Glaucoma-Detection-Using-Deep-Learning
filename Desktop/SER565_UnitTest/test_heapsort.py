import pytest
import unittest
from heapsort import heapSort

class TestHeapSort(unittest.TestCase):

    def test_heap_sort(self):
        # Test Case 1
        arr1 = [12, 11, 13, 5, 6, 7]
        expected_sorted_arr1 = [5, 6, 7, 11, 12, 13]
        heapSort(arr1)
        self.assertEqual(arr1, expected_sorted_arr1)

        # Test Case 2
        arr2 = [5, 2, 9, 1, 5, 6]
        expected_sorted_arr2 = [1, 2, 5, 5, 6, 9]
        heapSort(arr2)
        self.assertEqual(arr2, expected_sorted_arr2)

        # Test Case 3
        arr3 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        expected_sorted_arr3 = [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
        heapSort(arr3)
        self.assertEqual(arr3, expected_sorted_arr3)

    def test_heap_sort_empty_array(self):
        # Test with an empty array
        empty_array = []
        heapSort(empty_array)
        self.assertEqual(empty_array, [])

    def test_heap_sort_single_element_array(self):
        # Test with an array containing a single element
        single_element_array = [42]
        heapSort(single_element_array)
        self.assertEqual(single_element_array, [42])

    def test_heap_sort_already_sorted_array(self):
        # Test with an array that is already sorted
        sorted_array = [1, 2, 3, 4, 5]
        expected_sorted_array = [1, 2, 3, 4, 5]
        heapSort(sorted_array)
        self.assertEqual(sorted_array, expected_sorted_array)



if __name__ == '__main__':
    unittest.main()
