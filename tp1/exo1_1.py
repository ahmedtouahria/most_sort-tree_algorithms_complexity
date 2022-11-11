import sys
import time
from functions.bubblesort import bubbleSort
from functions.quicksort import quickSort
from functions.mergesort import mergeSort
from functions.insertionsort import insertionSort
from functions.selectionsort import selectionSort
"""EXO 1"""
from functions.utils import array_of_random



#print(sys.getrecursionlimit())  # -> 1000 !

# I change the recursion limit with sys.setrecursionlimit:

sys.setrecursionlimit(6000)

if __name__ == '__main__':
    array_of_n = [100, 200, 300, 400, 500, 1000, 2000, 3000, 4000, 5000] # array of sizes
    for arr in array_of_n:
        new_array = array_of_random(arr) # create array of size n -> array_of_n[]
        array_size = len(new_array) # get array size
        start = time.time() # start time of bubbleSort excution
        bubbleSort(new_array)
        end = time.time() # end time of bubbleSort excution
        print(f"The time of execution of bubbleSort algorithm while n = {arr} is :",
              (end-start) * 10**3, "ms")
        start = time.time()
        insertionSort(new_array)
        end = time.time()
        print(f"The time of execution of insertionSort algorithm while n= {arr} is :",
              (end-start) * 10**3, "ms")
        start = time.time()
        selectionSort(new_array, array_size)
        end = time.time()
        print(f"The time of execution of selectionSort algorithm while n= {arr} is :",
              (end-start) * 10**3, "ms")
        start = time.time()
        quickSort(new_array, 0, array_size-1)
        end = time.time()
        print(f"The time of execution of quickSort algorithm while n= {arr} is :",
              (end-start) * 10**3, "ms")

    sys.setrecursionlimit(1000)
