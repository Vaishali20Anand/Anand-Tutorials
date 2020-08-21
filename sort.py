#!/bin/python3

import random
import time

def merge(arr, l, m, r): 
    n1 = m - l + 1
    n2 = r- m  
    L = [0] * (n1) 
    R = [0] * (n2) 
    # Copy data to temp arrays L[] and R[] 
    for i in range(0 , n1): 
        L[i] = arr[l + i] 
    for j in range(0 , n2): 
        R[j] = arr[m + 1 + j] 
    # Merge the temp arrays back into arr[l..r] 
    i = 0     # Initial index of first subarray 
    j = 0     # Initial index of second subarray 
    k = l     # Initial index of merged subarray 
    while i < n1 and j < n2 : 
        if L[i] <= R[j]: 
            arr[k] = L[i] 
            i += 1
        else: 
            arr[k] = R[j] 
            j += 1
        k += 1
    # Copy the remaining elements of L[],
    while i < n1: 
        arr[k] = L[i]
        
        i += 1
        k += 1
    # Copy the remaining elements of R[]
    while j < n2: 
        arr[k] = R[j] 
        j += 1
        k += 1

def mergeSort(arr,l,r): 
    if l < r: 
        # Same as (l+r)//2, but avoids overflow for large l and h 
        m = (l+(r-1))//2
        # Sort first and second halves 
        mergeSort(arr, l, m) 
        mergeSort(arr, m+1, r) 
        merge(arr, l, m, r) 

def bubbleSort(arr): 
    n = len(arr) 
    # Traverse through all array elements 
    for i in range(n):
        swapped = False
  
        # Last i elements are already 
        #  in place 
        for j in range(0, n-i-1): 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 
                swapped = True
        # IF no two elements were swapped 
        # by inner loop, then break 
        if swapped == False: 
            break

def partition(arr,low,high): 
    i = ( low-1 )         # index of smaller element 
    pivot = arr[high]     # pivot 
  
    for j in range(low , high): 
  
        # If current element is smaller than the pivot 
        if   arr[j] < pivot: 
          
            # increment index of smaller element 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 
 
# Function to do Quick sort 
def quickSort(arr,low,high): 
    if low < high: 
        # pi is partitioning index, arr[p] is now 
        # at right place 
        pi = partition(arr,low,high) 
        # Separately sort elements before 
        # partition and after partition 
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high) 


def selectionSort(arr):
    for i in range(0, len(arr) - 1):
        smallest = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[smallest]:
                smallest = j
        arr[i], arr[smallest] = arr[smallest], arr[i]

def insertionSort(arr): 
    # Traverse through 1 to len(arr) 
    for i in range(1, len(arr)): 
        key = arr[i] 
        # Move elements of arr[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position 
        j = i-1
        while j >=0 and key < arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = key 

if __name__ == '__main__':
    n = int(input("Enter the number of element in the array : "))
    randomlist = []
    for i in range(0,n):
        temp = random.randint(1,1000)
        randomlist.append(temp)
    lis=[0,0,0,0,0]
    arr = randomlist.copy()
    bubble_start = time.time()
    bubbleSort(arr) 
    bubble_end = time.time()
    print("\n\nTime taken by Bubble Sort is",bubble_end - bubble_start)
    lis[0]=bubble_end - bubble_start

    arr = randomlist.copy()
    mereg_start = time.time()
    mergeSort(arr,0,len(randomlist)-1) 
    merge_end = time.time()
    print("\nTime taken by Merge Sort is",merge_end - mereg_start)
    lis[1]=merge_end - mereg_start

    arr = randomlist.copy()
    quick_start = time.time()
    quickSort(arr,0, len(arr)-1) 
    quick_end = time.time()
    print("\nTime taken by Quick Sort is",quick_end - quick_start)
    lis[2]=quick_end - quick_start
    
    arr = randomlist.copy()
    selection_start = time.time()
    selectionSort(arr) 
    selection_end = time.time()
    print("\nTime taken by Selection Sort is",selection_end - selection_start)
    lis[3]=selection_end - selection_start
    
    arr = randomlist.copy()
    insertion_start = time.time()
    insertionSort(arr) 
    insertion_end = time.time()
    print("\nTime taken by Insertion Sort is",insertion_end - insertion_start)
    lis[4]=insertion_end - insertion_start
    print("")
    print("")
    min1=lis[0]
    m=0
    count=0
    for i in lis:
        if i==0:
            count+=1
    if count>1:
        print("Entered size of array is too small to compare!!!")
    else:
        for i in range(5):
            if min1>lis[i]:
                min1=lis[i]
                m=i
        if m== 0:
            print("The best Algorithm for you is Bubble Sorting")
        if m== 1:
            print("The best Algorithm for you is Merge Sorting")
        if m== 2:
            print("The best Algorithm for you is Quick Sorting")
        if m== 3:
            print("The best Algorithm for you is Selection Sorting")
        if m== 4:
            print("The best Algorithm for you is Insertion Sorting")
    
    hold = input()
    