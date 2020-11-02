# Quick Sort | Time: O(nlogn), Space: O(logn)
# Version 1
def quick_sort(self, array):
    self.quick_sort_helper(array, 0, len(array) - 1)

def quick_sort_helper(self, array, start, end):
    if start >= end:
        return

    left, right = start, end
    pivot = array[(left + right) // 2]
    while left <= right:
        while left <= right and array[left] < pivot:
            left += 1
        while left <= right and array[right] > pivot:
            right -= 1
        while left <= right:
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1
    quick_sort_helper(a, start, right)
    quick_sort_helper(a, left, end)

# version 2
def quickSort(array):
    quickSortHelper(array, 0, len (array) - 1)
    return array

def quickSortHelper(array, startIdx, endIdx):
    if startIdx > endIdx:
        return
    pivotIdx = startIdx
    leftIdx = startIdx + 1
    rightIdx = endIdx
    while rightIdx >= leftIdx:
        if array[leftIdx] > array[pivotIdx] and array[rightIdx] < array[pivotIdx]:
            swap(leftIdx, rightIdx, array)
        if array[leftIdx] < array[pivotIdx]:
            leftIdx += 1
        if array[rightIdx] >= array[pivotIdx]:
            rightIdx -= 1
    swap(rightIdx, pivotIdx, array)
    leftIsSmaller = rightIdx - 1 - startIdx < endIdx - (startIdx + 1)
    if leftIsSmaller:
        quickSortHelper(array, startIdx, rightIdx - 1)
        quickSortHelper(array, rightIdx + 1, endIdx)

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]

