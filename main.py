import time
from numpy.random import seed, randint
from src.bubblesort import bubbleSort
from src.heapsort import heapSort
from src.insertionsort import insertionSort
from src.mergesort import mergeSort
from src.quicksort import quickSort
from src.radixsort import radixSort
from src.selectionsort import selectionSort

def time_rank(time1, time2, time3, time4, time5, time6, time7):
    arr = [time1, time2, time3, time4, time5, time6, time7]
    print(sorted(arr, key = lambda x:float(x)))
    sorts = {}
    for i in range(7):
        sorts[i] = time1
    print(sorts[i])

if __name__ == "__main__":
    seed(42069)
    testArr = randint(0, 4096, 4096)
    bubbleST = time.time()
    bubbleSort(testArr)
    bubbleET = time.time()
    bubbleTime = bubbleET - bubbleST
    print("bubble sort time: ", bubbleTime)
    #print(testArr)

    testArr = randint(0, 4096, 4096)
    heapST = time.time()
    heapSort(testArr)
    heapET = time.time()
    heapTime = heapET - heapST
    print("heap sort time: ", heapTime)
    #print(testArr)

    testArr = randint(0, 4096, 4096)
    insertionST = time.time()
    insertionSort(testArr)
    insertionET = time.time()
    insertionTime = insertionET - insertionST
    print("insertion sort time: ",insertionTime)
    #print(testArr)

    testArr = randint(0, 4096, 4096)
    mergeST = time.time()
    mergeSort(testArr, 0, len(testArr) - 1)
    mergeET = time.time()
    mergeTime = mergeET - mergeST
    print("merge sort time: ", mergeTime)
    #print(testArr)

    testArr = randint(0, 4096, 4096)
    quickST = time.time()
    quickSort(testArr, 0, len(testArr) - 1)
    quickET = time.time()
    quickTime = quickET - quickST
    print("quick sort time: ", quickTime)
    #print(testArr)

    testArr = randint(0, 4096, 4096)
    radixST = time.time()
    radixSort(testArr)
    radixET = time.time()
    radixTime = radixET - radixST
    print("radix sort time: ",radixTime)
    #print(testArr)

    testArr = randint(0, 4096, 4096)
    selectionST = time.time()
    selectionSort(testArr, len(testArr))
    selectionET = time.time()
    selectionTime = selectionET - selectionST
    print("selection sort time: ", selectionTime)
    #print(testArr)

    time_rank(bubbleTime, heapTime, insertionTime, mergeTime, quickTime, radixTime, selectionTime)

