from src.bubblesort import bubbleSort
from src.heapsort import heapSort
from src.insertionsort import insertionSort
from src.mergesort import mergeSort
from src.quicksort import quickSort
from src.radixsort import radixSort
from src.selectionsort import selectionSort

if __name__ == "__main__":
    testArr = [3, 2, 1, 4, 5, 2, 1, 233, 123, 432, 123]
    bubbleSort(testArr)
    print("bubble sort: ")
    print(testArr)

    testArr = [3, 2, 1, 4, 5, 2, 1, 233, 123, 432, 123]
    heapSort(testArr)
    print("heap sort: ")
    print(testArr)

    testArr = [3, 2, 1, 4, 5, 2, 1, 233, 123, 432, 123]
    insertionSort(testArr)
    print("insertion sort: ")
    print(testArr)

    testArr = [3, 2, 1, 4, 5, 2, 1, 233, 123, 432, 123]
    mergeSort(testArr, 0, len(testArr) - 1)
    print("merge sort: ")
    print(testArr)

    testArr = [3, 2, 1, 4, 5, 2, 1, 233, 123, 432, 123]
    quickSort(testArr, 0, len(testArr) - 1)
    print("quick sort: ")
    print(testArr)

    testArr = [3, 2, 1, 4, 5, 2, 1, 233, 123, 432, 123]
    radixSort(testArr)
    print("radix sort: ")
    print(testArr)

    testArr = [3, 2, 1, 4, 5, 2, 1, 233, 123, 432, 123]
    selectionSort(testArr, len(testArr))
    print("selection sort: ")
    print(testArr)