import time
from numpy.random import seed, randint
from src.bubblesort import bubbleSort
from src.heapsort import heapSort
from src.insertionsort import insertionSort
from src.mergesort import mergeSort
from src.quicksort import quickSort
from src.radixsort import radixSort
from src.selectionsort import selectionSort

if __name__ == "__main__":
    seed(42069)
    testArr = randint(0, 4096, 4096)
    bubbleST = time.time()
    bubbleSort(testArr)
    bubbleET = time.time()
    print("bubble sort time: ", bubbleET - bubbleST)
    print(testArr)

    testArr = randint(0, 4096, 4096)
    heapST = time.time()
    heapSort(testArr)
    heapET = time.time()
    print("heap sort time: ", heapET - heapST)
    print(testArr)

    testArr = randint(0, 4096, 4096)
    insertionST = time.time()
    insertionSort(testArr)
    insertionET = time.time()
    print("insertion sort time: ", insertionET - insertionST)
    print(testArr)

    testArr = randint(0, 4096, 4096)
    mergeST = time.time()
    mergeSort(testArr, 0, len(testArr) - 1)
    mergeET = time.time()
    print("merge sort time: ", mergeET - mergeST)
    print(testArr)

    testArr = randint(0, 4096, 4096)
    quickST = time.time()
    quickSort(testArr, 0, len(testArr) - 1)
    quickET = time.time()
    print("quick sort time: ", quickET - quickST)
    print(testArr)

    testArr = randint(0, 4096, 4096)
    radixST = time.time()
    radixSort(testArr)
    radixET = time.time()
    print("radix sort time: ", radixET - radixST)
    print(testArr)

    testArr = randint(0, 4096, 4096)
    selectionST = time.time()
    selectionSort(testArr, len(testArr))
    selectionET = time.time()
    print("selection sort time: ", selectionET - selectionST)
    print(testArr)